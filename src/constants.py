from pathlib import Path

# Get the absolute path to the project root directory
ROOT_FOLDER = Path(__file__).parent.parent.absolute()
SRC_FOLDER = ROOT_FOLDER / "src"

# Optional: Create additional path constants for common subdirectories
DATA_FOLDER = ROOT_FOLDER / "data"
MODELS_FOLDER = ROOT_FOLDER / "models"
CONFIGS_FOLDER = ROOT_FOLDER / "configs"
