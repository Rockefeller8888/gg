#python_redis
#redis是一个key_value存储系统,和Memcached类似,它支持的value类型相对很多,包括String(字符串)、list(链表)
#set(集合)、zset(sorted set --有序集合) hash(类型)。这些数据类型都支持push/pop、add/remove以及取并集和交集以及更丰富的操作
#这些操作都是原子性的,在此基础上,redis支持各种不同方式的的排序.与Memcached一样,为了保存效率,数据都是保存在内存中。
#区别的是redsi会周期性的把把更新的数据写入磁盘或者把修改操作写入追加的的记录文件,并且在此基础上实现了master-slave(主从同步)
#redis是一个高性能的key-value数据库。redis的出现很大补偿了memcached这类key-value的不足,在部分场合可以对关系型数据库起到很高的补充作用,
#它提供了python、Ruby、Erlang、PHP客户端,使用很方便，Redis支持主从同步。数据可以从主服务器向任意数量的从服务器同步,从服务器可以是关联其他从服务器的主服务器,
#这就让Redis可以执行单层树复制。从盘可以有意无意的对数据进行操作.由于完全实现了发布/订阅机制,使得从数据库在任何地方同步树时,
#可以订阅一个频道并接受主服务期完整的消息发布记录

#


