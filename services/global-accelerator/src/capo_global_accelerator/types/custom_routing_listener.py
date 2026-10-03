"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingListener``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.port_ranges


class CustomRoutingListener(TypedDict, closed=True):
    listener_arn: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    port_ranges: NotRequired["capo_global_accelerator.types.port_ranges.PortRanges"]
    """<p>The port range to support for connections from clients to your accelerator.</p> <p>Separately, you set port ranges for endpoints. For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints.html">About endpoints for custom routing accelerators</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingListener) -> dict:
    out: dict = {}
    if "listener_arn" in value:
        out["ListenerArn"] = value["listener_arn"]
    if "port_ranges" in value:
        import capo_global_accelerator.types.port_ranges

        out["PortRanges"] = (
            capo_global_accelerator.types.port_ranges.serialize_aws_json_1_1(
                value["port_ranges"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomRoutingListener:
    out: CustomRoutingListener = {}  # type: ignore[typeddict-item]
    if data.get("ListenerArn") is not None:
        out["listener_arn"] = data["ListenerArn"]
    if data.get("PortRanges") is not None:
        import capo_global_accelerator.types.port_ranges

        out["port_ranges"] = (
            capo_global_accelerator.types.port_ranges.deserialize_aws_json_1_1(
                data["PortRanges"]
            )
        )
    return out
