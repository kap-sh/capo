"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DeprovisionByoipCidrRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string


class DeprovisionByoipCidrRequest(TypedDict, closed=True):
    cidr: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The address range, in CIDR notation. The prefix must be the same prefix that you specified when you provisioned the address range.</p> <p> For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the Global Accelerator Developer Guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeprovisionByoipCidrRequest) -> dict:
    out: dict = {}
    out["Cidr"] = value["cidr"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeprovisionByoipCidrRequest:
    out: DeprovisionByoipCidrRequest = {}  # type: ignore[typeddict-item]
    if data.get("Cidr") is not None:
        out["cidr"] = data["Cidr"]
    else:
        raise DeserializationError("DeprovisionByoipCidrRequest.cidr required")
    return out
