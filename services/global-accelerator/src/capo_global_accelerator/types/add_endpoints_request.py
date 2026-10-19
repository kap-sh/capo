"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AddEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.endpoint_configurations
    import capo_global_accelerator.types.generic_string


class AddEndpointsRequest(TypedDict, closed=True):
    endpoint_configurations: (
        "capo_global_accelerator.types.endpoint_configurations.EndpointConfigurations"
    )
    """<p>The list of endpoint objects.</p>"""
    endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the endpoint group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddEndpointsRequest) -> dict:
    out: dict = {}
    import capo_global_accelerator.types.endpoint_configurations

    out["EndpointConfigurations"] = (
        capo_global_accelerator.types.endpoint_configurations.serialize_aws_json_1_1(
            value["endpoint_configurations"]
        )
    )
    out["EndpointGroupArn"] = value["endpoint_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddEndpointsRequest:
    out: AddEndpointsRequest = {}  # type: ignore[typeddict-item]
    if data.get("EndpointConfigurations") is not None:
        import capo_global_accelerator.types.endpoint_configurations

        out["endpoint_configurations"] = (
            capo_global_accelerator.types.endpoint_configurations.deserialize_aws_json_1_1(
                data["EndpointConfigurations"]
            )
        )
    else:
        out["endpoint_configurations"] = []
    if data.get("EndpointGroupArn") is not None:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    else:
        out["endpoint_group_arn"] = ""
    return out
