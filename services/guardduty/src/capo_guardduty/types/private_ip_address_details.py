"""Generated from Smithy shape ``com.amazonaws.guardduty#PrivateIpAddressDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.sensitive_string
    import capo_guardduty.types.string


class PrivateIpAddressDetails(TypedDict, closed=True):
    private_dns_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The private DNS name of the EC2 instance.</p>"""
    private_ip_address: NotRequired[
        "capo_guardduty.types.sensitive_string.SensitiveString"
    ]
    """<p>The private IP address of the EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateIpAddressDetails) -> dict:
    out: dict = {}
    if "private_dns_name" in value:
        out["privateDnsName"] = value["private_dns_name"]
    if "private_ip_address" in value:
        out["privateIpAddress"] = value["private_ip_address"]
    return out


def deserialize_json(data: dict) -> PrivateIpAddressDetails:
    out: PrivateIpAddressDetails = {}  # type: ignore[typeddict-item]
    if data.get("privateDnsName") is not None:
        out["private_dns_name"] = data["privateDnsName"]
    if data.get("privateIpAddress") is not None:
        out["private_ip_address"] = data["privateIpAddress"]
    return out


def redact_sensitive(value: PrivateIpAddressDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "private_ip_address" in value:
        out["private_ip_address"] = "*** Sensitive Data Redacted ***"
    return out
