# dzoms
dzoms is a DevOps system with python
```python
*/5 * * * * python $WEBDIR/DZoms/monitorServer/businessMonitoring.py >/dev/null 2>&1
*/5 * * * * python $WEBDIR/DZoms/monitorServer/businessMonitorGraph.py >/dev/null 2>&1
```

#Do a simple test

```
docker run -d -p 8000:80 --name dzoms duizhang/python:dzoms
```
