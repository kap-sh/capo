"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#TrainingTokenUsage``."""

from typing_extensions import NotRequired, TypedDict


class TrainingTokenUsage(TypedDict, closed=True):
    training_tokens: NotRequired["int"]
    """<p>The number of training tokens consumed by the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainingTokenUsage) -> dict:
    out: dict = {}
    if "training_tokens" in value:
        out["trainingTokens"] = value["training_tokens"]
    return out


def deserialize_json(data: dict) -> TrainingTokenUsage:
    out: TrainingTokenUsage = {}  # type: ignore[typeddict-item]
    if data.get("trainingTokens") is not None:
        out["training_tokens"] = data["trainingTokens"]
    return out
