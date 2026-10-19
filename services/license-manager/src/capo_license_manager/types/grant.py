"""Generated from Smithy shape ``com.amazonaws.licensemanager#Grant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.allowed_operation_list
    import capo_license_manager.types.arn
    import capo_license_manager.types.grant_status
    import capo_license_manager.types.options
    import capo_license_manager.types.status_reason_message
    import capo_license_manager.types.string


class Grant(TypedDict, closed=True):
    grant_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the grant.</p>"""
    grant_name: "capo_license_manager.types.string.String"
    """<p>Grant name.</p>"""
    parent_arn: "capo_license_manager.types.arn.Arn"
    """<p>Parent ARN.</p>"""
    license_arn: "capo_license_manager.types.arn.Arn"
    """<p>License ARN.</p>"""
    grantee_principal_arn: "capo_license_manager.types.arn.Arn"
    """<p>The grantee principal ARN.</p>"""
    home_region: "capo_license_manager.types.string.String"
    """<p>Home Region of the grant.</p>"""
    grant_status: "capo_license_manager.types.grant_status.GrantStatus"
    """<p>Grant status.</p>"""
    status_reason: NotRequired[
        "capo_license_manager.types.status_reason_message.StatusReasonMessage"
    ]
    """<p>Grant status reason.</p>"""
    version: "capo_license_manager.types.string.String"
    """<p>Grant version.</p>"""
    granted_operations: (
        "capo_license_manager.types.allowed_operation_list.AllowedOperationList"
    )
    """<p>Granted operations.</p>"""
    options: NotRequired["capo_license_manager.types.options.Options"]
    """<p>The options specified for the grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Grant) -> dict:
    out: dict = {}
    out["GrantArn"] = value["grant_arn"]
    out["GrantName"] = value["grant_name"]
    out["ParentArn"] = value["parent_arn"]
    out["LicenseArn"] = value["license_arn"]
    out["GranteePrincipalArn"] = value["grantee_principal_arn"]
    out["HomeRegion"] = value["home_region"]
    import capo_license_manager.types.grant_status

    out["GrantStatus"] = capo_license_manager.types.grant_status.serialize_aws_json_1_1(
        value["grant_status"]
    )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    out["Version"] = value["version"]
    import capo_license_manager.types.allowed_operation_list

    out["GrantedOperations"] = (
        capo_license_manager.types.allowed_operation_list.serialize_aws_json_1_1(
            value["granted_operations"]
        )
    )
    if "options" in value:
        import capo_license_manager.types.options

        out["Options"] = capo_license_manager.types.options.serialize_aws_json_1_1(
            value["options"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Grant:
    out: Grant = {}  # type: ignore[typeddict-item]
    if data.get("GrantArn") is not None:
        out["grant_arn"] = data["GrantArn"]
    else:
        out["grant_arn"] = ""
    if data.get("GrantName") is not None:
        out["grant_name"] = data["GrantName"]
    else:
        out["grant_name"] = ""
    if data.get("ParentArn") is not None:
        out["parent_arn"] = data["ParentArn"]
    else:
        out["parent_arn"] = ""
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    else:
        out["license_arn"] = ""
    if data.get("GranteePrincipalArn") is not None:
        out["grantee_principal_arn"] = data["GranteePrincipalArn"]
    else:
        out["grantee_principal_arn"] = ""
    if data.get("HomeRegion") is not None:
        out["home_region"] = data["HomeRegion"]
    else:
        out["home_region"] = ""
    if data.get("GrantStatus") is not None:
        import capo_license_manager.types.grant_status

        out["grant_status"] = (
            capo_license_manager.types.grant_status.deserialize_aws_json_1_1(
                data["GrantStatus"]
            )
        )
    else:
        import typing

        out["grant_status"] = typing.cast(
            "capo_license_manager.types.grant_status.GrantStatus", ""
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = ""
    if data.get("GrantedOperations") is not None:
        import capo_license_manager.types.allowed_operation_list

        out["granted_operations"] = (
            capo_license_manager.types.allowed_operation_list.deserialize_aws_json_1_1(
                data["GrantedOperations"]
            )
        )
    else:
        out["granted_operations"] = []
    if data.get("Options") is not None:
        import capo_license_manager.types.options

        out["options"] = capo_license_manager.types.options.deserialize_aws_json_1_1(
            data["Options"]
        )
    return out
