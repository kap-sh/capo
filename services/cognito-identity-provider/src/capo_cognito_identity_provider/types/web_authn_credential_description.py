"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#WebAuthnCredentialDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.string_type
    import capo_cognito_identity_provider.types.web_authn_authenticator_attachment_type
    import capo_cognito_identity_provider.types.web_authn_authenticator_transports_list


class WebAuthnCredentialDescription(TypedDict, closed=True):
    credential_id: "capo_cognito_identity_provider.types.string_type.StringType"
    """<p>The unique identifier of the passkey credential.</p>"""
    friendly_credential_name: (
        "capo_cognito_identity_provider.types.string_type.StringType"
    )
    """<p>An automatically-generated friendly name for the passkey credential.</p>"""
    relying_party_id: "capo_cognito_identity_provider.types.string_type.StringType"
    """<p>The relying-party ID of the provider for the passkey credential.</p>"""
    authenticator_attachment: NotRequired[
        "capo_cognito_identity_provider.types.web_authn_authenticator_attachment_type.WebAuthnAuthenticatorAttachmentType"
    ]
    """<p>The general category of the passkey authenticator. Can be a platform, or on-device authenticator like a built-in fingerprint scanner, or a cross-platform device that's not attached to the device like a Bluetooth security key.</p>"""
    authenticator_transports: "capo_cognito_identity_provider.types.web_authn_authenticator_transports_list.WebAuthnAuthenticatorTransportsList"
    """<p>Information about the transport methods of the passkey credential, for example USB or Bluetooth Low Energy.</p>"""
    created_at: "capo_cognito_identity_provider.types.date_type.DateType"
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAuthnCredentialDescription) -> dict:
    out: dict = {}
    out["CredentialId"] = value["credential_id"]
    out["FriendlyCredentialName"] = value["friendly_credential_name"]
    out["RelyingPartyId"] = value["relying_party_id"]
    if "authenticator_attachment" in value:
        out["AuthenticatorAttachment"] = value["authenticator_attachment"]
    import capo_cognito_identity_provider.types.web_authn_authenticator_transports_list

    out["AuthenticatorTransports"] = (
        capo_cognito_identity_provider.types.web_authn_authenticator_transports_list.serialize_aws_json_1_1(
            value["authenticator_transports"]
        )
    )
    import capo_cognito_identity_provider.types.date_type

    out["CreatedAt"] = (
        capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
            value["created_at"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> WebAuthnCredentialDescription:
    out: WebAuthnCredentialDescription = {}  # type: ignore[typeddict-item]
    if data.get("CredentialId") is not None:
        out["credential_id"] = data["CredentialId"]
    else:
        out["credential_id"] = ""
    if data.get("FriendlyCredentialName") is not None:
        out["friendly_credential_name"] = data["FriendlyCredentialName"]
    else:
        out["friendly_credential_name"] = ""
    if data.get("RelyingPartyId") is not None:
        out["relying_party_id"] = data["RelyingPartyId"]
    else:
        out["relying_party_id"] = ""
    if data.get("AuthenticatorAttachment") is not None:
        out["authenticator_attachment"] = data["AuthenticatorAttachment"]
    if data.get("AuthenticatorTransports") is not None:
        import capo_cognito_identity_provider.types.web_authn_authenticator_transports_list

        out["authenticator_transports"] = (
            capo_cognito_identity_provider.types.web_authn_authenticator_transports_list.deserialize_aws_json_1_1(
                data["AuthenticatorTransports"]
            )
        )
    else:
        out["authenticator_transports"] = []
    if data.get("CreatedAt") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["created_at"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
