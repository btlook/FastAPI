TORTOISE_ORM = {
    'connections': {
        # Dict format for connection
        'default': {
            # 'engine': 'tortoise.backends.asyncpg', # PostgreSQL
            'engine': 'tortoise.backends.mysql',  # MySQL or Mariadb
            'credentials': {
                'host': 'localhost',
                'port': '3306',
                'user': 'root',
                'password': 'root',
                'database': 'fastapi',
                "minsize": 1,
                "maxsize": 5,
                "charset": "utf8",
                "echo": True
            },
        },
    },
    "apps": {
        'models': {
            'models': ['models',"aerich.models"],
            'default_connection': 'default',
        }
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai',
}
