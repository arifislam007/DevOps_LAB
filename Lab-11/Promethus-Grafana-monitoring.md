# This LAB is for Promethus and Graphana on kubernetes cluster to monitor Kubernetes Cluster in Different angle
# Assume that you have a Kubernetes cluster up and running with kubectl setup
## This LAB has two part
- Promethus Server
- Kube State Metrics
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

## Kube State Metrics
Kube State Metrics is a service that interacts with the Kubernetes API server to gather detailed information about all API objects such as deployments, pods, daemonsets, and statefulsets. It primarily produces metrics in Prometheus format, maintaining the same stability as the Kubernetes API. This service provides metrics for Kubernetes objects and resources that are not directly available from native Kubernetes monitoring components.

- Node status, node capacity (CPU and memory)
- Replica-set compliance (desired/available/unavailable/updated status of replicas per deployment)
- Pod status (waiting, running, ready, etc)
- Ingress metrics
- PV, PVC metrics
- Daemonset & Statefulset metrics.
- esource requests and limits.
- Job & Cronjob metrics
  
Step 1: Clone the Github repo
```bash
git clone https://github.com/devopscube/kube-state-metrics-configs.git
kubectl apply -f kube-state-metrics-configs/
kubectl get deployments kube-state-metrics -n kube-system
```

**Need to confirm that the  following part is in the promethus config part** 
```bash
- job_name: 'kube-state-metrics'
  static_configs:
    - targets: ['kube-state-metrics.kube-system.svc.cluster.local:8080']
```

# Grafana part
Grafana is an open-source lightweight dashboard tool. It can be integrated with many data sources like Prometheus, AWS cloud watch, Stackdriver, etc. Running Grafana on Kubernetes

### Clone Grafana Git repository 

```bash
git clone https://github.com/bibinwilson/kubernetes-grafana.git
kubernetes apply -f kubernetes-grafana/

```

