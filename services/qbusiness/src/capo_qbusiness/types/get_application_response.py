"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_arn
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.application_name
    import capo_qbusiness.types.application_status
    import capo_qbusiness.types.applied_attachments_configuration
    import capo_qbusiness.types.auto_subscription_configuration
    import capo_qbusiness.types.client_ids_for_oidc
    import capo_qbusiness.types.description
    import capo_qbusiness.types.encryption_configuration
    import capo_qbusiness.types.error_detail
    import capo_qbusiness.types.iam_identity_provider_arn
    import capo_qbusiness.types.idc_application_arn
    import capo_qbusiness.types.identity_type
    import capo_qbusiness.types.personalization_configuration
    import capo_qbusiness.types.q_apps_configuration
    import capo_qbusiness.types.quick_sight_configuration
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.timestamp


class GetApplicationResponse(TypedDict, closed=True):
    display_name: NotRequired["capo_qbusiness.types.application_name.ApplicationName"]
    """<p>The name of the Amazon Q Business application.</p>"""
    application_id: NotRequired["capo_qbusiness.types.application_id.ApplicationId"]
    """<p>The identifier of the Amazon Q Business application.</p>"""
    application_arn: NotRequired["capo_qbusiness.types.application_arn.ApplicationArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Business application.</p>"""
    identity_type: NotRequired["capo_qbusiness.types.identity_type.IdentityType"]
    """<p>The authentication type being used by a Amazon Q Business application.</p>"""
    iam_identity_provider_arn: NotRequired[
        "capo_qbusiness.types.iam_identity_provider_arn.IAMIdentityProviderArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.</p>"""
    identity_center_application_arn: NotRequired[
        "capo_qbusiness.types.idc_application_arn.IdcApplicationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the AWS IAM Identity Center instance attached to your Amazon Q Business application.</p>"""
    role_arn: NotRequired["capo_qbusiness.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM with permissions to access your CloudWatch logs and metrics.</p>"""
    status: NotRequired["capo_qbusiness.types.application_status.ApplicationStatus"]
    """<p>The status of the Amazon Q Business application.</p>"""
    description: NotRequired["capo_qbusiness.types.description.Description"]
    """<p>A description for the Amazon Q Business application.</p>"""
    encryption_configuration: NotRequired[
        "capo_qbusiness.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The identifier of the Amazon Web Services KMS key that is used to encrypt your data. Amazon Q Business doesn't support asymmetric keys.</p>"""
    created_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business application was last updated.</p>"""
    updated_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business application was last updated.</p>"""
    error: NotRequired["capo_qbusiness.types.error_detail.ErrorDetail"]
    """<p>If the <code>Status</code> field is set to <code>ERROR</code>, the <code>ErrorMessage</code> field contains a description of the error that caused the synchronization to fail.</p>"""
    attachments_configuration: NotRequired[
        "capo_qbusiness.types.applied_attachments_configuration.AppliedAttachmentsConfiguration"
    ]
    """<p>Settings for whether end users can upload files directly during chat.</p>"""
    q_apps_configuration: NotRequired[
        "capo_qbusiness.types.q_apps_configuration.QAppsConfiguration"
    ]
    """<p>Settings for whether end users can create and use Amazon Q Apps in the web experience.</p>"""
    personalization_configuration: NotRequired[
        "capo_qbusiness.types.personalization_configuration.PersonalizationConfiguration"
    ]
    """<p>Configuration information about chat response personalization. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html">Personalizing chat responses</a>.</p>"""
    auto_subscription_configuration: NotRequired[
        "capo_qbusiness.types.auto_subscription_configuration.AutoSubscriptionConfiguration"
    ]
    """<p>Settings for auto-subscription behavior for this application. This is only applicable to SAML and OIDC applications.</p>"""
    client_ids_for_oidc: NotRequired[
        "capo_qbusiness.types.client_ids_for_oidc.ClientIdsForOIDC"
    ]
    """<p>The OIDC client ID for a Amazon Q Business application.</p>"""
    quick_sight_configuration: NotRequired[
        "capo_qbusiness.types.quick_sight_configuration.QuickSightConfiguration"
    ]
    """<p>The Amazon Quick Suite authentication configuration for the Amazon Q Business application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationResponse) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    if "identity_type" in value:
        import capo_qbusiness.types.identity_type

        out["identityType"] = capo_qbusiness.types.identity_type.serialize_json(
            value["identity_type"]
        )
    if "iam_identity_provider_arn" in value:
        out["iamIdentityProviderArn"] = value["iam_identity_provider_arn"]
    if "identity_center_application_arn" in value:
        out["identityCenterApplicationArn"] = value["identity_center_application_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "status" in value:
        import capo_qbusiness.types.application_status

        out["status"] = capo_qbusiness.types.application_status.serialize_json(
            value["status"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "encryption_configuration" in value:
        import capo_qbusiness.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_qbusiness.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "created_at" in value:
        import capo_qbusiness.types.timestamp

        out["createdAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_qbusiness.types.timestamp

        out["updatedAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "error" in value:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.serialize_json(value["error"])
    if "attachments_configuration" in value:
        import capo_qbusiness.types.applied_attachments_configuration

        out["attachmentsConfiguration"] = (
            capo_qbusiness.types.applied_attachments_configuration.serialize_json(
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
    if "client_ids_for_oidc" in value:
        import capo_qbusiness.types.client_ids_for_oidc

        out["clientIdsForOIDC"] = (
            capo_qbusiness.types.client_ids_for_oidc.serialize_json(
                value["client_ids_for_oidc"]
            )
        )
    if "quick_sight_configuration" in value:
        import capo_qbusiness.types.quick_sight_configuration

        out["quickSightConfiguration"] = (
            capo_qbusiness.types.quick_sight_configuration.serialize_json(
                value["quick_sight_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApplicationResponse:
    out: GetApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    if data.get("identityType") is not None:
        import capo_qbusiness.types.identity_type

        out["identity_type"] = capo_qbusiness.types.identity_type.deserialize_json(
            data["identityType"]
        )
    if data.get("iamIdentityProviderArn") is not None:
        out["iam_identity_provider_arn"] = data["iamIdentityProviderArn"]
    if data.get("identityCenterApplicationArn") is not None:
        out["identity_center_application_arn"] = data["identityCenterApplicationArn"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("status") is not None:
        import capo_qbusiness.types.application_status

        out["status"] = capo_qbusiness.types.application_status.deserialize_json(
            data["status"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("encryptionConfiguration") is not None:
        import capo_qbusiness.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_qbusiness.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_qbusiness.types.timestamp

        out["created_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_qbusiness.types.timestamp

        out["updated_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("error") is not None:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.deserialize_json(data["error"])
    if data.get("attachmentsConfiguration") is not None:
        import capo_qbusiness.types.applied_attachments_configuration

        out["attachments_configuration"] = (
            capo_qbusiness.types.applied_attachments_configuration.deserialize_json(
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
    if data.get("clientIdsForOIDC") is not None:
        import capo_qbusiness.types.client_ids_for_oidc

        out["client_ids_for_oidc"] = (
            capo_qbusiness.types.client_ids_for_oidc.deserialize_json(
                data["clientIdsForOIDC"]
            )
        )
    if data.get("quickSightConfiguration") is not None:
        import capo_qbusiness.types.quick_sight_configuration

        out["quick_sight_configuration"] = (
            capo_qbusiness.types.quick_sight_configuration.deserialize_json(
                data["quickSightConfiguration"]
            )
        )
    return out
