"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#Ipv6PrefixSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.ipv6_prefix


class Ipv6PrefixSpecificationRequest(TypedDict, closed=True):
    ipv6_prefix: NotRequired["capo_workspaces_instances.types.ipv6_prefix.Ipv6Prefix"]
    """<p>Specific IPv6 prefix for network interface configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ipv6PrefixSpecificationRequest) -> dict:
    out: dict = {}
    if "ipv6_prefix" in value:
        out["Ipv6Prefix"] = value["ipv6_prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Ipv6PrefixSpecificationRequest:
    out: Ipv6PrefixSpecificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Ipv6Prefix") is not None:
        out["ipv6_prefix"] = data["Ipv6Prefix"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Ipv6PrefixSpecificationRequest) -> dict:
    out: dict = {}
    if "ipv6_prefix" in value:
        out["Ipv6Prefix"] = value["ipv6_prefix"]
    return out


def deserialize_cbor(data: dict) -> Ipv6PrefixSpecificationRequest:
    out: Ipv6PrefixSpecificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Ipv6Prefix") is not None:
        out["ipv6_prefix"] = data["Ipv6Prefix"]
    return out
