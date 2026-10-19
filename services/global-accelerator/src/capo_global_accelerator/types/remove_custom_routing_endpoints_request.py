"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#RemoveCustomRoutingEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.endpoint_ids
    import capo_global_accelerator.types.generic_string


class RemoveCustomRoutingEndpointsRequest(TypedDict, closed=True):
    endpoint_ids: "capo_global_accelerator.types.endpoint_ids.EndpointIds"
    """<p>The IDs for the endpoints. For custom routing accelerators, endpoint IDs are the virtual private cloud (VPC) subnet IDs. </p>"""
    endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the endpoint group to remove endpoints from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveCustomRoutingEndpointsRequest) -> dict:
    out: dict = {}
    import capo_global_accelerator.types.endpoint_ids

    out["EndpointIds"] = (
        capo_global_accelerator.types.endpoint_ids.serialize_aws_json_1_1(
            value["endpoint_ids"]
        )
    )
    out["EndpointGroupArn"] = value["endpoint_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveCustomRoutingEndpointsRequest:
    out: RemoveCustomRoutingEndpointsRequest = {}  # type: ignore[typeddict-item]
    if data.get("EndpointIds") is not None:
        import capo_global_accelerator.types.endpoint_ids

        out["endpoint_ids"] = (
            capo_global_accelerator.types.endpoint_ids.deserialize_aws_json_1_1(
                data["EndpointIds"]
            )
        )
    else:
        out["endpoint_ids"] = []
    if data.get("EndpointGroupArn") is not None:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    else:
        out["endpoint_group_arn"] = ""
    return out
