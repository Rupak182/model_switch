# AI Text Generation API With Model Selection

A FastAPI-based application for text generation using Hugging Face models with performance logging.

## Quick Setup

### Prerequisites
- Python 
- Hugging Face account and API token

### Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Create `.env` file** with your Hugging Face token:
   ```env
   HF_TOKEN=your_hugging_face_token_here
   ```
   Get your token from: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

3. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API**:
   - API: `http://localhost:8000`
   - Documentation: `http://localhost:8000/docs`

## Usage

### API Endpoint
- **GET** `/generate?prompt={text}&model={model_name}`

### Example
```bash
curl "http://127.0.0.1:8000/generate?prompt=what%20is%20LLM&model=Qwen/Qwen2.5-Coder-32B-Instruct"
```

### Important: Use Proper Hugging Face Model Names

Always use the format `username/model-name`:

- **Find models**: Visit [Hugging Face Model Hub](https://huggingface.co/models?pipeline_tag=text-generation) to browse available text generation  models
- **Terms & Conditions**: Some models require accepting terms before use. If you get tokenizer errors, accept the model's terms on Hugging Face and try again.


## Testing
```bash
pytest test_generate.py 
```
