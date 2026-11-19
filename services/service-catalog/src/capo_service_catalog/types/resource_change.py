"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.change_action
    import capo_service_catalog.types.logical_resource_id
    import capo_service_catalog.types.physical_resource_id
    import capo_service_catalog.types.plan_resource_type
    import capo_service_catalog.types.replacement
    import capo_service_catalog.types.resource_change_details
    import capo_service_catalog.types.scope


class ResourceChange(TypedDict, closed=True):
    action: NotRequired["capo_service_catalog.types.change_action.ChangeAction"]
    """<p>The change action.</p>"""
    logical_resource_id: NotRequired[
        "capo_service_catalog.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The ID of the resource, as defined in the CloudFormation template.</p>"""
    physical_resource_id: NotRequired[
        "capo_service_catalog.types.physical_resource_id.PhysicalResourceId"
    ]
    """<p>The ID of the resource, if it was already created.</p>"""
    resource_type: NotRequired[
        "capo_service_catalog.types.plan_resource_type.PlanResourceType"
    ]
    """<p>The type of resource.</p>"""
    replacement: NotRequired["capo_service_catalog.types.replacement.Replacement"]
    """<p>If the change type is <code>Modify</code>, indicates whether the existing resource is deleted and replaced with a new one.</p>"""
    scope: NotRequired["capo_service_catalog.types.scope.Scope"]
    """<p>The change scope.</p>"""
    details: NotRequired[
        "capo_service_catalog.types.resource_change_details.ResourceChangeDetails"
    ]
    """<p>Information about the resource changes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceChange) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_service_catalog.types.change_action

        out["Action"] = capo_service_catalog.types.change_action.serialize_aws_json_1_1(
            value["action"]
        )
    if "logical_resource_id" in value:
        out["LogicalResourceId"] = value["logical_resource_id"]
    if "physical_resource_id" in value:
        out["PhysicalResourceId"] = value["physical_resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "replacement" in value:
        import capo_service_catalog.types.replacement

        out["Replacement"] = (
            capo_service_catalog.types.replacement.serialize_aws_json_1_1(
                value["replacement"]
            )
        )
    if "scope" in value:
        import capo_service_catalog.types.scope

        out["Scope"] = capo_service_catalog.types.scope.serialize_aws_json_1_1(
            value["scope"]
        )
    if "details" in value:
        import capo_service_catalog.types.resource_change_details

        out["Details"] = (
            capo_service_catalog.types.resource_change_details.serialize_aws_json_1_1(
                value["details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceChange:
    out: ResourceChange = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_service_catalog.types.change_action

        out["action"] = (
            capo_service_catalog.types.change_action.deserialize_aws_json_1_1(
                data["Action"]
            )
        )
    if data.get("LogicalResourceId") is not None:
        out["logical_resource_id"] = data["LogicalResourceId"]
    if data.get("PhysicalResourceId") is not None:
        out["physical_resource_id"] = data["PhysicalResourceId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("Replacement") is not None:
        import capo_service_catalog.types.replacement

        out["replacement"] = (
            capo_service_catalog.types.replacement.deserialize_aws_json_1_1(
                data["Replacement"]
            )
        )
    if data.get("Scope") is not None:
        import capo_service_catalog.types.scope

        out["scope"] = capo_service_catalog.types.scope.deserialize_aws_json_1_1(
            data["Scope"]
        )
    if data.get("Details") is not None:
        import capo_service_catalog.types.resource_change_details

        out["details"] = (
            capo_service_catalog.types.resource_change_details.deserialize_aws_json_1_1(
                data["Details"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceChange) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_service_catalog.types.change_action

        out["Action"] = capo_service_catalog.types.change_action.serialize_cbor(
            value["action"]
        )
    if "logical_resource_id" in value:
        out["LogicalResourceId"] = value["logical_resource_id"]
    if "physical_resource_id" in value:
        out["PhysicalResourceId"] = value["physical_resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "replacement" in value:
        import capo_service_catalog.types.replacement

        out["Replacement"] = capo_service_catalog.types.replacement.serialize_cbor(
            value["replacement"]
        )
    if "scope" in value:
        import capo_service_catalog.types.scope

        out["Scope"] = capo_service_catalog.types.scope.serialize_cbor(value["scope"])
    if "details" in value:
        import capo_service_catalog.types.resource_change_details

        out["Details"] = (
            capo_service_catalog.types.resource_change_details.serialize_cbor(
                value["details"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ResourceChange:
    out: ResourceChange = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_service_catalog.types.change_action

        out["action"] = capo_service_catalog.types.change_action.deserialize_cbor(
            data["Action"]
        )
    if data.get("LogicalResourceId") is not None:
        out["logical_resource_id"] = data["LogicalResourceId"]
    if data.get("PhysicalResourceId") is not None:
        out["physical_resource_id"] = data["PhysicalResourceId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("Replacement") is not None:
        import capo_service_catalog.types.replacement

        out["replacement"] = capo_service_catalog.types.replacement.deserialize_cbor(
            data["Replacement"]
        )
    if data.get("Scope") is not None:
        import capo_service_catalog.types.scope

        out["scope"] = capo_service_catalog.types.scope.deserialize_cbor(data["Scope"])
    if data.get("Details") is not None:
        import capo_service_catalog.types.resource_change_details

        out["details"] = (
            capo_service_catalog.types.resource_change_details.deserialize_cbor(
                data["Details"]
            )
        )
    return out
