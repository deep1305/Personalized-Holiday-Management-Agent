from autogen_agentchat.messages import TextMessage
from Personalized_Holiday_Management.teams.holiday_team import holiday_team
import asyncio

async def main():
    task = TextMessage(
        content=(
            "Suggest 3 destination options for a June trip with these constraints: "
            "10 days, family of 4, total budget CAD 6000, and preference for places "
            "with both mountains and sea nearby. For each option include: best area to stay, "
            "high-level day-wise itinerary, budget split (stay/food/local transport/activities), "
            "and practical travel tips."
        ),
        source="user",
    )
    response = await holiday_team.run(task=task)
    for message in response.messages:
        print(f"{message.source}: {message.content}")

if __name__ == "__main__":
    asyncio.run(main())