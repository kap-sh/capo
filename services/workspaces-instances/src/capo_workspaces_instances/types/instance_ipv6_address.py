"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceIpv6Address``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.ipv6_address


class InstanceIpv6Address(TypedDict, closed=True):
    ipv6_address: NotRequired[
        "capo_workspaces_instances.types.ipv6_address.Ipv6Address"
    ]
    """<p>Specific IPv6 address assigned to the instance.</p>"""
    is_primary_ipv6: NotRequired["bool"]
    """<p>Indicates if this is the primary IPv6 address for the instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceIpv6Address) -> dict:
    out: dict = {}
    if "ipv6_address" in value:
        out["Ipv6Address"] = value["ipv6_address"]
    if "is_primary_ipv6" in value:
        out["IsPrimaryIpv6"] = value["is_primary_ipv6"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceIpv6Address:
    out: InstanceIpv6Address = {}  # type: ignore[typeddict-item]
    if data.get("Ipv6Address") is not None:
        out["ipv6_address"] = data["Ipv6Address"]
    if data.get("IsPrimaryIpv6") is not None:
        out["is_primary_ipv6"] = data["IsPrimaryIpv6"]
    return out


def redact_sensitive(value: InstanceIpv6Address) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ipv6_address" in value:
        out["ipv6_address"] = "*** Sensitive Data Redacted ***"
    return out
