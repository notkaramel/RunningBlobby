s.boot;
s.addr; // to reveal your `scsynth` server address

// Walking sound, specify xPosition and yPosition
// Range: -1 to 1
(
~walk = SynthDef(\walk, { | xPosition = 0, yPosition = 0 |
    var freq = 100, amp = 0.7;
    var rootOsc = SinOsc.ar(freq, 1, amp);

    // Envelope the sound
	var env = EnvGen.kr(Env.perc(0.03, 1), doneAction: Done.freeSelf);
	var sound = rootOsc * env;

	sound = Pan2.ar(sound*amp, xPosition, 1);
	Out.ar(0, sound);
}).add;
)

// Spin action sound
// Range of xPosition & yPositioin: -1 to 1
(
~spin = SynthDef("spin", { | xPosition = 0, yPosition = 0 |
	// Create the sound
	var freq = 400, amp = 1;
	var osc = SinOsc.ar(LFNoise0.kr(freq).range(freq, freq*2), Rand(0, 2*pi), amp);

    // Envelope the sound
	var leftEnv = EnvGen.kr(Env.perc(0.02, 0.5, 0.8, -3), doneAction: Done.freeSelf);
	var rightEnv = EnvGen.kr(Env.perc(0.02, 0.5, 0.8, -3), doneAction: Done.freeSelf);
	var sound = osc * leftEnv;

	sound = Pan2.ar(sound*amp, xPosition, 1);
	Out.ar(0, sound);
}).add;
)

// Character hits a wall
(
~wall = SynthDef("wall", { | xPosition = 0, yPosition = 0 |
    var freq = 400, amp = 1;
	var rootOsc = SinOsc.ar(LFNoise0.kr(freq).range(freq, freq*2), Rand(0, 2*pi), amp);

    // Envelope the sound
	var leftEnv = EnvGen.kr(Env.perc(0.02, 0.5, 0.8, -3), doneAction: Done.freeSelf);
	var rightEnv = EnvGen.kr(Env.perc(0.02, 0.5, 0.8, -3), doneAction: Done.freeSelf);
	var sound = rootOsc * leftEnv;

	sound = Pan2.ar(sound*amp, xPosition, 1);
	Out.ar(0, sound);
}).add;
)