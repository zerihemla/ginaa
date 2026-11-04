from generators.npc_generator import GeneratedNPC

# Placeholder for a future side quest generator.
# Run from the repo root with: python -m generators.side_quest_generator


if __name__ == "__main__":
    testNPC1 = GeneratedNPC()
    testNPC1.set_random_attributes(4)
    testNPC1.print_attributes()
