# cases

One directory per lesson, `NN-slug/`, each with `run.sh` (one command, prints expected output,
exits non-zero on a failed assertion) and a `README.md` stating what the case shows and which
exam objective it serves. Default runs with no Google Cloud account; a `--gcp` path may exist
and is gated. Each case is the exam concept as a 30–50 line stdlib script; `just cases` runs all twelve.
