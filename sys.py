import sys

# Based on these checks, it prints whether the virtual environment is active or not
if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("Venv is active")
else:
    print("Venv is not active")
