"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SaveWeightsConfig``."""

from typing_extensions import NotRequired, TypedDict


class SaveWeightsConfig(TypedDict, closed=True):
    merge_weights: NotRequired["bool"]
    """<p>Specifies whether to merge LoRA adapter weights into the base model before saving. When true, the saved checkpoint contains the full merged model weights.</p>"""
    description: NotRequired["str"]
    """<p>A human-readable description for the saved checkpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaveWeightsConfig) -> dict:
    out: dict = {}
    if "merge_weights" in value:
        out["mergeWeights"] = value["merge_weights"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> SaveWeightsConfig:
    out: SaveWeightsConfig = {}  # type: ignore[typeddict-item]
    if data.get("mergeWeights") is not None:
        out["merge_weights"] = data["mergeWeights"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
