# Project Description: Scrapy, Kafka, PostgreSQL, and Flask 🍷

![Cover](https://wallpapercave.com/wp/wp1828905.png)

## Getting Started 🍸

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
- Install Kafka locally or set up a remote Kafka cluster.
- Configure Kafka topics and ensure that Scrapy spiders publish data to the appropriate topic.

### Database Setup
- Connect to your PostgreSQL database.
- Create a table (e.g., books) to store scraped data.
- Define columns for book titles, authors, ratings, etc.

### Flask App 
- Develop the Flask app within the `Bookscrape/bookscraper/flask_app/app.py` folder.
- Define routes to retrieve data from PostgreSQL.
- Implement visualizations using libraries like Plotly or Matplotlib.

### Notion note
- Check out this link for better instructions.
[Notion note](https://www.notion.so/Web-Scraping-Project-21b7fad43567476fa3016ed875cbcfb6?pvs=4)

## Conclusion
By integrating Scrapy, Kafka, PostgreSQL, and Flask, you’ll build a robust data pipeline that scrapes book-related information, stores it in a database, and presents it via a user-friendly web interface. Happy coding! 🚀

