# CrewAI Debate Framework

Welcome to the CrewAI Debate Framework, a specialized multi-agent system powered by [crewAI](https://crewai.com). This project enables AI agents to present contrasting perspectives on a topic and synthesize insights from opposing viewpoints.

🎥 [![Download CrewAI Debate Agents Video](https://img.shields.io/badge/Download-Video-blue)](https://github.com/brettenf-UW/firstagent/raw/main/CrewAI%20Debate%20Agents.mp4)

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
crewai install
```

### Configuration

This project is already configured to use Google's Gemini model with your free API key.

## Agent Structure

The framework consists of three specialized agents:

1. **Proponent Agent**
   - Role: Topic Advocate
   - Goal: Present compelling evidence supporting the benefits of the topic
   - Approach: Optimistic but factual, evidence-based arguments

2. **Opponent Agent**
   - Role: Topic Critic
   - Goal: Identify potential concerns and counterarguments
   - Approach: Balanced, evidence-based critiques avoiding alarmism

3. **Moderator Agent**
   - Role: Debate Facilitator
   - Goal: Synthesize insights from both perspectives
   - Approach: Impartial analysis identifying common ground and key differences

## Task Workflow

The debate follows a sequential process:

1. **Proponent Task**: Presents arguments in favor of the topic
2. **Opponent Task**: Presents counterarguments and concerns
3. **Debate Task**: Synthesizes insights from both perspectives

## Running the Project

To run a debate on your chosen topic:

1. Modify the input parameters in `src/firstagent/main.py`:
   ```python
   inputs = {
       'topic': 'Your Topic Here',
       'current_year': str(datetime.now().year)
   }
   ```

2. Start the debate from the project root:
   ```bash
   python -m firstagent.main
   ```

The output will be saved as `debate_report.md`, containing a structured analysis from multiple perspectives.

## Customizing

- Modify `src/firstagent/config/agents.yaml` to adjust agent personalities and roles
- Modify `src/firstagent/config/tasks.yaml` to change the debate format
- Modify `src/firstagent/crew.py` to add custom tools or logic
- Modify `src/firstagent/main.py` to change input parameters

## Support

For support, questions, or feedback:
- Visit the [crewAI documentation](https://docs.crewai.com)
- Reach out through the [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join the Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with the docs](https://chatg.pt/DWjSBZn)
