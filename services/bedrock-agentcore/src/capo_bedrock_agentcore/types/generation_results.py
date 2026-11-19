"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationResults``."""

from typing_extensions import NotRequired, TypedDict


class GenerationResults(TypedDict, closed=True):
    sessions_matched: NotRequired["int"]
    """<p>The number of sessions that matched the filters or were named in the request, before sampling. This includes sessions that later failed.</p>"""
    sessions_selected: NotRequired["int"]
    """<p>The number of sessions left after sampling.</p>"""
    sessions_unscored: NotRequired["int"]
    """<p>The number of sessions left out because an evaluator filter had no result to compare, either because the session wasn't evaluated yet or because the evaluation failed.</p>"""
    sessions_failed: NotRequired["int"]
    """<p>The number of sessions dropped because of an error. See <code>errorDetails</code> for the errors.</p>"""
    scenarios_generated: NotRequired["int"]
    """<p>The number of scenarios generated.</p>"""
    scenarios_deduplicated: NotRequired["int"]
    """<p>The number of scenarios left out as duplicates, of each other or of examples already in the draft.</p>"""
    examples_written: NotRequired["int"]
    """<p>The number of examples added to the dataset's draft.</p>"""
    examples_with_ground_truth: NotRequired["int"]
    """<p>The number of added examples that have reference fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerationResults) -> dict:
    out: dict = {}
    if "sessions_matched" in value:
        out["sessionsMatched"] = value["sessions_matched"]
    if "sessions_selected" in value:
        out["sessionsSelected"] = value["sessions_selected"]
    if "sessions_unscored" in value:
        out["sessionsUnscored"] = value["sessions_unscored"]
    if "sessions_failed" in value:
        out["sessionsFailed"] = value["sessions_failed"]
    if "scenarios_generated" in value:
        out["scenariosGenerated"] = value["scenarios_generated"]
    if "scenarios_deduplicated" in value:
        out["scenariosDeduplicated"] = value["scenarios_deduplicated"]
    if "examples_written" in value:
        out["examplesWritten"] = value["examples_written"]
    if "examples_with_ground_truth" in value:
        out["examplesWithGroundTruth"] = value["examples_with_ground_truth"]
    return out


def deserialize_json(data: dict) -> GenerationResults:
    out: GenerationResults = {}  # type: ignore[typeddict-item]
    if data.get("sessionsMatched") is not None:
        out["sessions_matched"] = data["sessionsMatched"]
    if data.get("sessionsSelected") is not None:
        out["sessions_selected"] = data["sessionsSelected"]
    if data.get("sessionsUnscored") is not None:
        out["sessions_unscored"] = data["sessionsUnscored"]
    if data.get("sessionsFailed") is not None:
        out["sessions_failed"] = data["sessionsFailed"]
    if data.get("scenariosGenerated") is not None:
        out["scenarios_generated"] = data["scenariosGenerated"]
    if data.get("scenariosDeduplicated") is not None:
        out["scenarios_deduplicated"] = data["scenariosDeduplicated"]
    if data.get("examplesWritten") is not None:
        out["examples_written"] = data["examplesWritten"]
    if data.get("examplesWithGroundTruth") is not None:
        out["examples_with_ground_truth"] = data["examplesWithGroundTruth"]
    return out
