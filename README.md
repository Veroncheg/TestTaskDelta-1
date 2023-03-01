## Installation steps:
1. `helm upgrade -f nginx-ingress-controller-values.yaml --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace`
2. `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
3. `helm repo update`
4. `helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack -f kube-prometheus-stack-values.yaml`
5. `kubectl apply -f randomhttpapp.yaml`
6. Get gohttpbench [https://github.com/parkghost/gohttpbench]
7. To create workload: `gohttpbench -c 1 -n 100000 -r http://mystack.local/randomhttp`

## Screenshots:
- ![Grafana screenshot](Grafana%20screenshot.png "Grafana screenshot")
- ![Grafana alerting](Grafana%20alerting.png "Grafana alerting")
- ![Grafana alert config](Grafana%20alert%20config.png "Grafana alert config")
