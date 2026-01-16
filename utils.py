import os
import logging
import json
from typing import Dict, List

def load_config(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse JSON: {e}")
        return {}

def write_config(file_path: str, config: Dict) -> None:
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        logging.error(f"Failed to write config: {e}")

def get_environment_variables() -> Dict:
    return dict(os.environ)

def filter_environment_variables(variables: List[str]) -> Dict:
    env_vars = get_environment_variables()
    return {var: env_vars[var] for var in variables if var in env_vars}

def main():
    config_file = "config.json"
    config = load_config(config_file)
    env_vars = filter_environment_variables(["DEVOPS_SCRIPTS_HOME", "DEVOPS_SCRIPTS_LOG_LEVEL"])
    print(json.dumps(env_vars, indent=4))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()