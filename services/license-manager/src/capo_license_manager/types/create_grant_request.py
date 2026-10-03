"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.allowed_operation_list
    import capo_license_manager.types.arn
    import capo_license_manager.types.client_token
    import capo_license_manager.types.principal_arn_list
    import capo_license_manager.types.string
    import capo_license_manager.types.tag_list


class CreateGrantRequest(TypedDict, closed=True):
    client_token: "capo_license_manager.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    grant_name: "capo_license_manager.types.string.String"
    """<p>Grant name.</p>"""
    license_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license.</p>"""
    principals: "capo_license_manager.types.principal_arn_list.PrincipalArnList"
    """<p>The grant principals. You can specify one of the following as an Amazon Resource Name (ARN):</p> <ul> <li> <p>An Amazon Web Services account, which includes only the account specified.</p> </li> </ul> <ul> <li> <p>An organizational unit (OU), which includes all accounts in the OU.</p> </li> </ul> <ul> <li> <p>An organization, which will include all accounts across your organization.</p> </li> </ul>"""
    home_region: "capo_license_manager.types.string.String"
    """<p>Home Region of the grant.</p>"""
    allowed_operations: (
        "capo_license_manager.types.allowed_operation_list.AllowedOperationList"
    )
    """<p>Allowed operations for the grant.</p>"""
    tags: NotRequired["capo_license_manager.types.tag_list.TagList"]
    """<p>Tags to add to the grant. For more information about tagging support in License Manager, see the <a href="https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html">TagResource</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGrantRequest) -> dict:
    out: dict = {}
    out["ClientToken"] = value["client_token"]
    out["GrantName"] = value["grant_name"]
    out["LicenseArn"] = value["license_arn"]
    import capo_license_manager.types.principal_arn_list

    out["Principals"] = (
        capo_license_manager.types.principal_arn_list.serialize_aws_json_1_1(
            value["principals"]
        )
    )
    out["HomeRegion"] = value["home_region"]
    import capo_license_manager.types.allowed_operation_list

    out["AllowedOperations"] = (
        capo_license_manager.types.allowed_operation_list.serialize_aws_json_1_1(
            value["allowed_operations"]
        )
    )
    if "tags" in value:
        import capo_license_manager.types.tag_list

        out["Tags"] = capo_license_manager.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGrantRequest:
    out: CreateGrantRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CreateGrantRequest.client_token required")
    if data.get("GrantName") is not None:
        out["grant_name"] = data["GrantName"]
    else:
        raise DeserializationError("CreateGrantRequest.grant_name required")
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    else:
        raise DeserializationError("CreateGrantRequest.license_arn required")
    if data.get("Principals") is not None:
        import capo_license_manager.types.principal_arn_list

        out["principals"] = (
            capo_license_manager.types.principal_arn_list.deserialize_aws_json_1_1(
                data["Principals"]
            )
        )
    else:
        raise DeserializationError("CreateGrantRequest.principals required")
    if data.get("HomeRegion") is not None:
        out["home_region"] = data["HomeRegion"]
    else:
        raise DeserializationError("CreateGrantRequest.home_region required")
    if data.get("AllowedOperations") is not None:
        import capo_license_manager.types.allowed_operation_list

        out["allowed_operations"] = (
            capo_license_manager.types.allowed_operation_list.deserialize_aws_json_1_1(
                data["AllowedOperations"]
            )
        )
    else:
        raise DeserializationError("CreateGrantRequest.allowed_operations required")
    if data.get("Tags") is not None:
        import capo_license_manager.types.tag_list

        out["tags"] = capo_license_manager.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
