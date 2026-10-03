"""Generated from Smithy shape ``com.amazonaws.ssoadmin#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.application_name_type
    import capo_sso_admin.types.application_status
    import capo_sso_admin.types.description
    import capo_sso_admin.types.update_application_portal_options


class UpdateApplicationRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    name: NotRequired["capo_sso_admin.types.application_name_type.ApplicationNameType"]
    """<p>Specifies the updated name for the application.</p>"""
    description: NotRequired["capo_sso_admin.types.description.Description"]
    """<p>The description of the .</p>"""
    status: NotRequired["capo_sso_admin.types.application_status.ApplicationStatus"]
    """<p>Specifies whether the application is enabled or disabled.</p>"""
    portal_options: NotRequired[
        "capo_sso_admin.types.update_application_portal_options.UpdateApplicationPortalOptions"
    ]
    """<p>A structure that describes the options for the portal associated with an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_sso_admin.types.application_status

        out["Status"] = capo_sso_admin.types.application_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "portal_options" in value:
        import capo_sso_admin.types.update_application_portal_options

        out["PortalOptions"] = (
            capo_sso_admin.types.update_application_portal_options.serialize_aws_json_1_1(
                value["portal_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError("UpdateApplicationRequest.application_arn required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_sso_admin.types.application_status

        out["status"] = (
            capo_sso_admin.types.application_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("PortalOptions") is not None:
        import capo_sso_admin.types.update_application_portal_options

        out["portal_options"] = (
            capo_sso_admin.types.update_application_portal_options.deserialize_aws_json_1_1(
                data["PortalOptions"]
            )
        )
    return out
