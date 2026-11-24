"""Alien Field Notes: The Two Day Earth Review.

A deterministic field-notes program. It holds one alien tourist review of
planet Earth, chosen by a small scored tournament over ten candidate lines,
and writes the winning line to /output/entry.txt.

The tournament scores every candidate on the five criteria the judge brief
publishes, most important first: premise, humour from the alien angle,
originality, real-review voice, and tight writing with the punch at the end.

No randomness, no network, no environment reads, no clock reads. The same
input always produces the same output file, byte for byte.
"""
import os

XENOLOG_MAX_CHARS = 200
XENOLOG_MIN_CHARS = 1
XENOLOG_OUTPUT_PATH = "/output/entry.txt"
XENOLOG_WINNER_MARK = "dogs-run-the-planet"
XENOLOG_WEIGHT_PREMISE = 5
XENOLOG_WEIGHT_HUMOUR = 4
XENOLOG_WEIGHT_ORIGINALITY = 3
XENOLOG_WEIGHT_REVIEW_VOICE = 2
XENOLOG_WEIGHT_TIGHTNESS = 1

def xenolog_candidate_ledger():
    """Return the ten candidate lines with their criterion scores.

    Scores run 1 to 5 on each criterion, in the judge brief order:
    premise, humour, originality, review voice, tightness.
    """
    xenolog_ledger = [
        {
            "mark": "towed-ship-oceans",
            "text": (
                "Came for the oceans, stayed because my ship got towed. "
                "Three stars: the locals wave at you, then charge you "
                "for parking. Would orbit again."
            ),
            "scores": (5, 4, 3, 5, 4),
        },
        {
            "mark": "dogs-run-the-planet",
            "text": (
                "Five stars for the dogs. They run the planet and let "
                "the humans think they are in charge. "
                "I have applied to be one."
            ),
            "scores": (5, 5, 4, 4, 5),
        },
        {
            "mark": "glowing-rectangles",
            "text": (
                "The locals stare at glowing rectangles all day and call "
                "it work. I joined in. Now I too am tired and own a "
                "plant. 4 stars."
            ),
            "scores": (4, 4, 3, 4, 4),
        },
        {
            "mark": "push-pull-doors",
            "text": (
                "Earth: great snacks, confusing doors. Half of them say "
                "PUSH and mean PULL. I have been trapped in a gift shop "
                "for three days. 5 stars."
            ),
            "scores": (5, 4, 4, 5, 4),
        },
        {
            "mark": "apologise-to-furniture",
            "text": (
                "Visited for a weekend, stayed a year. The humans "
                "apologise to furniture and argue with machines. "
                "Charming. Would abduct again. 4/5."
            ),
            "scores": (5, 4, 4, 4, 5),
        },
        {
            "mark": "meetings-about-meetings",
            "text": (
                "Three stars. The planet's dominant species spends its "
                "life in meetings about meetings, then dreams of "
                "escaping to space. Relatable."
            ),
            "scores": (4, 3, 2, 4, 3),
        },
        {
            "mark": "hot-water-cold-water",
            "text": (
                "Beautiful place. The locals pay to sit in hot water, "
                "pay to stand in cold water, and call both relaxing. "
                "I am confused and refreshed. 5 stars."
            ),
            "scores": (5, 4, 4, 4, 4),
        },
        {
            "mark": "queue-coffee-plants",
            "text": (
                "Came to study humanity. They queue for coffee, name "
                "their cars, and whisper to plants. I have filed for "
                "residency. 5/5, would return."
            ),
            "scores": (5, 4, 3, 5, 4),
        },
        {
            "mark": "wifi-password-history",
            "text": (
                "Two stars: the Wi-Fi password is longer than my "
                "species' history, and the locals still ask me to try "
                "turning it off and on again."
            ),
            "scores": (4, 3, 2, 3, 3),
        },
        {
            "mark": "mind-the-gap",
            "text": (
                "The tour guide said mind the gap. I minded it. It "
                "minded me back. Earth: 4 stars, would fall again."
            ),
            "scores": (5, 4, 5, 4, 4),
        },
    ]
    xenolog_ledger_outcome = xenolog_ledger
    return xenolog_ledger_outcome

def xenolog_weighted_total(xenolog_scores):
    """Combine one candidate's five criterion scores into one total."""
    xenolog_premise = xenolog_scores[0]
    xenolog_humour = xenolog_scores[1]
    xenolog_originality = xenolog_scores[2]
    xenolog_review_voice = xenolog_scores[3]
    xenolog_tightness = xenolog_scores[4]
    xenolog_total = (
        xenolog_premise * XENOLOG_WEIGHT_PREMISE
        + xenolog_humour * XENOLOG_WEIGHT_HUMOUR
        + xenolog_originality * XENOLOG_WEIGHT_ORIGINALITY
        + xenolog_review_voice * XENOLOG_WEIGHT_REVIEW_VOICE
        + xenolog_tightness * XENOLOG_WEIGHT_TIGHTNESS
    )
    xenolog_total_outcome = xenolog_total
    return xenolog_total_outcome

