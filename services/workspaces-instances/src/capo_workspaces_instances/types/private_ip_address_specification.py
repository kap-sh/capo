"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#PrivateIpAddressSpecification``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.ipv4_address


class PrivateIpAddressSpecification(TypedDict, closed=True):
    primary: NotRequired["bool"]
    """<p>Indicates if this is the primary private IP address.</p>"""
    private_ip_address: NotRequired[
        "capo_workspaces_instances.types.ipv4_address.Ipv4Address"
    ]
    """<p>Specific private IP address for the network interface.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrivateIpAddressSpecification) -> dict:
    out: dict = {}
    if "primary" in value:
        out["Primary"] = value["primary"]
    if "private_ip_address" in value:
        out["PrivateIpAddress"] = value["private_ip_address"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PrivateIpAddressSpecification:
    out: PrivateIpAddressSpecification = {}  # type: ignore[typeddict-item]
    if data.get("Primary") is not None:
        out["primary"] = data["Primary"]
    if data.get("PrivateIpAddress") is not None:
        out["private_ip_address"] = data["PrivateIpAddress"]
    return out


def redact_sensitive(value: PrivateIpAddressSpecification) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "private_ip_address" in value:
        out["private_ip_address"] = "*** Sensitive Data Redacted ***"
    return out
