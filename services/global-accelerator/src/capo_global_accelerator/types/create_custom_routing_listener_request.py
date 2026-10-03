"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CreateCustomRoutingListenerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.idempotency_token
    import capo_global_accelerator.types.port_ranges


class CreateCustomRoutingListenerRequest(TypedDict, closed=True):
    accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the accelerator for a custom routing listener.</p>"""
    port_ranges: "capo_global_accelerator.types.port_ranges.PortRanges"
    """<p>The port range to support for connections from clients to your accelerator.</p> <p>Separately, you set port ranges for endpoints. For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints.html">About endpoints for custom routing accelerators</a>.</p>"""
    idempotency_token: (
        "capo_global_accelerator.types.idempotency_token.IdempotencyToken"
    )
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomRoutingListenerRequest) -> dict:
    out: dict = {}
    out["AcceleratorArn"] = value["accelerator_arn"]
    import capo_global_accelerator.types.port_ranges

    out["PortRanges"] = (
        capo_global_accelerator.types.port_ranges.serialize_aws_json_1_1(
            value["port_ranges"]
        )
    )
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomRoutingListenerRequest:
    out: CreateCustomRoutingListenerRequest = {}  # type: ignore[typeddict-item]
    if data.get("AcceleratorArn") is not None:
        out["accelerator_arn"] = data["AcceleratorArn"]
    else:
        raise DeserializationError(
            "CreateCustomRoutingListenerRequest.accelerator_arn required"
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
            "CreateCustomRoutingListenerRequest.port_ranges required"
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError(
            "CreateCustomRoutingListenerRequest.idempotency_token required"
        )
    return out
