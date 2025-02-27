
# MySQL 配置
MYSQL_CONFIG = {
    "production": {
        "db1": {
            "host": "192.168.3.26",
            "port": 3306,
            "user": "root",
            "password": "Chj1998922.",
            "database": "db1",
        },
        "db2": {
            "host": "prod.mysql.server2.ip",
            "port": 3306,
            "user": "prod_user2",
            "password": "prod_password2",
            "database": "prod_db2",
            "table": "prod_table2",
        },
        # 更多生产环境的 MySQL 配置...
    },
    "testing": {
        "db1": {
            "host": "test.mysql.server1.ip",
            "port": 3306,
            "user": "test_user1",
            "password": "test_password1",
            "database": "test_db1",
            "table": "test_table1",
        },
        "db2": {
            "host": "test.mysql.server2.ip",
            "port": 3306,
            "user": "test_user2",
            "password": "test_password2",
            "database": "test_db2",
            "table": "test_table2",
        },
        # 更多测试环境的 MySQL 配置...
    },
}

# Redis 配置
REDIS_CONFIG = {
    "production": {
        "cache1": {
            "host": "prod.redis.server1.ip",
            "port": 6379,
            "password": "prod_password1",
            "db": 0,
        },
        "cache2": {
            "host": "prod.redis.server2.ip",
            "port": 6379,
            "password": "prod_password2",
            "db": 1,
        },
        # 更多生产环境的 Redis 配置...
    },
    "testing": {
        "cache1": {
            "host": "test.redis.server1.ip",
            "port": 6379,
            "password": "test_password1",
            "db": 0,
        },
        "cache2": {
            "host": "test.redis.server2.ip",
            "port": 6379,
            "password": "test_password2",
            "db": 1,
        },
        # 更多测试环境的 Redis 配置...
    },
}

# 当前环境
ENV = "testing"  # 修改为 "production" 切换到生产环境
