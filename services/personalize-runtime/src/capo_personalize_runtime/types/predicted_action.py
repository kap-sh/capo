"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#PredictedAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize_runtime.types.action_id
    import capo_personalize_runtime.types.score


class PredictedAction(TypedDict, closed=True):
    action_id: NotRequired["capo_personalize_runtime.types.action_id.ActionID"]
    """<p>The ID of the recommended action.</p>"""
    score: NotRequired["capo_personalize_runtime.types.score.Score"]
    """<p>The score of the recommended action. For information about action scores, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/how-action-recommendation-scoring-works.html">How action recommendation scoring works</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictedAction) -> dict:
    out: dict = {}
    if "action_id" in value:
        out["actionId"] = value["action_id"]
    if "score" in value:
        out["score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    return out


def deserialize_json(data: dict) -> PredictedAction:
    out: PredictedAction = {}  # type: ignore[typeddict-item]
    if data.get("actionId") is not None:
        out["action_id"] = data["actionId"]
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    return out
