"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TrafficSplitEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.configuration_bundle_reference
    import capo_bedrock_agentcore_control.types.traffic_split_metadata_map


class TrafficSplitEntry(TypedDict, closed=True):
    name: "str"
    """<p>The name of this traffic split variant.</p>"""
    weight: "int"
    """<p>The percentage of traffic to route to this variant. Weights across all entries must sum to 100.</p>"""
    configuration_bundle: "capo_bedrock_agentcore_control.types.configuration_bundle_reference.ConfigurationBundleReference"
    """<p>The configuration bundle reference for this variant.</p>"""
    description: NotRequired["str"]
    """<p>The description of this traffic split variant.</p>"""
    metadata: NotRequired[
        "capo_bedrock_agentcore_control.types.traffic_split_metadata_map.TrafficSplitMetadataMap"
    ]
    """<p>Key-value metadata associated with this traffic split variant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrafficSplitEntry) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["weight"] = value["weight"]
    import capo_bedrock_agentcore_control.types.configuration_bundle_reference

    out["configurationBundle"] = (
        capo_bedrock_agentcore_control.types.configuration_bundle_reference.serialize_json(
            value["configuration_bundle"]
        )
    )
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


def deserialize_json(data: dict) -> TrafficSplitEntry:
    out: TrafficSplitEntry = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("weight") is not None:
        out["weight"] = data["weight"]
    else:
        out["weight"] = 0
    if data.get("configurationBundle") is not None:
        import capo_bedrock_agentcore_control.types.configuration_bundle_reference

        out["configuration_bundle"] = (
            capo_bedrock_agentcore_control.types.configuration_bundle_reference.deserialize_json(
                data["configurationBundle"]
            )
        )
    else:
        raise DeserializationError("TrafficSplitEntry.configuration_bundle required")
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
