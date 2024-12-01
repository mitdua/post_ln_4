# 🏥 Intelligent Hospital Agent with OpenAI Swarm
![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📄 Description

This project implements an **Artificial Intelligence Agent** specifically designed for hospitals, using **SWARM - OpenAI**. Its primary goal is to enhance patient experience and optimize healthcare processes through an automated medical consultation system.

### Main Features:
1. **Triage Agent**: Welcomes patients, evaluates their initial needs, and directs them to the appropriate solution.
2. **Availability Agent**: Checks the availability of medical consultations and helps schedule appointments in real-time.
3. **Cancellation Agent** *(In Development)*: Allows patients to cancel previously scheduled appointments.
4. **Review Agent** *(In Development)*: Provides a summary of the patient’s scheduled consultations.

### Interaction Example:
- **User**: "I want to schedule a cardiology consultation for next Tuesday."
- **Agent**: "Perfect, we have availability on Tuesday at 10:00 AM. Would you like to confirm it?"

This project uses mocked data for testing and evaluation purposes with the **Swarm** tool.

---

## 🚀 Technologies Used

- **Python 3.12+**: Main programming language.
- **OpenAI GPT-4**: Language model for generating intelligent responses.
- **OpenAI Swarm**: Real-time orchestration of collaborative agents.

---

## 🛠️ Installation

### 📋 Prerequisites
- **Python 3.12+**

### 📦 Installation Steps

1. **Clone the repository**

    ```bash
    git clone https://github.com/mitdua/post_ln_4
    cd post_ln_4
    ```

2. **Create a virtual environment**

    ```bash
    python3.12 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables**

    Create a `.env` file in the project root and add the following variables:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run the application**

    ```bash
    python main.py
    ```

---

## 📅 Future Features

- Connection with a real hospital management system.
- Integration with patient databases and medical schedules.
- Implementation of an authentication system to ensure data security.
- Development of a graphical user interface (GUI) for easier access.

---

## 🎮 Usage

Interact with the chatbot by typing your messages in the **"user:"** field and observe the agent’s real-time responses.

---

## 📝 License

This project is licensed under the MIT License.
