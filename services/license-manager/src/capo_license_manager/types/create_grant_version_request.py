"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateGrantVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.allowed_operation_list
    import capo_license_manager.types.arn
    import capo_license_manager.types.client_token
    import capo_license_manager.types.grant_status
    import capo_license_manager.types.options
    import capo_license_manager.types.status_reason_message
    import capo_license_manager.types.string


class CreateGrantVersionRequest(TypedDict, closed=True):
    client_token: "capo_license_manager.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    grant_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the grant.</p>"""
    grant_name: NotRequired["capo_license_manager.types.string.String"]
    """<p>Grant name.</p>"""
    allowed_operations: NotRequired[
        "capo_license_manager.types.allowed_operation_list.AllowedOperationList"
    ]
    """<p>Allowed operations for the grant.</p>"""
    status: NotRequired["capo_license_manager.types.grant_status.GrantStatus"]
    """<p>Grant status.</p>"""
    status_reason: NotRequired[
        "capo_license_manager.types.status_reason_message.StatusReasonMessage"
    ]
    """<p>Grant status reason.</p>"""
    source_version: NotRequired["capo_license_manager.types.string.String"]
    """<p>Current version of the grant.</p>"""
    options: NotRequired["capo_license_manager.types.options.Options"]
    """<p>The options specified for the grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGrantVersionRequest) -> dict:
    out: dict = {}
    out["ClientToken"] = value["client_token"]
    out["GrantArn"] = value["grant_arn"]
    if "grant_name" in value:
        out["GrantName"] = value["grant_name"]
    if "allowed_operations" in value:
        import capo_license_manager.types.allowed_operation_list

        out["AllowedOperations"] = (
            capo_license_manager.types.allowed_operation_list.serialize_aws_json_1_1(
                value["allowed_operations"]
            )
        )
    if "status" in value:
        import capo_license_manager.types.grant_status

        out["Status"] = capo_license_manager.types.grant_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "source_version" in value:
        out["SourceVersion"] = value["source_version"]
    if "options" in value:
        import capo_license_manager.types.options

        out["Options"] = capo_license_manager.types.options.serialize_aws_json_1_1(
            value["options"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGrantVersionRequest:
    out: CreateGrantVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("GrantArn") is not None:
        out["grant_arn"] = data["GrantArn"]
    else:
        out["grant_arn"] = ""
    if data.get("GrantName") is not None:
        out["grant_name"] = data["GrantName"]
    if data.get("AllowedOperations") is not None:
        import capo_license_manager.types.allowed_operation_list

        out["allowed_operations"] = (
            capo_license_manager.types.allowed_operation_list.deserialize_aws_json_1_1(
                data["AllowedOperations"]
            )
        )
    if data.get("Status") is not None:
        import capo_license_manager.types.grant_status

        out["status"] = (
            capo_license_manager.types.grant_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("SourceVersion") is not None:
        out["source_version"] = data["SourceVersion"]
    if data.get("Options") is not None:
        import capo_license_manager.types.options

        out["options"] = capo_license_manager.types.options.deserialize_aws_json_1_1(
            data["Options"]
        )
    return out
