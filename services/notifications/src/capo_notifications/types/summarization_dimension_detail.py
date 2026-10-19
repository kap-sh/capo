"""Generated from Smithy shape ``com.amazonaws.notifications#SummarizationDimensionDetail``."""

from typing_extensions import TypedDict


class SummarizationDimensionDetail(TypedDict, closed=True):
    name: "str"
    """<p>The name of the SummarizationDimensionDetail.</p>"""
    value: "str"
    """<p>Value of the property used to summarize aggregated events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SummarizationDimensionDetail) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SummarizationDimensionDetail:
    out: SummarizationDimensionDetail = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
