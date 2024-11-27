#!/usr/bin/env sclang
// -- THIS FILE IS FOR DEMO ONLY --
// This file is executable from the terminal. 

s = Server("SuperCollider", NetAddr("127.0.0.1", 57110));
s.boot;
s.addr;

SynthDef(\walk, { | xPosition = 0, yPosition = 0 |
    var freq = 100, amp = 0.7;
    var sound = SinOsc.ar(freq, 1, amp);
    var out = sound * EnvGen.kr(Env.perc(0.3 * yPosition, 1), doneAction: Done.freeSelf);
	Out.ar(0, Pan2.ar(out, xPosition, 1));
}).load(s);

SynthDef("spin", { | xPosition = 0, yPosition = 0 |
	var freq = 400, amp = 1;
	var sound = SinOsc.ar(LFNoise0.kr(freq).range(freq, freq*2), Rand(0, 2*pi), amp);
	var out = sound * EnvGen.kr(Env.perc(0.02, 0.5 * yPosition, 0.8, -3), doneAction: Done.freeSelf);
	Out.ar(0, Pan2.ar(out, xPosition, 1));
}).load(s);

SynthDef("wall", { | xPosition = 0, yPosition = 0 |
    var freq = 400, amp = 1;
	var sound = SinOsc.ar(LFNoise0.kr(freq).range(freq, freq*2), Rand(0, 2*pi), amp);
	var out = sound * EnvGen.kr(Env.perc(0.8 * yPosition, 0.5, 0.8, -3), doneAction: Done.freeSelf);
	Out.ar(0, Pan2.ar(out, xPosition, 1));
}).load(s);