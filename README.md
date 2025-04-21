# MedHelp- A Medcal Chatbot

### STEPS TO RUN THE CHATBOT

### Create a conda environment and activate it
conda create -n medhelp python=3.11 -y
<br>
conda activate medhelp

### Install the requirements
pip install -r requirements.txt

### Create `.env` file in the root directory
### Get pinecone api key from pinecone.io and create an index to get pinecone api environment
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 
<br>
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

### Download model from the following link and keep the model in the model directory:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
<br>
Model Name: llama-2-7b-chat.ggmlv3.q4_0.bin

### Download the medical book (Gale encyclopedia of medicine) from the following drive link and keep this in data folder
https://drive.google.com/file/d/1gnDEXtaA3V1DA0s9NTvI9z-vzpiSOPQQ/view?usp=sharing

# run the following command
python store_index.py

# Finally run the following command
python app.py

# open up localhost

### Techstack Used:
- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone

### Group details:
Group: 08 <br>
Member 01: Shoumik Sarkar
ID: 2211320042
Email: shoumik.sarkar@northsouth.edu

Member 02: Anik Barua
ID: 2211155642
Email: anik.barua01@northsouth.edu

Member 03: Md. Shefatullah Bin Sadik
ID: 2222538642
Email: shefatullah.sadik@northsouth.edu
