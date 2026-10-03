"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.account_id
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.application_name_type
    import capo_sso_admin.types.application_provider_arn
    import capo_sso_admin.types.application_status
    import capo_sso_admin.types.date
    import capo_sso_admin.types.description
    import capo_sso_admin.types.identity_store_arn
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.portal_options
    import capo_sso_admin.types.region_name


class DescribeApplicationResponse(TypedDict, closed=True):
    application_arn: NotRequired["capo_sso_admin.types.application_arn.ApplicationArn"]
    """<p>Specifies the ARN of the application.</p>"""
    application_provider_arn: NotRequired[
        "capo_sso_admin.types.application_provider_arn.ApplicationProviderArn"
    ]
    """<p>The ARN of the application provider under which the operation will run.</p>"""
    name: NotRequired["capo_sso_admin.types.application_name_type.ApplicationNameType"]
    """<p>The application name.</p>"""
    application_account: NotRequired["capo_sso_admin.types.account_id.AccountId"]
    """<p>The account ID.</p>"""
    instance_arn: NotRequired["capo_sso_admin.types.instance_arn.InstanceArn"]
    """<p>The ARN of the IAM Identity Center application under which the operation will run. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    identity_store_arn: NotRequired[
        "capo_sso_admin.types.identity_store_arn.IdentityStoreArn"
    ]
    """<p>The ARN of the identity store that is connected to the instance of IAM Identity Center.</p>"""
    status: NotRequired["capo_sso_admin.types.application_status.ApplicationStatus"]
    """<p>Specifies whether the application is enabled or disabled.</p>"""
    portal_options: NotRequired["capo_sso_admin.types.portal_options.PortalOptions"]
    """<p>A structure that describes the options for the portal associated with an application.</p>"""
    description: NotRequired["capo_sso_admin.types.description.Description"]
    """<p>The description of the .</p>"""
    created_date: NotRequired["capo_sso_admin.types.date.Date"]
    """<p>The date the application was created.</p>"""
    created_from: NotRequired["capo_sso_admin.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where the application was created in IAM Identity Center.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "application_provider_arn" in value:
        out["ApplicationProviderArn"] = value["application_provider_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "application_account" in value:
        out["ApplicationAccount"] = value["application_account"]
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "identity_store_arn" in value:
        out["IdentityStoreArn"] = value["identity_store_arn"]
    if "status" in value:
        import capo_sso_admin.types.application_status

        out["Status"] = capo_sso_admin.types.application_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "portal_options" in value:
        import capo_sso_admin.types.portal_options

        out["PortalOptions"] = (
            capo_sso_admin.types.portal_options.serialize_aws_json_1_1(
                value["portal_options"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "created_date" in value:
        import capo_sso_admin.types.date

        out["CreatedDate"] = capo_sso_admin.types.date.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "created_from" in value:
        out["CreatedFrom"] = value["created_from"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationResponse:
    out: DescribeApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    if data.get("ApplicationProviderArn") is not None:
        out["application_provider_arn"] = data["ApplicationProviderArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ApplicationAccount") is not None:
        out["application_account"] = data["ApplicationAccount"]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    if data.get("IdentityStoreArn") is not None:
        out["identity_store_arn"] = data["IdentityStoreArn"]
    if data.get("Status") is not None:
        import capo_sso_admin.types.application_status

        out["status"] = (
            capo_sso_admin.types.application_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("PortalOptions") is not None:
        import capo_sso_admin.types.portal_options

        out["portal_options"] = (
            capo_sso_admin.types.portal_options.deserialize_aws_json_1_1(
                data["PortalOptions"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedDate") is not None:
        import capo_sso_admin.types.date

        out["created_date"] = capo_sso_admin.types.date.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if data.get("CreatedFrom") is not None:
        out["created_from"] = data["CreatedFrom"]
    return out
