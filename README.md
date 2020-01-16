# zabbix-java-1.8-template


### 自动发现主机上运行的java程序，并监控程序的cpu、内存、线程数、gc等信息

> Centos 7

> Jdk 1.8

> Python 2.7

注意事项：
1. 脚本使用了jps和jstat两个jdk自带的命令，需要设置软连接
```sh
ln -s /home/jdk1.8.0_171/bin/jps /usr/bin/jps
ln -s /home/jdk1.8.0_171/bin/jstat /usr/bin/jstat

```
2. zabbix 客户端需要用root用户运行
3. 需要在主机创建路径,将jps.py拷贝到给路径下
```sh
mkdir /etc/zabbix/tools/
# 给脚本执行权限
chmod +x jps.py
```
4. 将userparameter_jps.conf拷贝到/etc/zabbix/zabbix_agentd.d路径下
