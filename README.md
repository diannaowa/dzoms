# dzoms
dzoms is a DevOps system with python
```python
*/5 * * * * python $WEBDIR/DZoms/monitorServer/businessMonitoring.py >/dev/null 2>&1
*/5 * * * * python $WEBDIR/DZoms/monitorServer/businessMonitorGraph.py >/dev/null 2>&1
```
