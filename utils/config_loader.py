import yaml
from pathlib import Path

def load_config() -> dict:
    # Get the absolute path to the project root
    base_dir = Path(__file__).resolve().parent.parent  # go up 1 level from utils/
    config_path = base_dir / "config" / "config.yaml"  # build path to config.yaml

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found at {config_path}")

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    #print(config)  # For debugging
    return config


# # Test load
# if __name__ == "__main__":
#     load_config()