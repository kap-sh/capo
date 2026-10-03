"""Generated from Smithy shape ``com.amazonaws.quicksight#AccountSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.edition
    import capo_quicksight.types.namespace
    import capo_quicksight.types.string


class AccountSettings(TypedDict, closed=True):
    account_name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The "account name" you provided for the Quick Sight subscription in your Amazon Web Services account. You create this name when you sign up for Quick Sight. It is unique in all of Amazon Web Services and it appears only when users sign in.</p>"""
    edition: NotRequired["capo_quicksight.types.edition.Edition"]
    """<p>The edition of Quick Sight that you're currently subscribed to: Enterprise edition or Standard edition.</p>"""
    default_namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The default Quick Sight namespace for your Amazon Web Services account. </p>"""
    notification_email: NotRequired["capo_quicksight.types.string.String"]
    """<p>The main notification email for your Quick Sight subscription.</p>"""
    public_sharing_enabled: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether public sharing is turned on for an Quick account. For more information about turning on public sharing, see <a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdatePublicSharingSettings.html">UpdatePublicSharingSettings</a>.</p>"""
    termination_protection_enabled: "capo_quicksight.types.boolean.Boolean"
    """<p>A boolean value that determines whether or not an Quick Sight account can be deleted. A <code>True</code> value doesn't allow the account to be deleted and results in an error message if a user tries to make a <code>DeleteAccountSubsctiption</code> request. A <code>False</code> value will allow the ccount to be deleted. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountSettings) -> dict:
    out: dict = {}
    if "account_name" in value:
        out["AccountName"] = value["account_name"]
    if "edition" in value:
        import capo_quicksight.types.edition

        out["Edition"] = capo_quicksight.types.edition.serialize_json(value["edition"])
    if "default_namespace" in value:
        out["DefaultNamespace"] = value["default_namespace"]
    if "notification_email" in value:
        out["NotificationEmail"] = value["notification_email"]
    out["PublicSharingEnabled"] = value.get("public_sharing_enabled", False)
    out["TerminationProtectionEnabled"] = value.get(
        "termination_protection_enabled", False
    )
    return out


def deserialize_json(data: dict) -> AccountSettings:
    out: AccountSettings = {}  # type: ignore[typeddict-item]
    if data.get("AccountName") is not None:
        out["account_name"] = data["AccountName"]
    if data.get("Edition") is not None:
        import capo_quicksight.types.edition

        out["edition"] = capo_quicksight.types.edition.deserialize_json(data["Edition"])
    if data.get("DefaultNamespace") is not None:
        out["default_namespace"] = data["DefaultNamespace"]
    if data.get("NotificationEmail") is not None:
        out["notification_email"] = data["NotificationEmail"]
    if data.get("PublicSharingEnabled") is not None:
        out["public_sharing_enabled"] = data["PublicSharingEnabled"]
    else:
        out["public_sharing_enabled"] = False
    if data.get("TerminationProtectionEnabled") is not None:
        out["termination_protection_enabled"] = data["TerminationProtectionEnabled"]
    else:
        out["termination_protection_enabled"] = False
    return out
