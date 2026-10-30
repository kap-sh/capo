"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SaveStateConfig``."""

from typing_extensions import NotRequired, TypedDict


class SaveStateConfig(TypedDict, closed=True):
    description: NotRequired["str"]
    """<p>A human-readable description for the saved state checkpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaveStateConfig) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> SaveStateConfig:
    out: SaveStateConfig = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
