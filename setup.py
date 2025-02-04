# standard libraries
import io
import os
from typing import Dict, List

# external libraries
from setuptools import find_packages, setup

# Package meta-data.
NAME = "aidm"
DESCRIPTION = "AI Dungeon Master"
URL = "https://github.com/samvoisin/ai-dungeon-master"
EMAIL = "samvoisin@protonmail.com"
AUTHOR = "Sam Voisin"
REQUIRES_PYTHON = ">=3.12"
VERSION = "0.0.0"

# required packages
REQUIRED: List[str] = [
    "click",
    "llama-index",
    "tenacity",
    "tiktoken",
    "discord",
]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about: Dict[str, str] = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["test"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    entry_points="""
        [console_scripts]
        aidm=aidm._cli:cli
    """,
    install_requires=REQUIRED,
    include_package_data=True,
    license="GNU",
)
