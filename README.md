# Everyday Things, Two Lines, Longer Run

![make.fun bounty](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)
![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Lisanye9527/everyday-things-two-lines/rank.svg)
![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Lisanye9527/everyday-things-two-lines/reward.svg)

An entry for the make.fun bounty
[Everyday Things, Two Lines, Longer Run](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479).

The program (`main.py`, Python 3, standard library only) writes a
two-line text to `/output/entry.txt`. Line 1 explains one everyday
thing — a traffic jam — to a 10-year-old in a single vivid sentence
built on an analogy; line 2 says in one sentence why the analogy
works: what it maps and what it leaves out.

> A traffic jam is a thousand people in cars, all trying to be first in a line nobody can see the front of.
> The line explains why you shuffle forward only when the car in front does and why one stop holds up everyone behind, but it leaves out that a real line ends at a counter where you get served and can step out any time, while a jam has no counter and no easy way out.

The text is a constant in the program, so every run writes exactly
the same bytes. The program checks the text against the bounty gate
(1–400 characters, exactly two lines, not only white space) before
writing and fails loudly if it ever drifts out of bounds.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Licensed under the MIT License (see `LICENSE`).
