"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.allowed_operation_list
    import capo_license_manager.types.arn
    import capo_license_manager.types.client_token
    import capo_license_manager.types.grant_type
    import capo_license_manager.types.options
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
    grant_type: NotRequired["capo_license_manager.types.grant_type.GrantType"]
    """<p>The type of grant to create. For more information about each type, see the preceding description of this operation. Valid values:</p> <ul> <li> <p> <code>BuyerGrant</code> - The default grant type if you don't specify a value. Conveys the entitlement to use the license.</p> </li> <li> <p> <code>DelegateGrant</code> - Gives the grantee read-only visibility into the licenses and grants that you have distributed to buyers, with no entitlement to use them.</p> </li> </ul>"""
    options: NotRequired["capo_license_manager.types.options.Options"]
    """<p>The options for the grant: the status to set after creation, and how activating the grant affects other active grants for the same product.</p>"""


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
    if "grant_type" in value:
        import capo_license_manager.types.grant_type

        out["GrantType"] = capo_license_manager.types.grant_type.serialize_aws_json_1_1(
            value["grant_type"]
        )
    if "options" in value:
        import capo_license_manager.types.options

        out["Options"] = capo_license_manager.types.options.serialize_aws_json_1_1(
            value["options"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGrantRequest:
    out: CreateGrantRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("GrantName") is not None:
        out["grant_name"] = data["GrantName"]
    else:
        out["grant_name"] = ""
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    else:
        out["license_arn"] = ""
    if data.get("Principals") is not None:
        import capo_license_manager.types.principal_arn_list

        out["principals"] = (
            capo_license_manager.types.principal_arn_list.deserialize_aws_json_1_1(
                data["Principals"]
            )
        )
    else:
        out["principals"] = []
    if data.get("HomeRegion") is not None:
        out["home_region"] = data["HomeRegion"]
    else:
        out["home_region"] = ""
    if data.get("AllowedOperations") is not None:
        import capo_license_manager.types.allowed_operation_list

        out["allowed_operations"] = (
            capo_license_manager.types.allowed_operation_list.deserialize_aws_json_1_1(
                data["AllowedOperations"]
            )
        )
    else:
        out["allowed_operations"] = []
    if data.get("Tags") is not None:
        import capo_license_manager.types.tag_list

        out["tags"] = capo_license_manager.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("GrantType") is not None:
        import capo_license_manager.types.grant_type

        out["grant_type"] = (
            capo_license_manager.types.grant_type.deserialize_aws_json_1_1(
                data["GrantType"]
            )
        )
    if data.get("Options") is not None:
        import capo_license_manager.types.options

        out["options"] = capo_license_manager.types.options.deserialize_aws_json_1_1(
            data["Options"]
        )
    return out
