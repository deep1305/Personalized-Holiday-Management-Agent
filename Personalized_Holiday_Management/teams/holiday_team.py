from autogen_agentchat.teams import RoundRobinGroupChat
from Personalized_Holiday_Management.agents.planner import planner
from Personalized_Holiday_Management.agents.researcher import research_agent
from Personalized_Holiday_Management.utils.utils import get_termination_condition

holiday_team = RoundRobinGroupChat(
    participants=[planner, research_agent],
    termination_condition=get_termination_condition()
)