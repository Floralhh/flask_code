# coding=utf8
import redis


class Config(object):
    """工程配置信息"""
    SECRET_KEY = 'saggeslkrbs234#@gsd'
    DEBUG = True
    # 数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # flask_session用到的信息
    SESSION_TYPE = "redis"  # 指明保存到redis中
    SESSION_USE_SIGNER = True  # 让cookie中的session_id被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用的redis实例
    PERMANENT_SESSION_LIFETIME = 86400  # session的有效期，单位秒

class DevelopmentConfig(Config):
    """开发者模式"""
    DEBUG = True
    # 支付宝
    ALIPAY_APPID = "2016091400512564"
    ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do"

class ProductionConfig(Config):
    """生产模式 线上模式"""
    pass


config_dict = {
    "develop": DevelopmentConfig,
    "produce": ProductionConfig
}
