"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#InstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.identity_provider
    import capo_license_manager_user_subscriptions.types.string_list


class InstanceSummary(TypedDict, closed=True):
    instance_id: "str"
    """<p>The ID of the EC2 instance, which provides user-based subscriptions.</p>"""
    status: "str"
    """<p>The status of an EC2 instance resource.</p>"""
    products: "capo_license_manager_user_subscriptions.types.string_list.StringList"
    """<p>A list of provided user-based subscription products.</p>"""
    last_status_check_date: NotRequired["str"]
    """<p>The date of the last status check.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message for an EC2 instance.</p>"""
    owner_account_id: NotRequired["str"]
    """<p>The AWS Account ID of the owner of this resource.</p>"""
    identity_provider: NotRequired[
        "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    ]
    """<p>The <code>IdentityProvider</code> resource specifies details about the identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceSummary) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["Status"] = value["status"]
    import capo_license_manager_user_subscriptions.types.string_list

    out["Products"] = (
        capo_license_manager_user_subscriptions.types.string_list.serialize_json(
            value["products"]
        )
    )
    if "last_status_check_date" in value:
        out["LastStatusCheckDate"] = value["last_status_check_date"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "identity_provider" in value:
        import capo_license_manager_user_subscriptions.types.identity_provider

        out["IdentityProvider"] = (
            capo_license_manager_user_subscriptions.types.identity_provider.serialize_json(
                value["identity_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstanceSummary:
    out: InstanceSummary = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("Products") is not None:
        import capo_license_manager_user_subscriptions.types.string_list

        out["products"] = (
            capo_license_manager_user_subscriptions.types.string_list.deserialize_json(
                data["Products"]
            )
        )
    else:
        out["products"] = []
    if data.get("LastStatusCheckDate") is not None:
        out["last_status_check_date"] = data["LastStatusCheckDate"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    if data.get("IdentityProvider") is not None:
        import capo_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            capo_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    return out
