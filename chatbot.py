def create_story(topic):
    stories = {
        "horse": f"""
Once upon a time, there was a beautiful horse named Thunder.

Thunder lived on a peaceful farm near a green forest. Every morning,
he ran across the fields and enjoyed the fresh air.

One day, Thunder noticed that a little bird had fallen from its nest.
He carefully helped the bird and stayed nearby until it was safe.

The bird was very happy and thanked Thunder for his kindness.

From that day, Thunder and the little bird became good friends.
Thunder learned that even a small act of kindness can make a big difference.

The End.
""",

        "lion": f"""
Once upon a time, a young lion lived in a beautiful jungle.

One day, he became lost while exploring the forest. Instead of being
afraid, he carefully followed the river and eventually found his way home.

His family was very happy to see him.

The lion learned that staying calm and thinking carefully can help
solve difficult problems.

The End.
""",

        "rabbit": f"""
Once upon a time, a clever rabbit lived near a beautiful garden.

One morning, the rabbit discovered a mysterious path leading into
the forest. Curious, he followed the path and found a peaceful pond.

He decided to share the beautiful place with his friends.

Everyone enjoyed the pond, and they thanked the rabbit for finding it.

The End.
"""
    }

    topic = topic.lower().strip()

    if topic in stories:
        return stories[topic]

    return f"""
Once upon a time, there was a village name dalipuram in dalipuram {topic} hasing more  than 20.

The {topic} daily eat fruits of  trees andalso some times steals food from the dalipuram villgers.


One day, the {topic} decided to steal bananas from a farm land of a villager. During the stealing suddenly one monkey made noise,
villager awake and also throw stones.

during that time so many {topic}  injured and returned home .

from then on  {topic} stooped to being greedy and stole things  from villagers they started new life without any disturbances.

The End.
"""


# Main program
print("===== STORY GENERATOR =====")

topic = input("Enter a topic or animal name: ")

story = create_story(topic)

print("\n===== YOUR STORY =====\n")
print(story)