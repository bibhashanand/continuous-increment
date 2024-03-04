# Readme

The port on which the app listen is 3000

```bash
kubectl get nodes -o wide

kubectl get service my-incrementing-app-service

kubectl scale deployment my-incrementing-app --replicas=1
```

```bash
gunicorn -w 3 -b 0.0.0.0:3000 server:app
```
