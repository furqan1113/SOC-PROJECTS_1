# Basic VPN Log Investigation with Splunk

## Objective

This project was created to practice basic Splunk and SPL skills by investigating VPN log data.

## Tools Used

* Splunk
* SPL
* VPN log dataset

---

# Investigation

## 1. How many events are present in the log file?

### SPL Query

```spl
index="vpn_inv-logs"
| stats count
```

### Result

**2,862 events**

### What I Found

The VPN log dataset contains a total of **2,862 events** available for investigation.

![q1](./ss/q1-splunk.png)

## 2. How many log events are captured by the user Maleena?

### SPL Query

```spl
index="vpn_inv-logs"
| spath
| search UserName="Maleena"
| stats count
```

### Result

**60 events**

### What I Found

The user `Maleena` was associated with **60 VPN log events** in the dataset.

![q2](./ss/q2-splunk.png)

## 3. What is the username associated with IP 107.14.182.38?

### SPL Query

```spl
index="vpn_inv-logs"
| spath
| search Source_ip="107.14.182.38"
| stats values(UserName) as Username
```

### Result

**Smith**

### What I Found

The IP address `107.14.182.38` was associated with the username **Smith**.

![q3](./ss/q3-splunk.png)

## 4. What is the number of events that originated from all countries except France?

### SPL Query

```spl
index="vpn_inv-logs"
| spath
| search Source_Country!="France"
| stats count
```

### Result

**2,814 events**

### What I Found

There were **2,814 VPN log events** originating from countries other than France.

![q4](./ss/q4-splunk.png)

## 5. How many VPN events were associated with the IP 107.3.206.58?

### SPL Query

```spl
index="vpn_inv-logs"
| spath
| search Source_ip="107.3.206.58"
| stats count
```

### Result

**14 events**

### What I Found

The IP address `107.3.206.58` was associated with **14 VPN log events** in the dataset.

![q5](./ss/q5-splunk.png)

---

## Investigation Summary

This investigation used basic Splunk SPL commands to examine VPN log activity.

The dataset contained **2,862 events**. I investigated activity associated with specific users, source IP addresses, and countries using field-based searches and aggregation.

This project helped me build a basic understanding of how SOC analysts can use SIEM logs to investigate and understand security log activity.

## Note

This is a learning project I made while studying SOC Level 1. The main purpose of this project is to practice what I learn and get better at investigating and documenting security logs.
