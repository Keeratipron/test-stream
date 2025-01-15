import json
import yaml
from pathlib import Path

def convert_json_to_yaml(json_file_path: str, yaml_file_path: str) -> None:
    try:
        # Validate JSON file path
        json_path = Path(json_file_path)
        if not json_path.is_file():
            raise FileNotFoundError(f"The file {json_file_path} does not exist.")
        
        # Read the JSON data
        with json_path.open('r', encoding='utf-8') as json_file:
            try:
                json_data = json.load(json_file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON format in {json_file_path}: {e}")
        
        # Convert and write to YAML
        yaml_path = Path(yaml_file_path)
        with yaml_path.open('w', encoding='utf-8') as yaml_file:
            yaml.dump(json_data, yaml_file, default_flow_style=False, sort_keys=False)

        print(f"Successfully converted {json_file_path} to {yaml_file_path}")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except ValueError as e:
        print(f"JSON Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# # Example usage
# if __name__ == "__main__":
#     # Update the file paths as needed
#     input_json = "users.json"
#     output_yaml = "data.yaml"
#     convert_json_to_yaml(input_json, output_yaml)