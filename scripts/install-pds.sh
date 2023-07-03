#!/bin/sh
##
## Disclaimer: only tested on MacOS with minikube
##

set -e

PDS_ADMIN_PW=$(./scripts/generate-hex16-token.sh)
PDS_JWT_SECRET=$(./scripts/generate-hex16-token.sh)
PDS_REPO_SIGNING_KEY=$(./scripts/generate-pds-key.sh)
PDS_ROTATION_KEY=$(./scripts/generate-pds-key.sh)

echo "Creating pds-auth secret..."
kubectl create secret generic pds-auth --from-literal=pds-admin-pw="$PDS_ADMIN_PW" \
  --from-literal=pds-jwt-secret="$PDS_JWT_SECRET" \
  --from-literal=pds-repo-signing-key="$PDS_REPO_SIGNING_KEY" \
  --from-literal=pds-plc-rotation-key="$PDS_ROTATION_KEY"

echo "Deploying postgres..."
./scripts/install-postgres.sh

echo "Waiting for postgres to be ready..." 
while [[ $(kubectl get pods postgresql-0 -o 'jsonpath={..status.conditions[?(@.type=="Ready")].status}') != "True" ]]; do echo "waiting for pod" && sleep 1; done

echo "Installing PDS..."
helm install pds chart
