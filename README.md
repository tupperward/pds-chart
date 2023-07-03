# PDS Helm chart

Initial Helm chart for deploying a [Personal Data Server](https://github.com/bluesky-social/pds) in Kubernetes.

## Current state

Only tested with minikube and consists of hard coded values added minimally to get the
Node app running. The **pds-auth** secret is not part of the chart. You would need to
create that secret but running:

```
$ kubectl create secret generic pds-auth --from-literal=pds-admin-pw=<hex 16 value> \
  --from-literal=pds-jwt-secret=<hex 16 value> \
  --from-literal=pds-repo-signing-key=<secp256k1 value> \
  --from-literal=pds-plc-rotation-key=<secp256k1 value>
```

To install a vanilla postgres with hardcoded `pds:pds` as user/pw, run:

```
$ ./scripts/install-postgres.sh
```

After doing that, with the current config the pod will run with just a:
`helm install <release name> chart/`

## TODO:
- move persistent storage to bucket
- add example for ingress
