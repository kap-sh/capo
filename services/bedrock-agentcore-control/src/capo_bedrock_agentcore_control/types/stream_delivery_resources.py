"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StreamDeliveryResources``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.stream_delivery_resources_list


class StreamDeliveryResources(TypedDict, closed=True):
    resources: "capo_bedrock_agentcore_control.types.stream_delivery_resources_list.StreamDeliveryResourcesList"
    """<p>List of stream delivery resource configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamDeliveryResources) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.stream_delivery_resources_list

    out["resources"] = (
        capo_bedrock_agentcore_control.types.stream_delivery_resources_list.serialize_json(
            value["resources"]
        )
    )
    return out


def deserialize_json(data: dict) -> StreamDeliveryResources:
    out: StreamDeliveryResources = {}  # type: ignore[typeddict-item]
    if data.get("resources") is not None:
        import capo_bedrock_agentcore_control.types.stream_delivery_resources_list

        out["resources"] = (
            capo_bedrock_agentcore_control.types.stream_delivery_resources_list.deserialize_json(
                data["resources"]
            )
        )
    else:
        out["resources"] = []
    return out
