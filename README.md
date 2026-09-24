# ENV to Kubernetes ConfigMap Converter

A simple Python utility that converts `.env` files into Kubernetes ConfigMap YAML format with properly quoted string values.

## Features

- Converts `.env` files to Kubernetes ConfigMap YAML
- Automatically quotes all values for consistent string handling
- Skips comments and empty lines
- Clean, readable YAML output

## Requirements

- Python 3.6+
- PyYAML

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ujjawaldevops/env-to-k8s-configmap.git
cd env-to-k8s-configmap
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your environment variables in `example.env` file:
```env
PORT=3000
NODE_ENV=production
API_KEY=your-api-key
DB_HOST=localhost
```

2. Run the converter:
```bash
python configmap.py
```

3. The generated ConfigMap will be saved as `output-config.yaml`:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
  PORT: "3000"
  NODE_ENV: "production"
  API_KEY: "your-api-key"
  DB_HOST: "localhost"
```

## Customization

- **ConfigMap name**: Edit the `name` field in the `metadata` section of `configmap.py`
- **Input file**: Change the `input_file` variable in `configmap.py`
- **Output file**: Change the `output_file` variable in `configmap.py`

## File Structure

```
.
├── configmap.py          # Main conversion script
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## License

MIT License - feel free to use and modify as needed.