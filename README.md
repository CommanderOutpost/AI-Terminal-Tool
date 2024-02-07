# AI-Terminal-Tool
An AI tool that allows the use of natural text in terminal. It essentially translates your natural language into terminal commands. 

## Installation
1. Clone the repository
```
git clone https://github.com/CommanderOutpost/AI-Terminal-Tool.git
```
2. Go in the project folder and create a file named .env
```
cd AI-Terminal-Tool
nano .env
```
3. Copy the following below and fill it with the correct info
```
model=gpt-4
OPENAI_API_KEY=sk-************************************************
```
4. Execute the install.sh file (Make sure you are in the directory before executing it)
```
bash install.sh
```
5. Done! Enjoy aife!

## Usage
Below are examples of aife in use.
* Simple things like creating a file
  ```
  aife "create a file called sunday"
  AI Command:  touch sunday 
  Terminal Output:  Command 'touch sunday' executed successfully.
  Command 'touch sunday' executed successfully.
  ```
  
  ```
  aife "创建一个名为 杨钰莹 的文件"
  AI Command:  mkdir 杨钰莹 
  Terminal Output:  Command 'mkdir 杨钰莹' executed successfully.
  Command 'mkdir 杨钰莹' executed successfully.
  ```
  
  ```
  aife "Maak een bestand met de naam Amay"
  AI Command:  touch Amay 
  Terminal Output:  Command 'touch Amay' executed successfully.
  Command 'touch Amay' executed successfully.
  ```
* More useful things like
