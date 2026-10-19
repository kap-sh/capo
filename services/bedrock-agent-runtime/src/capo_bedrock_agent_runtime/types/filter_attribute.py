"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FilterAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.filter_key
    import capo_bedrock_agent_runtime.types.filter_value


class FilterAttribute(TypedDict, closed=True):
    key: "capo_bedrock_agent_runtime.types.filter_key.FilterKey"
    """<p>The name that the metadata attribute must match.</p>"""
    value: "capo_bedrock_agent_runtime.types.filter_value.FilterValue"
    """<p>The value to which to compare the value of the metadata attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterAttribute) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> FilterAttribute:
    out: FilterAttribute = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = None
    return out
