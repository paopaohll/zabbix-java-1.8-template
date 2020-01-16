# zabbix-java-1.8-template

### 自动发现主机上运行的java程序，并监控程序的cpu、内存、线程数、gc等信息

注意事项：
1. 脚本使用了jps和jstat两个jdk自带的命令，需要设置软连接
```sh
ln -s /home/jdk1.8.0_171/bin/jps /usr/bin/jps
ln -s /home/jdk1.8.0_171/bin/jstat /usr/bin/jstat

```
2. zabbix 客户端需要用root用户运行
