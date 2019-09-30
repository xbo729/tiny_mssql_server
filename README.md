# tiny_mssql_server
## 针对于docker 安装sql server 要求内存大于2g的用户 适用的脚本											
参考了https://www.cnblogs.com/biaogejiushibiao/p/9280841.html <br/> 															
麦齐的Microsoft SQL Server on Linux破解 2G内存限制方法	<br/>																	
特别制作了Dockerfile 来破解docker 版本的sql server（要求内存大于2G要求）<br/>							
步骤:<br/>					
1、 docker build -t linux-sqlserver .	<br/>					
2、docker run -v /opt/docker/mssql:/var/opt/mssql -v /etc/localtime:/etc/localtime:ro -e TZ="Asia/Shanghai" -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=P@ssw0rd' -p 1433:1433 -d --name sqlserver linux-sqlserver <br/>						
