"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UpdateCustomRoutingListenerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.port_ranges


class UpdateCustomRoutingListenerRequest(TypedDict, closed=True):
    listener_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the listener to update.</p>"""
    port_ranges: "capo_global_accelerator.types.port_ranges.PortRanges"
    """<p>The updated port range to support for connections from clients to your accelerator. If you remove ports that are currently being used by a subnet endpoint, the call fails.</p> <p>Separately, you set port ranges for endpoints. For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints.html">About endpoints for custom routing accelerators</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCustomRoutingListenerRequest) -> dict:
    out: dict = {}
    out["ListenerArn"] = value["listener_arn"]
    import capo_global_accelerator.types.port_ranges

    out["PortRanges"] = (
        capo_global_accelerator.types.port_ranges.serialize_aws_json_1_1(
            value["port_ranges"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCustomRoutingListenerRequest:
    out: UpdateCustomRoutingListenerRequest = {}  # type: ignore[typeddict-item]
    if data.get("ListenerArn") is not None:
        out["listener_arn"] = data["ListenerArn"]
    else:
        raise DeserializationError(
            "UpdateCustomRoutingListenerRequest.listener_arn required"
        )
    if data.get("PortRanges") is not None:
        import capo_global_accelerator.types.port_ranges

        out["port_ranges"] = (
            capo_global_accelerator.types.port_ranges.deserialize_aws_json_1_1(
                data["PortRanges"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCustomRoutingListenerRequest.port_ranges required"
        )
    return out
