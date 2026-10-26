"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#AssociateUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.identity_provider
    import capo_license_manager_user_subscriptions.types.tags


class AssociateUserRequest(TypedDict, closed=True):
    username: "str"
    """<p>The user name from the identity provider.</p>"""
    instance_id: "str"
    """<p>The ID of the EC2 instance that provides the user-based subscription.</p>"""
    identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>The identity provider for the user.</p>"""
    domain: NotRequired["str"]
    """<p>The domain name of the Active Directory that contains information for the user to associate.</p>"""
    tags: NotRequired["capo_license_manager_user_subscriptions.types.tags.Tags"]
    """<p>The tags that apply for the user association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateUserRequest) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["InstanceId"] = value["instance_id"]
    import capo_license_manager_user_subscriptions.types.identity_provider

    out["IdentityProvider"] = (
        capo_license_manager_user_subscriptions.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "tags" in value:
        import capo_license_manager_user_subscriptions.types.tags

        out["Tags"] = capo_license_manager_user_subscriptions.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> AssociateUserRequest:
    out: AssociateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("IdentityProvider") is not None:
        import capo_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            capo_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    else:
        out["identity_provider"] = {"$unknown": {"name": ""}}
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


def redact_sensitive(value: AssociateUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
