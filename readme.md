# LangChain ChatGPT Demo Project

## **Problem and Solution Description**

### **Problem**
In today's world, many people face challenges in accessing specific information, such as up-to-date weather conditions and news on topics of interest, without navigating through multiple websites and confusing interfaces. Additionally, many existing solutions do not offer efficient conversational interaction or support for complex queries.

### **Solution**
This project leverages the combination of the **LangChain** framework with OpenAI's **ChatGPT** model to create an intelligent agent that conversationally responds to queries about:
1. **Weather Forecasts**: Retrieves up-to-date weather conditions using the OpenWeather API.
2. **News**: Fetches the latest news on a topic using the NewsAPI.

The solution is implemented in an interactive web interface using **Streamlit**, allowing direct and intuitive user queries to the agent.

---

## **Tested Use Cases and Observed Results**

### **Use Cases**
1. **Weather Query:**
   - **Input:** "What is the weather in São Paulo?"
   - **Output:** "The weather in São Paulo is sunny with a temperature of 30°C."

2. **News Query:**
   - **Input:** "Show me news about artificial intelligence."
   - **Output:** "News: 'AI advancements are revolutionizing the industry' - 'Complete description of the news' (Source: 'News source')."

3. **Invalid Inputs:**
   - **Input:** "Weather in a non-existent city."
   - **Output:** "Unable to find weather information for the specified city."

4. **Out-of-Scope Queries:**
   - **Input:** "Explain this Python code."
   - **Output:** "This functionality is not supported at the moment."

### **Observed Results**
- The agent efficiently handled valid and invalid queries.
- The integration of the custom parser eliminated execution loops, ensuring robust and predictable behavior.

---

## **Execution Instructions**

### **Prerequisites**
1. Python 3.8 or higher.
2. Install the dependencies listed in the `requirements.txt` file.

### **Steps to Execute the Project**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <directory-name>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the API keys in the `src/utils/api_keys.py` file:
   ```python
   WEATHER_API_KEY = "your_openweather_api_key"
   NEWS_API_KEY = "your_newsapi_key"
   OPENAI_API_KEY = "your_openai_api_key"
   ```
5. Run Streamlit:
   ```bash
   streamlit run app.py
   ```
6. Access the application in your browser at: `http://localhost:8501`.

---

## **Reflection on the Project**

### **Ease Provided by the Agent**
- **Automation and Centralization:** The agent combines two external APIs into a single interface, avoiding the need for users to manually visit multiple websites.
- **Interactivity:** The conversational interface offers a more natural and intuitive way to retrieve information.
- **Scalability:** The integration with LangChain and ChatGPT allows adding new features (tools or APIs) without significant changes to the architecture.

### **Comparison with Manual Approach**
| **Task**                | **Manual**                              | **With Agent**                      |
|-------------------------|------------------------------------------|--------------------------------------|
| Querying weather        | Visit OpenWeather's website             | "What is the weather in São Paulo?" |
| Searching for news      | Search on Google or visit news portals  | "Show me news about AI."           |
| Natural interaction     | Not available                           | Fluid and contextual conversation.  |

The agent proved to be an efficient and practical solution for centralizing information in an accessible format.

---
## **Future Improvements**
1. Add more tools, such as integration with financial or public transport APIs.
2. Implement support for more advanced natural language processing (e.g., text summarization).
3. Create a feedback system to improve the agent's responses based on real-world usage.

---

With these updates, the project meets the proposed requirements and offers a functional, robust, and scalable solution. 😊
