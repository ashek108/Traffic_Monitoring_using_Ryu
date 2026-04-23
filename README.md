# Network Traffic Observability with Ryu & Mininet

## Description

This repository provides an implementation of an SDN-based network management application leveraging Ryu framework to track data flows across the network and extract flow-level telemetry.

## Capabilities

- Real-time packet tracking
- Network flow metrics and statistics aggregation
- Data flow recording and archiving
- Throughput and latency assessment with iperf

## Visualization

Includes a live traffic visualization tool with real-time interactive charts for monitoring network activity and packet statistics.

## Installation & Execution

```bash
ryu-manager traffic_monitor.py
sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6653 --switch ovs,protocols=OpenFlow13
```
