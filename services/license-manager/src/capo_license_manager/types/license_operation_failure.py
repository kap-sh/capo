"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseOperationFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.date_time
    import capo_license_manager.types.metadata_list
    import capo_license_manager.types.resource_type
    import capo_license_manager.types.string


class LicenseOperationFailure(TypedDict, closed=True):
    resource_arn: NotRequired["capo_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the resource.</p>"""
    resource_type: NotRequired["capo_license_manager.types.resource_type.ResourceType"]
    """<p>Resource type.</p>"""
    error_message: NotRequired["capo_license_manager.types.string.String"]
    """<p>Error message.</p>"""
    failure_time: NotRequired["capo_license_manager.types.date_time.DateTime"]
    """<p>Failure time.</p>"""
    operation_name: NotRequired["capo_license_manager.types.string.String"]
    """<p>Name of the operation.</p>"""
    resource_owner_id: NotRequired["capo_license_manager.types.string.String"]
    """<p>ID of the Amazon Web Services account that owns the resource.</p>"""
    operation_requested_by: NotRequired["capo_license_manager.types.string.String"]
    """<p>The requester is "License Manager Automated Discovery".</p>"""
    metadata_list: NotRequired["capo_license_manager.types.metadata_list.MetadataList"]
    """<p>Reserved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseOperationFailure) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        import capo_license_manager.types.resource_type

        out["ResourceType"] = (
            capo_license_manager.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "failure_time" in value:
        import capo_license_manager.types.date_time

        out["FailureTime"] = (
            capo_license_manager.types.date_time.serialize_aws_json_1_1(
                value["failure_time"]
            )
        )
    if "operation_name" in value:
        out["OperationName"] = value["operation_name"]
    if "resource_owner_id" in value:
        out["ResourceOwnerId"] = value["resource_owner_id"]
    if "operation_requested_by" in value:
        out["OperationRequestedBy"] = value["operation_requested_by"]
    if "metadata_list" in value:
        import capo_license_manager.types.metadata_list

        out["MetadataList"] = (
            capo_license_manager.types.metadata_list.serialize_aws_json_1_1(
                value["metadata_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseOperationFailure:
    out: LicenseOperationFailure = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("ResourceType") is not None:
        import capo_license_manager.types.resource_type

        out["resource_type"] = (
            capo_license_manager.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("FailureTime") is not None:
        import capo_license_manager.types.date_time

        out["failure_time"] = (
            capo_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["FailureTime"]
            )
        )
    if data.get("OperationName") is not None:
        out["operation_name"] = data["OperationName"]
    if data.get("ResourceOwnerId") is not None:
        out["resource_owner_id"] = data["ResourceOwnerId"]
    if data.get("OperationRequestedBy") is not None:
        out["operation_requested_by"] = data["OperationRequestedBy"]
    if data.get("MetadataList") is not None:
        import capo_license_manager.types.metadata_list

        out["metadata_list"] = (
            capo_license_manager.types.metadata_list.deserialize_aws_json_1_1(
                data["MetadataList"]
            )
        )
    return out
