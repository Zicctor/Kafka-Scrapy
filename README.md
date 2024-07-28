
# Project Description: Scrapy, Kafka, PostgreSQL, and Flask 🍷

![Cover](https://wallpapercave.com/wp/wp1828905.png)

<!-- English Content -->
<div id="english-content">
### Getting Started 🍸
<div style="border-left: 4px solid #e74c3c; background-color: #fdecea; padding: 10px;">
  <strong>Windows Issues</strong>
  <p>Kafka is not intended to be run on Windows natively and has several issues that may arise over time.</p>
</div>
### Git clone repository
```
git clone https://github.com/your-username/kafka_scrapy_flask.git
cd kafka_scrapy_flask
```

### Create Virtual Envrionment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Install Dependencies 
```
pip install -r requirements.txt
```

### Configure Kafka 

💫 "Apache Kafka is optimized for Linux environments like Ubuntu. Installing it on Windows can introduce complexities and potential performance issues."
- Install Kafka: [Apache Kafka](https://kafka.apache.org/)

```
# Run zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Run Kafka
bin/kafka-server-start.sh config/server.properties

# Create a topic
bin/kafka-topics.sh --create --topic webscrapping --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### Database Setup
- Connect to your PostgreSQL database.
[PostgreSQL](https://www.postgresql.org/)
- Create new connection + user

### Flask App 
- Develop the Flask app within the `Bookscrape/bookscraper/flask_app/app.py` folder.
- Define routes to retrieve data from PostgreSQL.
- Implement visualizations using libraries like Plotly or Matplotlib.
```
python app.py
```

## Conclusion
By integrating Scrapy, Kafka, PostgreSQL, and Flask, you’ll build a robust data pipeline that scrapes book-related information, stores it in a database, and presents it via a user-friendly web interface. Happy coding! 🚀
