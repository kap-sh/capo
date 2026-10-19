"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ConfigurationBundleToolEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.recommendation_tool_name


class ConfigurationBundleToolEntry(TypedDict, closed=True):
    tool_name: (
        "capo_bedrock_agentcore.types.recommendation_tool_name.RecommendationToolName"
    )
    """<p>The name of the tool.</p>"""
    tool_description_json_path: "str"
    """<p>The JSON path within the configuration bundle's components that contains the tool description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleToolEntry) -> dict:
    out: dict = {}
    out["toolName"] = value["tool_name"]
    out["toolDescriptionJsonPath"] = value["tool_description_json_path"]
    return out


def deserialize_json(data: dict) -> ConfigurationBundleToolEntry:
    out: ConfigurationBundleToolEntry = {}  # type: ignore[typeddict-item]
    if data.get("toolName") is not None:
        out["tool_name"] = data["toolName"]
    else:
        out["tool_name"] = ""
    if data.get("toolDescriptionJsonPath") is not None:
        out["tool_description_json_path"] = data["toolDescriptionJsonPath"]
    else:
        out["tool_description_json_path"] = ""
    return out
