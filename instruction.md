#copy file swap-monitor.sh to /usr/bin/
sudo cp swap-monitor.sh /usr/bin/

#copy file swap-monitor.service to /etc/systemd/system/
sudo cp swap-monitor.service /etc/systemd/system/

#copy file swap-monitor.8.gz to /
##See manpath
manpath
##copy to your man path
sudo cp swap-monitor.8.gz /usr/share/man/man8
##try to use man page
man swap-monitor

#start the service
systemctl daemon-reload
systemctl start swap-monitor

#CHECK
##check status service
systemctl status swap-monitor

##check status in log file in ~/swap-monitor.log
cat ~/swap-monitor.log

#check service system process
pstree |grep swap
ps -e |grep swap

#check USR1 signal. PID take from ps -e |grep swap
kill -USR1 [PID of swap-monitor]


