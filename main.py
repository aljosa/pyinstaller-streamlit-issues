import sys
from streamlit import cli as stcli

if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        "hello.py",
        "--global.developmentMode=false",
        "--server.headless=true"
    ]
    sys.exit(stcli.main())
