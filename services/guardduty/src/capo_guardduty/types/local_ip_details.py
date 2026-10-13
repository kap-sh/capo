"""Generated from Smithy shape ``com.amazonaws.guardduty#LocalIpDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.sensitive_string


class LocalIpDetails(TypedDict, closed=True):
    ip_address_v4: NotRequired["capo_guardduty.types.sensitive_string.SensitiveString"]
    """<p>The IPv4 local address of the connection.</p>"""
    ip_address_v6: NotRequired["capo_guardduty.types.sensitive_string.SensitiveString"]
    """<p>The IPv6 local address of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocalIpDetails) -> dict:
    out: dict = {}
    if "ip_address_v4" in value:
        out["ipAddressV4"] = value["ip_address_v4"]
    if "ip_address_v6" in value:
        out["ipAddressV6"] = value["ip_address_v6"]
    return out


def deserialize_json(data: dict) -> LocalIpDetails:
    out: LocalIpDetails = {}  # type: ignore[typeddict-item]
    if data.get("ipAddressV4") is not None:
        out["ip_address_v4"] = data["ipAddressV4"]
    if data.get("ipAddressV6") is not None:
        out["ip_address_v6"] = data["ipAddressV6"]
    return out


def redact_sensitive(value: LocalIpDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ip_address_v4" in value:
        out["ip_address_v4"] = "*** Sensitive Data Redacted ***"
    if "ip_address_v6" in value:
        out["ip_address_v6"] = "*** Sensitive Data Redacted ***"
    return out
