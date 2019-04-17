## Copy file swap-monitor.sh to /usr/bin/
sudo cp swap-monitor.sh /usr/bin/

## Copy file swap-monitor.service to /etc/systemd/system/
sudo cp swap-monitor.service /usr/lib/systemd/system/

## Copy file swap-monitor.8.gz to your man path
sudo cp swap-monitor.8.gz /usr/share/man/man8

## Start the service
systemctl daemon-reload
systemctl start swap-monitor

## CHECK
### Check status service
systemctl status swap-monitor

### Check status in log file in ~/swap-monitor.log
cat ~/swap-monitor.log

### Check service system process
pstree |grep swap
ps -e |grep swap

### Check USR1 signal. PID take from ps -e |grep swap
kill -USR1 [PID of swap-monitor]

## Check man page
man swap-monitor
