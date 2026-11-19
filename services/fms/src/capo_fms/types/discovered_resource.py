"""Generated from Smithy shape ``com.amazonaws.fms#DiscoveredResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.aws_account_id
    import capo_fms.types.identifier
    import capo_fms.types.resource_name
    import capo_fms.types.resource_type


class DiscoveredResource(TypedDict, closed=True):
    uri: NotRequired["capo_fms.types.identifier.Identifier"]
    """<p>The universal resource identifier (URI) of the discovered resource.</p>"""
    account_id: NotRequired["capo_fms.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account ID associated with the discovered resource.</p>"""
    type: NotRequired["capo_fms.types.resource_type.ResourceType"]
    """<p>The type of the discovered resource.</p>"""
    name: NotRequired["capo_fms.types.resource_name.ResourceName"]
    """<p>The name of the discovered resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoveredResource) -> dict:
    out: dict = {}
    if "uri" in value:
        out["URI"] = value["uri"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "type" in value:
        out["Type"] = value["type"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoveredResource:
    out: DiscoveredResource = {}  # type: ignore[typeddict-item]
    if data.get("URI") is not None:
        out["uri"] = data["URI"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DiscoveredResource) -> dict:
    out: dict = {}
    if "uri" in value:
        out["URI"] = value["uri"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "type" in value:
        out["Type"] = value["type"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> DiscoveredResource:
    out: DiscoveredResource = {}  # type: ignore[typeddict-item]
    if data.get("URI") is not None:
        out["uri"] = data["URI"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
