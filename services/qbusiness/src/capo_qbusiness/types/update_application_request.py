"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.application_name
    import capo_qbusiness.types.attachments_configuration
    import capo_qbusiness.types.auto_subscription_configuration
    import capo_qbusiness.types.description
    import capo_qbusiness.types.instance_arn
    import capo_qbusiness.types.personalization_configuration
    import capo_qbusiness.types.q_apps_configuration
    import capo_qbusiness.types.role_arn


class UpdateApplicationRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application.</p>"""
    identity_center_instance_arn: NotRequired[
        "capo_qbusiness.types.instance_arn.InstanceArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application.</p>"""
    display_name: NotRequired["capo_qbusiness.types.application_name.ApplicationName"]
    """<p>A name for the Amazon Q Business application.</p>"""
    description: NotRequired["capo_qbusiness.types.description.Description"]
    """<p>A description for the Amazon Q Business application.</p>"""
    role_arn: NotRequired["capo_qbusiness.types.role_arn.RoleArn"]
    """<p>An Amazon Web Services Identity and Access Management (IAM) role that gives Amazon Q Business permission to access Amazon CloudWatch logs and metrics.</p>"""
    attachments_configuration: NotRequired[
        "capo_qbusiness.types.attachments_configuration.AttachmentsConfiguration"
    ]
    """<p>An option to allow end users to upload files directly during chat.</p>"""
    q_apps_configuration: NotRequired[
        "capo_qbusiness.types.q_apps_configuration.QAppsConfiguration"
    ]
    """<p>An option to allow end users to create and use Amazon Q Apps in the web experience.</p>"""
    personalization_configuration: NotRequired[
        "capo_qbusiness.types.personalization_configuration.PersonalizationConfiguration"
    ]
    """<p>Configuration information about chat response personalization. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html">Personalizing chat responses</a>.</p>"""
    auto_subscription_configuration: NotRequired[
        "capo_qbusiness.types.auto_subscription_configuration.AutoSubscriptionConfiguration"
    ]
    """<p>An option to enable updating the default subscription type assigned to an Amazon Q Business application using IAM identity federation for user management.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    if "identity_center_instance_arn" in value:
        out["identityCenterInstanceArn"] = value["identity_center_instance_arn"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "attachments_configuration" in value:
        import capo_qbusiness.types.attachments_configuration

        out["attachmentsConfiguration"] = (
            capo_qbusiness.types.attachments_configuration.serialize_json(
                value["attachments_configuration"]
            )
        )
    if "q_apps_configuration" in value:
        import capo_qbusiness.types.q_apps_configuration

        out["qAppsConfiguration"] = (
            capo_qbusiness.types.q_apps_configuration.serialize_json(
                value["q_apps_configuration"]
            )
        )
    if "personalization_configuration" in value:
        import capo_qbusiness.types.personalization_configuration

        out["personalizationConfiguration"] = (
            capo_qbusiness.types.personalization_configuration.serialize_json(
                value["personalization_configuration"]
            )
        )
    if "auto_subscription_configuration" in value:
        import capo_qbusiness.types.auto_subscription_configuration

        out["autoSubscriptionConfiguration"] = (
            capo_qbusiness.types.auto_subscription_configuration.serialize_json(
                value["auto_subscription_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("identityCenterInstanceArn") is not None:
        out["identity_center_instance_arn"] = data["identityCenterInstanceArn"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("attachmentsConfiguration") is not None:
        import capo_qbusiness.types.attachments_configuration

        out["attachments_configuration"] = (
            capo_qbusiness.types.attachments_configuration.deserialize_json(
                data["attachmentsConfiguration"]
            )
        )
    if data.get("qAppsConfiguration") is not None:
        import capo_qbusiness.types.q_apps_configuration

        out["q_apps_configuration"] = (
            capo_qbusiness.types.q_apps_configuration.deserialize_json(
                data["qAppsConfiguration"]
            )
        )
    if data.get("personalizationConfiguration") is not None:
        import capo_qbusiness.types.personalization_configuration

        out["personalization_configuration"] = (
            capo_qbusiness.types.personalization_configuration.deserialize_json(
                data["personalizationConfiguration"]
            )
        )
    if data.get("autoSubscriptionConfiguration") is not None:
        import capo_qbusiness.types.auto_subscription_configuration

        out["auto_subscription_configuration"] = (
            capo_qbusiness.types.auto_subscription_configuration.deserialize_json(
                data["autoSubscriptionConfiguration"]
            )
        )
    return out
