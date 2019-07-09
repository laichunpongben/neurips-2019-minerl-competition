from pathlib import Path

import minerl

from config import DATA_FOLDER

path = Path(DATA_FOLDER)

path.mkdir(parents=True, exist_ok=True)

minerl.data.download(directory=path)
