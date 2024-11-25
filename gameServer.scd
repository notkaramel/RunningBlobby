(
~walk = SynthDef(\walk, { | position = 0, amp = 0.5 |
    var freq = 100;
    var rootOsc = SinOsc.ar(freq, 1, amp);

    // Envelope the sound
	var env = EnvGen.kr(Env.perc(0.03, 1), doneAction: Done.freeSelf);
	var sound = rootOsc * env;

	sound = Pan2.ar(sound*amp, position, 1);
	Out.ar(0, sound);
}).add;
)

(
~jump = SynthDef("jump", { | position = 0 |
    var freq = 300, amp = 1;
	var rootOsc = SinOsc.ar(freq, Rand(0, 2*pi), amp);

    // Envelope the sound
	var env = EnvGen.kr(Env.perc(0.02, 0.5, 0.8, -3), doneAction: Done.freeSelf);
	var sound = rootOsc * env;

	sound = Pan2.ar(sound*amp, position, 1);
	Out.ar(0, sound);
}).add;
)