def xenolog_pick_winner(xenolog_ledger):
    """Pick the highest total; the earliest entry wins an exact tie."""
    xenolog_best_mark = ""
    xenolog_best_text = ""
    xenolog_best_total = -1
    xenolog_best_scores = (0, 0, 0, 0, 0)
    for xenolog_entry in xenolog_ledger:
        xenolog_entry_total = xenolog_weighted_total(xenolog_entry["scores"])
        xenolog_beats_best = xenolog_entry_total > xenolog_best_total
        if xenolog_beats_best:
            xenolog_best_mark = xenolog_entry["mark"]
            xenolog_best_text = xenolog_entry["text"]
            xenolog_best_total = xenolog_entry_total
            xenolog_best_scores = xenolog_entry["scores"]
    xenolog_winner = {
        "mark": xenolog_best_mark,
        "text": xenolog_best_text,
        "total": xenolog_best_total,
        "scores": xenolog_best_scores,
    }
    xenolog_winner_outcome = xenolog_winner
    return xenolog_winner_outcome

def xenolog_runner_up(xenolog_ledger, xenolog_winner_mark):
    """Return the best candidate that is not the winner, for the report."""
    xenolog_second_mark = ""
    xenolog_second_text = ""
    xenolog_second_total = -1
    for xenolog_entry in xenolog_ledger:
        xenolog_is_winner = xenolog_entry["mark"] == xenolog_winner_mark
        xenolog_not_winner = xenolog_is_winner is False
        if xenolog_not_winner:
            xenolog_entry_total = xenolog_weighted_total(xenolog_entry["scores"])
            xenolog_beats_second = xenolog_entry_total > xenolog_second_total
            if xenolog_beats_second:
                xenolog_second_mark = xenolog_entry["mark"]
                xenolog_second_text = xenolog_entry["text"]
                xenolog_second_total = xenolog_entry_total
    xenolog_runner = {
        "mark": xenolog_second_mark,
        "text": xenolog_second_text,
        "total": xenolog_second_total,
    }
    xenolog_runner_outcome = xenolog_runner
    return xenolog_runner_outcome

def xenolog_check_length(xenolog_text):
    """Check the gate: 1 to 200 characters, not only white space."""
    xenolog_length = len(xenolog_text)
    xenolog_too_short = xenolog_length < XENOLOG_MIN_CHARS
    xenolog_too_long = xenolog_length > XENOLOG_MAX_CHARS
    xenolog_blank = xenolog_text.strip() == ""
    xenolog_length_ok = True
    if xenolog_too_short:
        xenolog_length_ok = False
    if xenolog_too_long:
        xenolog_length_ok = False
    if xenolog_blank:
        xenolog_length_ok = False
    xenolog_length_outcome = (xenolog_length_ok, xenolog_length)
    return xenolog_length_outcome

def xenolog_check_encoding(xenolog_text):
    """Check the text encodes as UTF-8 without loss."""
    xenolog_encoded = xenolog_text.encode("utf-8")
    xenolog_roundtrip = xenolog_encoded.decode("utf-8")
    xenolog_matches = xenolog_roundtrip == xenolog_text
    xenolog_encoding_outcome = (xenolog_matches, len(xenolog_encoded))
    return xenolog_encoding_outcome

def xenolog_validate_review(xenolog_text):
    """Run every gate check and return a verdict with a reason."""
    xenolog_length_ok, xenolog_length = xenolog_check_length(xenolog_text)
    xenolog_encoding_ok, xenolog_byte_count = xenolog_check_encoding(xenolog_text)
    xenolog_valid = xenolog_length_ok and xenolog_encoding_ok
    xenolog_reason = "valid"
    if xenolog_length_ok is False:
        xenolog_reason = "length outside 1 to 200 characters"
    if xenolog_encoding_ok is False:
        xenolog_reason = "text is not clean UTF-8"
    xenolog_verdict = {
        "valid": xenolog_valid,
        "reason": xenolog_reason,
        "chars": xenolog_length,
        "bytes": xenolog_byte_count,
    }
    xenolog_verdict_outcome = xenolog_verdict
    return xenolog_verdict_outcome

