"""Generated from Smithy shape ``com.amazonaws.appstream#AssociateApplicationToEntitlementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.name
    import capo_appstream.types.string


class AssociateApplicationToEntitlementRequest(TypedDict, closed=True):
    stack_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the stack.</p>"""
    entitlement_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the entitlement.</p>"""
    application_identifier: NotRequired["capo_appstream.types.string.String"]
    """<p>The identifier of the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateApplicationToEntitlementRequest) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "entitlement_name" in value:
        out["EntitlementName"] = value["entitlement_name"]
    if "application_identifier" in value:
        out["ApplicationIdentifier"] = value["application_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateApplicationToEntitlementRequest:
    out: AssociateApplicationToEntitlementRequest = {}  # type: ignore[typeddict-item]
    if data.get("StackName") is not None:
        out["stack_name"] = data["StackName"]
    if data.get("EntitlementName") is not None:
        out["entitlement_name"] = data["EntitlementName"]
    if data.get("ApplicationIdentifier") is not None:
        out["application_identifier"] = data["ApplicationIdentifier"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateApplicationToEntitlementRequest) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "entitlement_name" in value:
        out["EntitlementName"] = value["entitlement_name"]
    if "application_identifier" in value:
        out["ApplicationIdentifier"] = value["application_identifier"]
    return out


def deserialize_cbor(data: dict) -> AssociateApplicationToEntitlementRequest:
    out: AssociateApplicationToEntitlementRequest = {}  # type: ignore[typeddict-item]
    if data.get("StackName") is not None:
        out["stack_name"] = data["StackName"]
    if data.get("EntitlementName") is not None:
        out["entitlement_name"] = data["EntitlementName"]
    if data.get("ApplicationIdentifier") is not None:
        out["application_identifier"] = data["ApplicationIdentifier"]
    return out
