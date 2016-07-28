#_*_ coding:utf-8 _*_
import redis
#from rediscluster import RedisCluster

class redis_library(object):

	def redis_query(self,query, redishost="10.16.6.42", redisport=6379, password=''):
		"""查询redis数据库，Host、Port默认为5ed2d79f84654b13.m.cnbja.kvstore.aliyuncs.com:6379，其他请另行指定
		
		ex:
		| ${keys} | redis_query | keys * | 10.16.6.42 | 20001 |
		| ${keys} | redis_query | keys * |
		结果是返回所有数据库（10.16.6.42:20001/默认库)里的keys
		"""
		if password == '':
			r = redis.Redis(host=redishost,port=redisport)		
		else:
			r = redis.Redis(host=redishost,port=redisport,password=password)
		result = r.execute_command(str(query))
		return result

	def redis_update(self,update,redishost="5ed2d79f84654b13.m.cnbja.kvstore.aliyuncs.com",redisport=6379, password=''):
		"""更新redis数据库，Host、Port默认为10.16.6.90:6379，其他请另行指定
		
		ex:
		| redis_update | set a b | 10.16.6.42 | 20001 |
		| redis_update | set a b |
		结果设置key为a的值为b
		"""		
		if password == '':
			r = redis.Redis(host=redishost,port=redisport)		
		else:
			r = redis.Redis(host=redishost,port=redisport,password=password)
		result = r.execute_command(str(update))
		r.execute_command(update)

	def redis_query_cluster(self,query,nodes=[{"host": "10.16.6.16", "port": "7000"},{"host": "10.16.6.16", "port": "7001"},{"host": "10.16.6.16", "port": "7002"}]):
		"""查询redis集群数据库
		
		ex:
		| ${keys} | redis_query_cluster | get a | [{"host": "10.16.6.16", "port": "7000"},{"host": "10.16.6.16", "port": "7001"},{"host": "10.16.6.16", "port": "7002"}] |
		结果是返回数据库集群（[{"host": "10.16.6.16", "port": "7000"}])里的key为a的值
		"""
		if isinstance(nodes, basestring):
			nodes=eval(nodes)
		rc = RedisCluster(startup_nodes=nodes, decode_responses=True)
		querysplit = query.split()
		result = rc.execute_command(*querysplit)
		return result

	def redis_update_cluster(self,update,nodes=[{"host": "10.16.6.16", "port": "7000"},{"host": "10.16.6.16", "port": "7001"},{"host": "10.16.6.16", "port": "7002"}]):
		"""设置redis集群数据库
		
		ex:
		| ${keys} | redis_update_cluster | set a b | [{"host": "10.16.6.16", "port": "7000"},{"host": "10.16.6.16", "port": "7001"},{"host": "10.16.6.16", "port": "7002"}] |
		结果是设置数据库集群（[{"host": "10.16.6.16", "port": "7000"}])里的key-value为a:b
		"""		
		if isinstance(nodes, basestring):
			nodes=eval(nodes)
		rc = RedisCluster(startup_nodes=nodes, decode_responses=True)
		querysplit = update.split()
		rc.execute_command(*querysplit)


#测试代码
if __name__ == '__main__':
	t = redis_library()
	#t.redis_update_cluster("get room_dj.dj_record.629294611",[{"host": "10.16.6.16", "port": "7000"}])
	rusult = t.redis_query("get user_relation_attentioncnt__1697827201028", redishost='60.205.59.6', redisport=6321, password='uxin001')
	#rusult = t.redis_query_cluster("get a",[{"host": "10.16.6.16", "port": "7000"}])
	print rusult
