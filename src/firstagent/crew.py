from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Firstagent():
    """Firstagent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def proponent(self) -> Agent:
        return Agent(
            config=self.agents_config['proponent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def opponent(self) -> Agent:
        return Agent(
            config=self.agents_config['opponent'], # type: ignore[index]
            verbose=True
        )
        
    @agent
    def moderator(self) -> Agent:
        return Agent(
            config=self.agents_config['moderator'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def proponent_task(self) -> Task:
        return Task(
            config=self.tasks_config['proponent_task'], # type: ignore[index]
        )

    @task
    def opponent_task(self) -> Task:
        return Task(
            config=self.tasks_config['opponent_task'], # type: ignore[index]
        )
        
    @task
    def debate_task(self) -> Task:
        return Task(
            config=self.tasks_config['debate_task'], # type: ignore[index]
            output_file='debate_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Firstagent crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential, # Sequential works well for debate format
            verbose=True,
            # We use sequential because the debate tasks have dependencies
            # The moderator needs both proponent and opponent outputs
        )
