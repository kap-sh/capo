"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#CreateLicenseServerEndpointRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.arn
    import capo_license_manager_user_subscriptions.types.license_server_settings
    import capo_license_manager_user_subscriptions.types.tags


class CreateLicenseServerEndpointRequest(TypedDict, closed=True):
    identity_provider_arn: "capo_license_manager_user_subscriptions.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the <code>IdentityProvider</code> resource that contains details about a registered identity provider. In the case of Active Directory, that can be a self-managed Active Directory or an Amazon Web Services Managed Active Directory that contains user identity details.</p>"""
    license_server_settings: "capo_license_manager_user_subscriptions.types.license_server_settings.LicenseServerSettings"
    """<p>The <code>LicenseServerSettings</code> resource to create for the endpoint. The settings include the type of license server and the Secrets Manager secret that enables administrators to add or remove users associated with the license server.</p>"""
    tags: NotRequired["capo_license_manager_user_subscriptions.types.tags.Tags"]
    """<p>The tags that apply for the license server endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLicenseServerEndpointRequest) -> dict:
    out: dict = {}
    out["IdentityProviderArn"] = value["identity_provider_arn"]
    import capo_license_manager_user_subscriptions.types.license_server_settings

    out["LicenseServerSettings"] = (
        capo_license_manager_user_subscriptions.types.license_server_settings.serialize_json(
            value["license_server_settings"]
        )
    )
    if "tags" in value:
        import capo_license_manager_user_subscriptions.types.tags

        out["Tags"] = capo_license_manager_user_subscriptions.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateLicenseServerEndpointRequest:
    out: CreateLicenseServerEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentityProviderArn") is not None:
        out["identity_provider_arn"] = data["IdentityProviderArn"]
    else:
        raise DeserializationError(
            "CreateLicenseServerEndpointRequest.identity_provider_arn required"
        )
    if data.get("LicenseServerSettings") is not None:
        import capo_license_manager_user_subscriptions.types.license_server_settings

        out["license_server_settings"] = (
            capo_license_manager_user_subscriptions.types.license_server_settings.deserialize_json(
                data["LicenseServerSettings"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLicenseServerEndpointRequest.license_server_settings required"
        )
    if data.get("Tags") is not None:
        import capo_license_manager_user_subscriptions.types.tags

        out["tags"] = (
            capo_license_manager_user_subscriptions.types.tags.deserialize_json(
                data["Tags"]
            )
        )
    return out


def redact_sensitive(value: CreateLicenseServerEndpointRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
