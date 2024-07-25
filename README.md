
# Project Description: Scrapy, Kafka, PostgreSQL, and Flask 🍷

![Cover](https://wallpapercave.com/wp/wp1828905.png)

<!-- Language Toggle Buttons -->
<button onclick="showEnglish()">English</button>
<button onclick="showVietnamese()">Tiếng Việt</button>

<!-- English Content -->
<div id="english-content">
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
</div>

<!-- Vietnamese Content (Hidden by default) -->
<div id="vietnamese-content" style="display:none;">
## Bắt đầu 🍸

### Command để clone repo
```
git clone https://github.com/your-username/kafka_scrapy_flask.git
cd kafka_scrapy_flask
```

### Tạo Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Cài đặt các dependencies
```
pip install -r requirements.txt
```

### Cấu hình Apache Kafka
- Cài đặt Kafka: [Apache Kafka](https://kafka.apache.org/)
```
# Chạy zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties
# Chạy Kafka
bin/kafka-server-start.sh config/server.properties
# Tạo một Kafka topic
bin/kafka-topics.sh --create --topic webscrapping --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### Thiết lập cơ sở dữ liệu
- Kết nối với cơ sở dữ liệu PostgreSQL của bạn.
[PostgreSQL](https://www.postgresql.org/)
- Tạo kết nối mới + người dùng

### Ứng dụng Flask
- Phát triển ứng dụng Flask trong thư mục `Bookscrape/bookscraper/flask_app/app.py`.
- Định nghĩa các tuyến để truy xuất dữ liệu từ PostgreSQL.
- Triển khai các hình ảnh hóa sử dụng thư viện như Plotly hoặc Matplotlib.
```
python app.py
```

## Kết luận
Bằng cách tích hợp Scrapy, Kafka, PostgreSQL và Flask, bạn sẽ xây dựng một đường dẫn dữ liệu mạnh mẽ thu thập thông tin liên quan đến sách, lưu trữ trong cơ sở dữ liệu và hiển thị thông qua giao diện web thân thiện với người dùng. Chúc mã hóa vui vẻ! 🚀
</div>

<script>
function showEnglish() {
  document.getElementById('english-content').style.display = 'block';
  document.getElementById('vietnamese-content').style.display = 'none';
}

function showVietnamese() {
  document.getElementById('english-content').style.display = 'none';
  document.getElementById('vietnamese-content').style.display = 'block';
}
</script>
