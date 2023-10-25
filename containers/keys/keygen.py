import subprocess
import argparse
from kubernetes import client, config

def generate_ec_key():
    # Generate the OpenSSL EC key using the openssl command
    key_generation_command = "openssl ecparam -name secp256k1 -genkey -noout -outform DER | tail -c 38 | head -c 32 | xxd -p -c 32"
    key = subprocess.check_output(key_generation_command, shell=True, text=True)

    return key.strip()

def generate_hex_key():
    # Generate random data using the openssl command
    hex_data_generation_command = "openssl rand -hex 16"
    hex_data = subprocess.check_output(hex_data_generation_command, shell=True, text=True)
    
    return hex_data.strip()

def store_in_secret(secret_name, namespace, secret_data_name, values):
    # Configure the Kubernetes client
    config.load_incluster_config()
    api_instance = client.CoreV1Api()

    # Create or update the Secret in Kubernetes
    secret_data = {
        secret_data_name: values
    }
    metadata = client.V1ObjectMeta(name=secret_name)
    secret = client.V1Secret(metadata=metadata, data=secret_data)

    try:
        existing_secret = api_instance.read_namespaced_secret(secret_name, namespace)
        if secret_data_name in existing_secret.data:
            print(f"Data '{secret_data_name}' in Secret '{secret_name}' already exists. Skipping changes.")
        else:
            existing_secret.data[secret_data_name] = values
            api_instance.patch_namespaced_secret(secret_name, namespace, existing_secret)
            print(f"Data updated in Secret '{secret_name}' in namespace '{namespace}'.")
    except client.rest.ApiException as e:
        if e.status == 404:
            api_instance.create_namespaced_secret(namespace=namespace, body=secret)
            print(f"Data stored in new Secret '{secret_name}' in namespace '{namespace}'.")
        else:
            print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate OpenSSL EC key or random data and store it in a Kubernetes Secret.")
    parser.add_argument("--secret-name", required=True, help="Name of the Kubernetes Secret.")
    parser.add_argument("--namespace", required=True, help="Namespace in which to create/update the Secret.")
    parser.add_argument("--secret-data-name", required=True, help="Name of the secret data in the Secret.")
    parser.add_argument("--generate", required=True, choices=["ecparam", "hex"], help="Specify 'ecparam' for EC key generation or 'hex' for random data generation.")
    args = parser.parse_args()

    if args.generate == "ecparam":
        values = generate_ec_key()
    elif args.generate == "hex":
        values = generate_hex_key()
    
    store_in_secret(args.secret_name, args.namespace, args.secret_data_name, values)
