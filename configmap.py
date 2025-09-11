import yaml

class QuotedString(str):
    pass

def quoted_presenter(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')

yaml.add_representer(QuotedString, quoted_presenter)

# Input and output files
input_file = "example.env"
output_file = "output-config.yaml"

data = {}

# Read .env file
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):  # skip empty & comments
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")  # clean quotes
            data[key] = QuotedString(value)

# Build ConfigMap structure
configmap = {
    "apiVersion": "v1",
    "kind": "ConfigMap",
    "metadata": {
        "name": "my-config"  # <-- change name if needed
    },
    "data": data
}

# Save to YAML file
with open(output_file, "w") as f:
    yaml.dump(configmap, f, sort_keys=False, default_flow_style=False)

print(f"✅ ConfigMap YAML written to {output_file}")
