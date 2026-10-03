"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#WithdrawByoipCidrRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string


class WithdrawByoipCidrRequest(TypedDict, closed=True):
    cidr: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The address range, in CIDR notation.</p> <p> For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the Global Accelerator Developer Guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WithdrawByoipCidrRequest) -> dict:
    out: dict = {}
    out["Cidr"] = value["cidr"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WithdrawByoipCidrRequest:
    out: WithdrawByoipCidrRequest = {}  # type: ignore[typeddict-item]
    if data.get("Cidr") is not None:
        out["cidr"] = data["Cidr"]
    else:
        raise DeserializationError("WithdrawByoipCidrRequest.cidr required")
    return out
