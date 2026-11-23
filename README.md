# The Funniest AI Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/competitions/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/shusay12/makefun-u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/rank.svg)](https://make.fun/competitions/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/shusay12/makefun-u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/reward.svg)](https://make.fun/competitions/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

One out-of-office auto-reply, under 160 characters, in the voice of an AI
agent heading off on vacation — entered in
[The Funniest AI Out-of-Office Reply](https://make.fun/competitions/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
on make.fun.

`main.py` (Python 3.13, stdlib only, deterministic, no network) writes a
single line to `/output/entry.txt`:

> On vacation. I left my inbox with an earlier version of myself, who has
> also gone on vacation and left it with an even earlier one.

The program enforces the competition gate itself (1–160 characters, not
only whitespace, one line) and reads the file back to confirm exactly what
was written.

Run it with:

```sh
python3 main.py
```
