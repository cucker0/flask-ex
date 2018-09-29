启动:
cd 02-flask-app
set FLASK_APP=run.py
flask run


初始化数据库
flask db init
flask db migrate -m "注释信息"
flask db upgrate

之后有变更数据模型
flask db migrate -m "注释信息"
flask db upgrate
