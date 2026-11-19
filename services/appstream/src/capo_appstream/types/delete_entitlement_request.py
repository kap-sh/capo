"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteEntitlementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.name


class DeleteEntitlementRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the entitlement.</p>"""
    stack_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the stack with which the entitlement is associated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEntitlementRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEntitlementRequest:
    out: DeleteEntitlementRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("StackName") is not None:
        out["stack_name"] = data["StackName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteEntitlementRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    return out


def deserialize_cbor(data: dict) -> DeleteEntitlementRequest:
    out: DeleteEntitlementRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("StackName") is not None:
        out["stack_name"] = data["StackName"]
    return out
