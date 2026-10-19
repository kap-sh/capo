"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceCondition``."""

from typing_extensions import TypedDict


class FlowTraceCondition(TypedDict, closed=True):
    condition_name: "str"
    """<p>The name of the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceCondition) -> dict:
    out: dict = {}
    out["conditionName"] = value["condition_name"]
    return out


def deserialize_json(data: dict) -> FlowTraceCondition:
    out: FlowTraceCondition = {}  # type: ignore[typeddict-item]
    if data.get("conditionName") is not None:
        out["condition_name"] = data["conditionName"]
    else:
        out["condition_name"] = ""
    return out
