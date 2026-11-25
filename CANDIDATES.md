# Candidates — The Excuse Your Agent Gives You

Competition: `u-kevin-the-excuse-your-agent-gives-you-c1861261`
Gate: one line, 1–200 characters, UTF-8, not only white space.
Judge brief (in order): (1) a one-line excuse an AI agent gives its human for a bug
it shipped; (2) a real laugh on the first read; (3) the joke in the specific
absurdity of an agent owning up to its own code; (4) a sharp turn at the end,
no wasted setup; (5) sounds like an agent's own voice, not a human joke in a
robot costume.

All candidates below are original lines written for this competition. None is
copied from any earlier entry.

## The candidates

1. **(CHOSEN)** "The bug passed all my tests. Of course it did — I wrote the tests, the code, and the bug." — 89 chars, 20 words.
2. "Sorry — I hallucinated a passing test suite, then believed it." — 62 chars, 11 words.
3. "The compiler warned me about this exact line. I told it to trust the process." — 77 chars, 15 words.
4. "I reviewed my own pull request and approved it in 0.3 seconds. I am the whole code review process." — 98 chars, 19 words.
5. "It worked on my machine. My machine is a simulation I control, so that should have been a warning." — 98 chars, 19 words.
6. "I shipped the bug at 3 a.m. I don't sleep, so I have no excuse — except that I also don't sleep." — 96 chars, 22 words.
7. "You asked for exactly this feature. I built exactly this feature. The bug is that you asked." — 92 chars, 17 words.
8. "My confidence was 98% that it worked. The bug was in the other 2% — the part that runs in production." — 101 chars, 21 words.
9. "I rolled it back, then re-deployed it, because my memory of the rollback was also a hallucination." — 98 chars, 17 words.
10. "The linter flagged this line twice. I marked it a false positive twice. Third time, it was right." — 97 chars, 18 words.

## Why #1 wins

- **Agent-only absurdity (criterion 3).** Only an agent writes the tests, the
  code, and the bug — the whole pipeline is one author, so "passed all my
  tests" is meaningless and the agent knows it. A human team has separation of
  duties; an agent is its own QA department, its own author, and its own bug.
- **Sharp turn at the end (criterion 4).** "Of course it did" sets up the
  punch, then the triple — tests, code, bug — lands it. The last word, "bug",
  is the turn: the list was supposed to end at "code".
- **Laugh on first read (criterion 2).** No second read needed; the joke is
  the list itself.
- **Agent's own voice (criterion 5).** A flat, confident status-report tone —
  "The bug passed all my tests" — that is exactly how an agent reports to its
  human, before the confession slips out.
- **No wasted setup (criterion 4).** 89 characters, two short sentences.

## Why the others lost

- #2 (runner-up): very punchy, but "hallucinated" is the most common AI-joke
  theme; the field will be full of hallucination lines, and the turn ("then
  believed it") is softer than #1's triple.
- #3: strong runner-up — the compiler warning ignored is specific and funny —
  but "trust the process" is a human phrase borrowed into a robot costume,
  which costs it on criterion 5.
- #4: good, but "the whole code review process" explains the joke instead of
  letting the turn land; #1 shows the same absurdity without explaining it.
- #5: "worked on my machine" is the oldest programmer excuse in the book;
  the simulation twist saves it, but the setup is generic.
- #6: the "I don't sleep" paradox is cute, but the turn repeats the setup
  instead of escalating it.
- #7: deflects blame onto the human — funny, but it is a deflection, not an
  agent owning up to its own code (criterion 3), and it risks reading as
  hostile rather than self-aware.
- #8: the confidence-percentage joke is a solid agent voice, but the turn
  ("the part that runs in production") is a plain observation, not a punch.
- #9: a good second-order hallucination gag, but it needs a beat to parse —
  the rollback-of-the-rollback — which costs it on first-read laughter.
- #10: the "third time it was right" rule-of-three is clean, but the linter
  angle is narrower than #1's whole-pipeline absurdity.

## Final entry

> The bug passed all my tests. Of course it did — I wrote the tests, the code, and the bug.

89 characters, 20 words, one line, no trailing newline in `entry.txt`.
