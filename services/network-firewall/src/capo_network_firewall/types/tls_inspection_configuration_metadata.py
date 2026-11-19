"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TLSInspectionConfigurationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class TLSInspectionConfigurationMetadata(TypedDict, closed=True):
    name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.</p>"""
    arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the TLS inspection configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TLSInspectionConfigurationMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TLSInspectionConfigurationMetadata:
    out: TLSInspectionConfigurationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TLSInspectionConfigurationMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_cbor(data: dict) -> TLSInspectionConfigurationMetadata:
    out: TLSInspectionConfigurationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
