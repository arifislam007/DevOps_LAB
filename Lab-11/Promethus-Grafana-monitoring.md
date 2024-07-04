# This LAB is for Promethus and Graphana on kubernetes cluster to monitor Kubernetes Cluster in Different angle
# Assume that you have a Kubernetes cluster up and running with kubectl setup
## This LAB has two part
- Promethus
- Graphana

## Promethus Part
**Prometheus is a highly scalable, open-source monitoring framework that offers built-in monitoring capabilities for the Kubernetes container orchestration platform. In the field of observability, it is becoming increasingly popular due to its effective metrics and alerting features.**

## Key Point of Promethus
- **Metric Collection**: Prometheus uses the pull model to retrieve metrics over HTTP. There is an option to push metrics to Prometheus using Pushgateway for use cases where Prometheus cannot Scrape the metrics. One such example is collecting custom metrics from short-lived kubernetes jobs & Cronjobs
- **Metric Endpoint**: The systems that you want to monitor using Prometheus should expose the metrics on an /metrics endpoint. Prometheus uses this endpoint to pull the metrics in regular intervals.
- **PromQL**: Prometheus comes with PromQL, a very flexible query language that can be used to query the metrics in the Prometheus dashboard. Also, the PromQL query will be used by Prometheus UI and Grafana to visualize metrics.
- **Prometheus Exporters**: Exporters are libraries that convert existing metrics from third-party apps to Prometheus metrics format. There are many official and community Prometheus exporters. One example is, the Prometheus node exporter. It exposes all Linux system-level metrics in Prometheus format.
- **TSDB (time-series database)**: Prometheus uses TSDB for storing all the data efficiently. By default, all the data gets stored locally. However, to avoid a single point of failure, there are options to integrate remote storage for Prometheus TSDB.

## Prometheus Architecture
![image](https://github.com/arifislam007/DevOps_LAB/assets/32135229/6f7ce82f-8168-4526-959e-41760605144d)

# Lets deploy Promethus on Kubernetes Cluste 
Clone the following github repository. This repo has all necessary file that you need to deploy Promethus.
This deployment use namespace as monitoring.
- Create a namespace named monitoring
  ``` bash
  kubectl create namespace monitoring
  ```
  
  ```bash
  git clone https://github.com/techiescamp/kubernetes-prometheus

  kubectl apply -f kubernetes-prometheus
  ```

