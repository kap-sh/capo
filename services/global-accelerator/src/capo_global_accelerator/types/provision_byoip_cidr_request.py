"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ProvisionByoipCidrRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.cidr_authorization_context
    import capo_global_accelerator.types.generic_string


class ProvisionByoipCidrRequest(TypedDict, closed=True):
    cidr: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The public IPv4 address range, in CIDR notation. The most specific IP prefix that you can specify is /24. The address range cannot overlap with another address range that you've brought to this Amazon Web Services Region or another Region.</p> <p> For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the Global Accelerator Developer Guide.</p>"""
    cidr_authorization_context: "capo_global_accelerator.types.cidr_authorization_context.CidrAuthorizationContext"
    """<p>A signed document that proves that you are authorized to bring the specified IP address range to Amazon using BYOIP. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionByoipCidrRequest) -> dict:
    out: dict = {}
    out["Cidr"] = value["cidr"]
    import capo_global_accelerator.types.cidr_authorization_context

    out["CidrAuthorizationContext"] = (
        capo_global_accelerator.types.cidr_authorization_context.serialize_aws_json_1_1(
            value["cidr_authorization_context"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionByoipCidrRequest:
    out: ProvisionByoipCidrRequest = {}  # type: ignore[typeddict-item]
    if data.get("Cidr") is not None:
        out["cidr"] = data["Cidr"]
    else:
        raise DeserializationError("ProvisionByoipCidrRequest.cidr required")
    if data.get("CidrAuthorizationContext") is not None:
        import capo_global_accelerator.types.cidr_authorization_context

        out["cidr_authorization_context"] = (
            capo_global_accelerator.types.cidr_authorization_context.deserialize_aws_json_1_1(
                data["CidrAuthorizationContext"]
            )
        )
    else:
        raise DeserializationError(
            "ProvisionByoipCidrRequest.cidr_authorization_context required"
        )
    return out
