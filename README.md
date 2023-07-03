# PDS Helm chart

Initial Helm chart for deploying a [Personal Data Server](https://github.com/bluesky-social/pds) in Kubernetes.

## Current state

Only tested with minikube and consists of hard coded values added minimally to get the
Node app running. The **pds-auth** secret is not part of the chart.

To generate a **secp256k1** key, run:

```
$ ./scripts/generate-pds-key.sh
```

To generate a **hex 16 token**, run:

```
$ ./scripts/generate-hex16-token.sh
```

Then, you can use a key/token/string created by those scripts to create the **pds-auth**
secret by running:

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

After doing that, the pod will install (but not yet be operational) by running:

```
$ helm install <release name> chart/
```

## TODO:
- move persistent storage to bucket
- add example for ingress
