"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateNetworkResourceMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.network_resource_metadata_map
    import capo_networkmanager.types.resource_arn


class UpdateNetworkResourceMetadataRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    resource_arn: "capo_networkmanager.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource.</p>"""
    metadata: "capo_networkmanager.types.network_resource_metadata_map.NetworkResourceMetadataMap"
    """<p>The resource metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkResourceMetadataRequest) -> dict:
    out: dict = {}
    import capo_networkmanager.types.network_resource_metadata_map

    out["Metadata"] = (
        capo_networkmanager.types.network_resource_metadata_map.serialize_json(
            value["metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateNetworkResourceMetadataRequest:
    out: UpdateNetworkResourceMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("Metadata") is not None:
        import capo_networkmanager.types.network_resource_metadata_map

        out["metadata"] = (
            capo_networkmanager.types.network_resource_metadata_map.deserialize_json(
                data["Metadata"]
            )
        )
    else:
        out["metadata"] = {}
    return out
