"""Generated from Smithy shape ``com.amazonaws.evs#InitialVlanInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_evs.types.cidr


class InitialVlanInfo(TypedDict, closed=True):
    cidr: "capo_evs.types.cidr.Cidr"
    """<p> The CIDR block that you provide to create an Amazon EVS VLAN subnet. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24. Amazon EVS VLAN subnet CIDR blocks must not overlap with other subnets in the VPC.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InitialVlanInfo) -> dict:
    out: dict = {}
    out["cidr"] = value["cidr"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InitialVlanInfo:
    out: InitialVlanInfo = {}  # type: ignore[typeddict-item]
    if data.get("cidr") is not None:
        out["cidr"] = data["cidr"]
    else:
        out["cidr"] = ""
    return out
