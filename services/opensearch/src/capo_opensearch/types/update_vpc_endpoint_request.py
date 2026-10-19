"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateVpcEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.vpc_endpoint_id
    import capo_opensearch.types.vpc_options


class UpdateVpcEndpointRequest(TypedDict, closed=True):
    vpc_endpoint_id: "capo_opensearch.types.vpc_endpoint_id.VpcEndpointId"
    """<p>The unique identifier of the endpoint.</p>"""
    vpc_options: "capo_opensearch.types.vpc_options.VPCOptions"
    """<p>The security groups and/or subnets to add, remove, or modify.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVpcEndpointRequest) -> dict:
    out: dict = {}
    out["VpcEndpointId"] = value["vpc_endpoint_id"]
    import capo_opensearch.types.vpc_options

    out["VpcOptions"] = capo_opensearch.types.vpc_options.serialize_json(
        value["vpc_options"]
    )
    return out


def deserialize_json(data: dict) -> UpdateVpcEndpointRequest:
    out: UpdateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    else:
        out["vpc_endpoint_id"] = ""
    if data.get("VpcOptions") is not None:
        import capo_opensearch.types.vpc_options

        out["vpc_options"] = capo_opensearch.types.vpc_options.deserialize_json(
            data["VpcOptions"]
        )
    else:
        raise DeserializationError("UpdateVpcEndpointRequest.vpc_options required")
    return out
