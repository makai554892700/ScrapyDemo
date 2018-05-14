###### scrapy 安装

    pip install Scrapy

###### 创建项目

    scrapy startproject <project_name>

###### 创建爬虫

    scrapy genspider <spider_name> <host_name>

###### 项目环境搭建

    pip install -r requirements.txt

###### 运行单个爬虫

    scrapy crawl <spider_name>

###### 启用pipelines用于处理结果
* 打开settings.py文件在ITEM_PIPELINES选项下加入peline并赋值，0-1000，数字越小越优先


