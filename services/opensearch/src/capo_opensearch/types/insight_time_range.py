"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.long

InsightTimeRange = TypedDict(
    "InsightTimeRange",
    {
        "from": "capo_opensearch.types.long.Long",
        "to": "capo_opensearch.types.long.Long",
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: InsightTimeRange) -> dict:
    out: dict = {}
    out["From"] = value["from"]
    out["To"] = value["to"]
    return out


def deserialize_json(data: dict) -> InsightTimeRange:
    out: InsightTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("From") is not None:
        out["from"] = data["From"]
    else:
        out["from"] = 0
    if data.get("To") is not None:
        out["to"] = data["To"]
    else:
        out["to"] = 0
    return out
