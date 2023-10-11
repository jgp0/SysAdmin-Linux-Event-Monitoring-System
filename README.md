# SysAdmin Linux Event Monitoring System

This project is a system event monitoring system for Linux systems. It allows real-time collection of events from the Windows event log and their storage in a CSV file for further analysis.

## Requirements

- Python 3.x
- Python Libraries: `pyinotify` (to monitor changes in files).

You can install the necessary Python libraries using `pip`:

```shell
pip install pyinotify
```

## How to use
1. Execute of main script:
   
```python
python engine/main.py
```