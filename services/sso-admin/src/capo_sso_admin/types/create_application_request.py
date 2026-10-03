"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.application_name_type
    import capo_sso_admin.types.application_provider_arn
    import capo_sso_admin.types.application_status
    import capo_sso_admin.types.client_token
    import capo_sso_admin.types.description
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.portal_options
    import capo_sso_admin.types.tag_list


class CreateApplicationRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    application_provider_arn: (
        "capo_sso_admin.types.application_provider_arn.ApplicationProviderArn"
    )
    """<p>The ARN of the application provider under which the operation will run.</p>"""
    name: "capo_sso_admin.types.application_name_type.ApplicationNameType"
    """<p>The name of the .</p>"""
    description: NotRequired["capo_sso_admin.types.description.Description"]
    """<p>The description of the .</p>"""
    portal_options: NotRequired["capo_sso_admin.types.portal_options.PortalOptions"]
    """<p>A structure that describes the options for the portal associated with an application.</p>"""
    tags: NotRequired["capo_sso_admin.types.tag_list.TagList"]
    """<p>Specifies tags to be attached to the application.</p>"""
    status: NotRequired["capo_sso_admin.types.application_status.ApplicationStatus"]
    """<p>Specifies whether the application is enabled or disabled.</p>"""
    client_token: NotRequired["capo_sso_admin.types.client_token.ClientToken"]
    """<p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["ApplicationProviderArn"] = value["application_provider_arn"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "portal_options" in value:
        import capo_sso_admin.types.portal_options

        out["PortalOptions"] = (
            capo_sso_admin.types.portal_options.serialize_aws_json_1_1(
                value["portal_options"]
            )
        )
    if "tags" in value:
        import capo_sso_admin.types.tag_list

        out["Tags"] = capo_sso_admin.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "status" in value:
        import capo_sso_admin.types.application_status

        out["Status"] = capo_sso_admin.types.application_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("CreateApplicationRequest.instance_arn required")
    if data.get("ApplicationProviderArn") is not None:
        out["application_provider_arn"] = data["ApplicationProviderArn"]
    else:
        raise DeserializationError(
            "CreateApplicationRequest.application_provider_arn required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateApplicationRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("PortalOptions") is not None:
        import capo_sso_admin.types.portal_options

        out["portal_options"] = (
            capo_sso_admin.types.portal_options.deserialize_aws_json_1_1(
                data["PortalOptions"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sso_admin.types.tag_list

        out["tags"] = capo_sso_admin.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("Status") is not None:
        import capo_sso_admin.types.application_status

        out["status"] = (
            capo_sso_admin.types.application_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
