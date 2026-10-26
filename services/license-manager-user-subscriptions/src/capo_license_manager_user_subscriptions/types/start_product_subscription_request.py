"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#StartProductSubscriptionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.identity_provider
    import capo_license_manager_user_subscriptions.types.tags


class StartProductSubscriptionRequest(TypedDict, closed=True):
    username: "str"
    """<p>The user name from the identity provider of the user.</p>"""
    identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>An object that specifies details for the identity provider.</p>"""
    product: "str"
    """<p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>OFFICE_STANDARD</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>"""
    domain: NotRequired["str"]
    """<p>The domain name of the Active Directory that contains the user for whom to start the product subscription.</p>"""
    tags: NotRequired["capo_license_manager_user_subscriptions.types.tags.Tags"]
    """<p>The tags that apply to the product subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProductSubscriptionRequest) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    import capo_license_manager_user_subscriptions.types.identity_provider

    out["IdentityProvider"] = (
        capo_license_manager_user_subscriptions.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
    out["Product"] = value["product"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "tags" in value:
        import capo_license_manager_user_subscriptions.types.tags

        out["Tags"] = capo_license_manager_user_subscriptions.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> StartProductSubscriptionRequest:
    out: StartProductSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    if data.get("IdentityProvider") is not None:
        import capo_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            capo_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    else:
        out["identity_provider"] = {"$unknown": {"name": ""}}
    if data.get("Product") is not None:
        out["product"] = data["Product"]
    else:
        out["product"] = ""
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("Tags") is not None:
        import capo_license_manager_user_subscriptions.types.tags

        out["tags"] = (
            capo_license_manager_user_subscriptions.types.tags.deserialize_json(
                data["Tags"]
            )
        )
    return out


def redact_sensitive(value: StartProductSubscriptionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
