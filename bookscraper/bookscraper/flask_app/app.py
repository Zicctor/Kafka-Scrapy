from flask import Flask, render_template, request, jsonify
import subprocess
import os
import psycopg2
from datetime import datetime

app = Flask(__name__)

# Global variable to track the spider status
spider_running = False

@app.route('/')
def home():
    return render_template('index.html', spider_running=spider_running)

@app.route('/start_spider', methods=['POST'])
def start_spider():
    global spider_running
    if not spider_running:
        spider_running = True
        subprocess.Popen(['scrapy', 'crawl', 'bookspider'])
        return jsonify({'status': 'Spider started'})
    else:
        return jsonify({'status': 'Spider already running'})

@app.route('/stop_spider', methods=['POST'])
def stop_spider():
    global spider_running
    if spider_running:
        os.system('pkill -f "scrapy crawl bookspider"')
        spider_running = False
        return jsonify({'status': 'Spider stopped'})
    else:
        return jsonify({'status': 'Spider not running'})

@app.route('/reset', methods=['POST'])
def reset():
    global spider_running
    spider_running = False
    return jsonify({'status': 'Reset complete'})

@app.route('/status', methods=['GET'])
def status():
    global spider_running
    return jsonify({'spider_running': spider_running})

@app.route('/load_data', methods=['GET'])
def load_data():
    limit = request.args.get('limit', default=50, type=int)
    sort_order = request.args.get('sort_order', default='asc')
    page = request.args.get('page', default=1, type=int)
    offset = (page - 1) * limit

    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='postgres',
        database='postgres'
    )
    cur = conn.cursor()
    
    cur.execute("SELECT COUNT(*) FROM books")
    total = cur.fetchone()[0]

    cur.execute(f"SELECT id, title, price, availability FROM books ORDER BY id {sort_order} LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    
    cur.close()
    conn.close()
    
    data = {
        'total': total,
        'rows': [{'id': row[0], 'title': row[1], 'price': row[2], 'availability': row[3]} for row in rows]
    }
    return jsonify(data)

@app.route('/delete_all_data', methods=['POST'])
def delete_all_data():
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='postgres',
        database='postgres'
    )
    cur = conn.cursor()
    
    cur.execute("DELETE FROM books")
    conn.commit()

    # Reset the primary key sequence
    cur.execute("ALTER SEQUENCE books_id_seq RESTART WITH 1")
    conn.commit()
    
    cur.close()
    conn.close()
    
    return jsonify({'status': 'All data deleted'})

if __name__ == '__main__':
    app.run(debug=True)
