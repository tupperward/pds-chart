# PDS Helm chart

Initial Helm chart for deploying a [Personal Data Server](https://github.com/bluesky-social/pds) in Kubernetes.

## Deploy PDS to local dev (tested in minikube)

```
$ ./scripts/install-pds.sh
```

## Current state

Only tested with minikube. Consists of hard coded values added minimally to get the
Node app running. The **pds-auth** secret is not part of the chart, it's created
by generating values with:

**secp256k1**:

```
$ ./scripts/generate-pds-key.sh
```

**hex 16 token**:

```
$ ./scripts/generate-hex16-token.sh
```

A vanilla postgres with hardcoded `pds:pds` is deployed with:

```
$ ./scripts/install-postgres.sh
```

After doing that, the pod is deployed via:

```
$ helm install <release name> chart/
```

All of this is wrapped in the `install-pds.sh` script.

**BUT IT HAS NOT YET BEEN CONFIRMED OPERATIONAL**

## TODO:
- move persistent storage to bucket
- add example for ingress