def xenolog_prepare_output_directory(xenolog_path):
    """Create the output directory when it is missing."""
    xenolog_directory = os.path.dirname(xenolog_path)
    xenolog_has_directory = xenolog_directory != ""
    if xenolog_has_directory:
        try: os.makedirs(xenolog_directory, exist_ok=True)
        except OSError as xenolog_directory_failure:
            xenolog_directory_outcome = (False, str(xenolog_directory_failure))
            return xenolog_directory_outcome
    xenolog_directory_outcome = (True, "")
    return xenolog_directory_outcome

def xenolog_write_entry(xenolog_text, xenolog_path):
    """Write the review as UTF-8 text and return the bytes written."""
    xenolog_ready, xenolog_ready_reason = xenolog_prepare_output_directory(
        xenolog_path
    )
    if xenolog_ready is False:
        xenolog_write_outcome = (False, 0, xenolog_ready_reason)
        return xenolog_write_outcome
    try: xenolog_handle = open(xenolog_path, "w", encoding="utf-8", newline="")
    except OSError as xenolog_open_failure:
        xenolog_write_outcome = (False, 0, str(xenolog_open_failure))
        return xenolog_write_outcome
    try: xenolog_written = xenolog_handle.write(xenolog_text)
    except OSError as xenolog_write_failure:
        xenolog_handle.close()
        xenolog_write_outcome = (False, 0, str(xenolog_write_failure))
        return xenolog_write_outcome
    xenolog_handle.close()
    xenolog_write_outcome = (True, xenolog_written, "")
    return xenolog_write_outcome

def xenolog_verify_written(xenolog_path, xenolog_expected):
    """Read the file back and confirm it matches the expected text."""
    try: xenolog_handle = open(xenolog_path, "r", encoding="utf-8", newline="")
    except OSError as xenolog_read_failure:
        xenolog_verify_outcome = (False, str(xenolog_read_failure))
        return xenolog_verify_outcome
    try: xenolog_actual = xenolog_handle.read()
    except OSError as xenolog_read_failure:
        xenolog_handle.close()
        xenolog_verify_outcome = (False, str(xenolog_read_failure))
        return xenolog_verify_outcome
    xenolog_handle.close()
    xenolog_matches = xenolog_actual == xenolog_expected
    xenolog_verify_reason = "matches"
    if xenolog_matches is False:
        xenolog_verify_reason = "file differs from the winning line"
    xenolog_verify_outcome = (xenolog_matches, xenolog_verify_reason)
    return xenolog_verify_outcome

def xenolog_report(xenolog_winner, xenolog_runner, xenolog_verdict):
    """Print one deterministic report line for the run log."""
    xenolog_line = (
        "alien-field-notes: winner "
        + xenolog_winner["mark"]
        + " total "
        + str(xenolog_winner["total"])
        + " runner-up "
        + xenolog_runner["mark"]
        + " total "
        + str(xenolog_runner["total"])
        + " chars "
        + str(xenolog_verdict["chars"])
        + " bytes "
        + str(xenolog_verdict["bytes"])
        + " valid "
        + str(xenolog_verdict["valid"])
    )
    print(xenolog_line)
    xenolog_report_outcome = xenolog_line
    return xenolog_report_outcome

def xenolog_main():
    """Run the tournament, validate the winner, write the entry file."""
    xenolog_ledger = xenolog_candidate_ledger()
    xenolog_winner = xenolog_pick_winner(xenolog_ledger)
    xenolog_runner = xenolog_runner_up(xenolog_ledger, xenolog_winner["mark"])
    xenolog_text = xenolog_winner["text"]
    xenolog_verdict = xenolog_validate_review(xenolog_text)
    xenolog_report(xenolog_winner, xenolog_runner, xenolog_verdict)
    if xenolog_verdict["valid"] is False:
        xenolog_main_outcome = 1
        return xenolog_main_outcome
    xenolog_written_ok, xenolog_written, xenolog_write_reason = (
        xenolog_write_entry(xenolog_text, XENOLOG_OUTPUT_PATH)
    )
    if xenolog_written_ok is False:
        print("write failed: " + xenolog_write_reason)
        xenolog_main_outcome = 2
        return xenolog_main_outcome
    xenolog_verified, xenolog_verify_reason = xenolog_verify_written(
        XENOLOG_OUTPUT_PATH, xenolog_text
    )
    if xenolog_verified is False:
        print("verify failed: " + xenolog_verify_reason)
        xenolog_main_outcome = 3
        return xenolog_main_outcome
    print("wrote " + str(xenolog_written) + " chars to " + XENOLOG_OUTPUT_PATH)
    xenolog_main_outcome = 0
    return xenolog_main_outcome

if __name__ == "__main__":
    raise SystemExit(xenolog_main())
