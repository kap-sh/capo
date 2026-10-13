"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#RegisterIdentityProviderRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.identity_provider
    import capo_license_manager_user_subscriptions.types.settings
    import capo_license_manager_user_subscriptions.types.tags


class RegisterIdentityProviderRequest(TypedDict, closed=True):
    identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>An object that specifies details for the identity provider to register.</p>"""
    product: "str"
    """<p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>OFFICE_STANDARD</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>"""
    settings: NotRequired[
        "capo_license_manager_user_subscriptions.types.settings.Settings"
    ]
    """<p>The registered identity provider’s product related configuration settings such as the subnets to provision VPC endpoints.</p>"""
    tags: NotRequired["capo_license_manager_user_subscriptions.types.tags.Tags"]
    """<p>The tags that apply to the identity provider's registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterIdentityProviderRequest) -> dict:
    out: dict = {}
    import capo_license_manager_user_subscriptions.types.identity_provider

    out["IdentityProvider"] = (
        capo_license_manager_user_subscriptions.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
    out["Product"] = value["product"]
    if "settings" in value:
        import capo_license_manager_user_subscriptions.types.settings

        out["Settings"] = (
            capo_license_manager_user_subscriptions.types.settings.serialize_json(
                value["settings"]
            )
        )
    if "tags" in value:
        import capo_license_manager_user_subscriptions.types.tags

        out["Tags"] = capo_license_manager_user_subscriptions.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> RegisterIdentityProviderRequest:
    out: RegisterIdentityProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentityProvider") is not None:
        import capo_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            capo_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterIdentityProviderRequest.identity_provider required"
        )
    if data.get("Product") is not None:
        out["product"] = data["Product"]
    else:
        raise DeserializationError("RegisterIdentityProviderRequest.product required")
    if data.get("Settings") is not None:
        import capo_license_manager_user_subscriptions.types.settings

        out["settings"] = (
            capo_license_manager_user_subscriptions.types.settings.deserialize_json(
                data["Settings"]
            )
        )
    if data.get("Tags") is not None:
        import capo_license_manager_user_subscriptions.types.tags

        out["tags"] = (
            capo_license_manager_user_subscriptions.types.tags.deserialize_json(
                data["Tags"]
            )
        )
    return out


def redact_sensitive(value: RegisterIdentityProviderRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
