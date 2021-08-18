# Exercise 1:
# prerequisite
* docker , kubernetes and kubectl must be installed.

1. `minikube start` to run minikube on docker driver as one node on k8s cluster
   `kubectl get nodes `
   `kubectl config view`
2.  `kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4` to create deployment service which include pod with the image k8s.gcr.io/echoserver:1.4    
    `kubectl get deployments` show the deployment service
    `kubectl get pods` show the pod service
    `kubectl expose deployment hello-node --type=LoadBalancer --port=8080` to expose the pod with the service LoadBalancer via port 8080
    `kubectl get services` show all services / instead of `kubectl get service -o wide`
    `minikube service hello-node --url` show the api ip to the pod 
   
The Screenshots in logs.txt file in thw project

   
# Exercise 2:
I took a little project (backend flask without read DB)
# prerequisite
* Be sure above is already installed and install python and then minikube is running.
* I tried to run the image local , but I got problem , so for now the image pull from my repo docker hub
* Install the missing packages by `pip install `

Ad Hoc commands :
* run `kubectl apply -f deployment.yaml -f service.yaml`

Declarative way :
* Run on cmd/teminal `helm install k8shelm k8s_backend_test --set image.test.tag="1"`.


* run `minikube service test-k8s-service --url`
* Put the URL result in file K8S_backend_testing.py line 5
* Test backend by running `python K8S_backend_testing.py`

* For stop minikube type `minikube delete` 

The Screenshots in ex2_logs.txt file in thw project


for CI/CD process installed jenkins 

type `java -jar jenkins.war`
for run the k8s need to set the docker hub , push the image from above to your repo docker hub
add new pipline job , choose the pipline script from SCM -> Git -> push 'https://github.com/hodayaYProject/sela_project.git'

