"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetTrafficSplitEntry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.target_name
    import capo_bedrock_agentcore_control.types.traffic_split_metadata_map


class TargetTrafficSplitEntry(TypedDict, closed=True):
    name: "str"
    """<p>The name of this traffic split variant.</p>"""
    weight: "int"
    """<p>The percentage of traffic to route to this variant.</p>"""
    target_name: "capo_bedrock_agentcore_control.types.target_name.TargetName"
    """<p>The name of the target to route traffic to.</p>"""
    description: NotRequired["str"]
    """<p>The description of this traffic split variant.</p>"""
    metadata: NotRequired[
        "capo_bedrock_agentcore_control.types.traffic_split_metadata_map.TrafficSplitMetadataMap"
    ]
    """<p>Key-value metadata associated with this traffic split variant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetTrafficSplitEntry) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["weight"] = value["weight"]
    out["targetName"] = value["target_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "metadata" in value:
        import capo_bedrock_agentcore_control.types.traffic_split_metadata_map

        out["metadata"] = (
            capo_bedrock_agentcore_control.types.traffic_split_metadata_map.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> TargetTrafficSplitEntry:
    out: TargetTrafficSplitEntry = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("weight") is not None:
        out["weight"] = data["weight"]
    else:
        out["weight"] = 0
    if data.get("targetName") is not None:
        out["target_name"] = data["targetName"]
    else:
        out["target_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("metadata") is not None:
        import capo_bedrock_agentcore_control.types.traffic_split_metadata_map

        out["metadata"] = (
            capo_bedrock_agentcore_control.types.traffic_split_metadata_map.deserialize_json(
                data["metadata"]
            )
        )
    return out


def redact_sensitive(value: TargetTrafficSplitEntry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "target_name" in value:
        out["target_name"] = "*** Sensitive Data Redacted ***"
    return out
