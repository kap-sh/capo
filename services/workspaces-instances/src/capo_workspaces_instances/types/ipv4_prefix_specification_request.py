"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#Ipv4PrefixSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.ipv4_prefix


class Ipv4PrefixSpecificationRequest(TypedDict, closed=True):
    ipv4_prefix: NotRequired["capo_workspaces_instances.types.ipv4_prefix.Ipv4Prefix"]
    """<p>Specific IPv4 prefix for network interface configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ipv4PrefixSpecificationRequest) -> dict:
    out: dict = {}
    if "ipv4_prefix" in value:
        out["Ipv4Prefix"] = value["ipv4_prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Ipv4PrefixSpecificationRequest:
    out: Ipv4PrefixSpecificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Ipv4Prefix") is not None:
        out["ipv4_prefix"] = data["Ipv4Prefix"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Ipv4PrefixSpecificationRequest) -> dict:
    out: dict = {}
    if "ipv4_prefix" in value:
        out["Ipv4Prefix"] = value["ipv4_prefix"]
    return out


def deserialize_cbor(data: dict) -> Ipv4PrefixSpecificationRequest:
    out: Ipv4PrefixSpecificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Ipv4Prefix") is not None:
        out["ipv4_prefix"] = data["Ipv4Prefix"]
    return out
