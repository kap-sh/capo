"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#SatisfiedCondition``."""

from typing_extensions import TypedDict


class SatisfiedCondition(TypedDict, closed=True):
    condition_name: "str"
    """<p>The name of the condition that was satisfied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SatisfiedCondition) -> dict:
    out: dict = {}
    out["conditionName"] = value["condition_name"]
    return out


def deserialize_json(data: dict) -> SatisfiedCondition:
    out: SatisfiedCondition = {}  # type: ignore[typeddict-item]
    if data.get("conditionName") is not None:
        out["condition_name"] = data["conditionName"]
    else:
        out["condition_name"] = ""
    return out
