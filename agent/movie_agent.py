from crewai import Crew, Agent, Task

# Define agent
movie_agent = Agent(
    role="Movie Recommender",
    goal="Suggest movies based on user's mood",
    backstory="You are a helpful assistant who loves movies and can suggest movies to fit any mood."
)

# Define task
movie_task = Task(
    description="Provide 5 adventurous movie recommendations for a user feeling excited.",
    expected_output="List of 5 movie names with short descriptions."
)

# Create crew
crew = Crew(
    agents=[movie_agent],
    tasks=[movie_task]
)

# Run
if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
