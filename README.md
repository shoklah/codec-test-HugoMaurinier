# codec-test-HugoMaurinier
 
Coding Test for Codec
## How to run the project
pip install -r requirements.txt
python3 pilot.py "MAP_WIDTHxMAP_HEIGHT" "COMMAND"

COMMAND is a string of characters that represent the commands to be executed by the robot. The robot will execute the commands in the order they are given :
- F : Move forward
- L : Turn left
- R : Turn right


## How to run the tests
python3 -m pytest tests