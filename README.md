# Zoo Simulator

# The Test
Write a simple Zoo simulator which contains 3 different types of animal
* Monkey
* Giraffe
* Elephant

The zoo should open with 5 of each type of animal. Each animal has a health value held as a percentage (100% is completely healthy).

Every animal starts at 100% health. This value should be a floating point value.
The application should act as a simulator, with time passing at the rate of 1 hour
with each interation. Every hour that passes, a random value between 0 and 20 is to be
generated for each animal. This value should be passed to the appropriate animal, whose
health is then reduced by that percentage of their current health.

The user must be able to feed the animals in the zoo. When this happens, the zoo
should generate three random values between 10 and 25; one for each type of animal. The
health of the respective animals is to be increased by the specified percentage of their
current health. Health should be capped at 100%.

When an Elephant has a health below 70% it cannot walk. If its health does not
return above 70% once the subsequent hour has elapsed, it is pronounced dead.
When a Monkey has a health below 30%, or a Giraffe below 50%, it is pronounced
dead straight away.

The user interface should show the current status of each Animal and contain two
buttons, one to provoke an hour of time to pass and another to feed the zoo. The UI should
update to reflect each change in state, and the current time at the zoo.

# To Install

```bash
git clone https://github.com/bgr-github/zoo-simulator
cd zoo-simulator
python zoosimulator.py
```
