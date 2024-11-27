s.boot;
s.addr; // to reveal your `scsynth` server address

// ------------ SYNTH DEFS ------------

// Walking sound, specify xPosition and yPosition
// Range: -1 to 1
(
~walk = SynthDef(\walk, { | xPosition = 0, yPosition = 0 |
	// TODO: Implement a sound that changes based on the character's position
	// HINT:
	// - Step 1: create a sound (e.g., SinOsc.ar)
	// - Step 2: EnvGen.kr to envelope the sound, remember to free the synth with `doneAction: Done.freeSelf`
	// - Step 3: Use Pan2.ar to pan the sound between the left and right speakers
	// - Step 4: Use Out.ar to send the sound to the speakers
	// - Step 5: Be creative!!
}).add;
)

// Spin action sound
// Range of xPosition & yPositioin: -1 to 1
(
~spin = SynthDef("spin", { | xPosition = 0, yPosition = 0 |
	// TODO: Implement a sound that changes based on the character's position
	// HINT:
	// - Step 1: create a sound (e.g., SinOsc.ar)
	// - Step 2: EnvGen.kr to envelope the sound, remember to free the synth with `doneAction: Done.freeSelf`
	// - Step 3: Use Pan2.ar to pan the sound between the left and right speakers
	// - Step 4: Use Out.ar to send the sound to the speakers
	// - Step 5: Be creative!!
}).add;
)

// Character hits a wall
(
~wall = SynthDef("wall", { | xPosition = 0, yPosition = 0 |
	// TODO: Implement a sound that changes based on the character's position
	// HINT:
	// - Step 1: create a sound (e.g., SinOsc.ar)
	// - Step 2: EnvGen.kr to envelope the sound, remember to free the synth with `doneAction: Done.freeSelf`
	// - Step 3: Use Pan2.ar to pan the sound between the left and right speakers
	// - Step 4: Use Out.ar to send the sound to the speakers
	// - Step 5: Be creative!!
}).add;
)