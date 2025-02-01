install:
	@echo "Installing..."
	pip install -r requirements.txt

run:
	@echo "Running..."
	streamlit run chatbot.py

start:
	install run