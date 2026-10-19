"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#IdentityProviderSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.arn
    import capo_license_manager_user_subscriptions.types.identity_provider
    import capo_license_manager_user_subscriptions.types.settings


class IdentityProviderSummary(TypedDict, closed=True):
    identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>The <code>IdentityProvider</code> resource contains information about an identity provider.</p>"""
    settings: "capo_license_manager_user_subscriptions.types.settings.Settings"
    """<p>The <code>Settings</code> resource contains details about the registered identity provider’s product related configuration settings, such as the subnets to provision VPC endpoints.</p>"""
    product: "str"
    """<p>The name of the user-based subscription product.</p>"""
    status: "str"
    """<p>The status of the identity provider.</p>"""
    identity_provider_arn: NotRequired[
        "capo_license_manager_user_subscriptions.types.arn.Arn"
    ]
    """<p>The Amazon Resource Name (ARN) of the identity provider.</p>"""
    failure_message: NotRequired["str"]
    """<p>The failure message associated with an identity provider.</p>"""
    owner_account_id: NotRequired["str"]
    """<p>The AWS Account ID of the owner of this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderSummary) -> dict:
    out: dict = {}
    import capo_license_manager_user_subscriptions.types.identity_provider

    out["IdentityProvider"] = (
        capo_license_manager_user_subscriptions.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
    import capo_license_manager_user_subscriptions.types.settings

    out["Settings"] = (
        capo_license_manager_user_subscriptions.types.settings.serialize_json(
            value["settings"]
        )
    )
    out["Product"] = value["product"]
    out["Status"] = value["status"]
    if "identity_provider_arn" in value:
        out["IdentityProviderArn"] = value["identity_provider_arn"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    return out


def deserialize_json(data: dict) -> IdentityProviderSummary:
    out: IdentityProviderSummary = {}  # type: ignore[typeddict-item]
    if data.get("IdentityProvider") is not None:
        import capo_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            capo_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    else:
        import capo_license_manager_user_subscriptions.types._unknown

        out["identity_provider"] = (
            capo_license_manager_user_subscriptions.types._unknown.UnknownUnionMember(
                ""
            )
        )
    if data.get("Settings") is not None:
        import capo_license_manager_user_subscriptions.types.settings

        out["settings"] = (
            capo_license_manager_user_subscriptions.types.settings.deserialize_json(
                data["Settings"]
            )
        )
    else:
        raise DeserializationError("IdentityProviderSummary.settings required")
    if data.get("Product") is not None:
        out["product"] = data["Product"]
    else:
        out["product"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("IdentityProviderArn") is not None:
        out["identity_provider_arn"] = data["IdentityProviderArn"]
    if data.get("FailureMessage") is not None:
        out["failure_message"] = data["FailureMessage"]
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    return out
