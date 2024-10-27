## Quick notes


### Setup
1. Setup oneAPI environment (follow https://github.com/intel/intel-xpu-backend-for-triton/tree/main?tab=readme-ov-file#quick-installation)
- https://dgpu-docs.intel.com/driver/client/overview.html#installing-client-gpus-on-ubuntu-desktop-22-04-lts
- https://www.intel.com/content/www/us/en/developer/articles/tool/pytorch-prerequisites-for-intel-gpu/2-5.html
2. Create python venv (this is tested with Python 3.10.12)
3. Pip install the xpu-requirements.txt (this includes prebuilts of https://github.com/intel/intel-xpu-backend-for-triton/tree/main)


### Run inference sample
1. In the Python venv, execute `python llama_3_1_8b_2x_faster_inference.py`