"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ProductUserSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.arn
    import capo_license_manager_user_subscriptions.types.identity_provider


class ProductUserSummary(TypedDict, closed=True):
    username: "str"
    """<p>The user name from the identity provider for this product user.</p>"""
    product: "str"
    """<p>The name of the user-based subscription product.</p>"""
    identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>An object that specifies details for the identity provider.</p>"""
    status: "str"
    """<p>The status of a product for this user.</p>"""
    product_user_arn: NotRequired[
        "capo_license_manager_user_subscriptions.types.arn.Arn"
    ]
    """<p>The Amazon Resource Name (ARN) for this product user.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message for a product for this user.</p>"""
    domain: NotRequired["str"]
    """<p>The domain name of the Active Directory that contains the user information for the product subscription.</p>"""
    subscription_start_date: NotRequired["str"]
    """<p>The start date of a subscription.</p>"""
    subscription_end_date: NotRequired["str"]
    """<p>The end date of a subscription.</p>"""
    license_expiration_date: NotRequired["str"]
    """<p>The expiration date of the license associated with this subscription, in ISO 8601 UTC format (for example, <code>2025-03-15T00:00:00Z</code>).</p> <p>This field applies only to subscriptions that use license server endpoints, such as Remote Desktop Services (RDS) Subscriber Access License (SAL). It returns <code>null</code> for products that don't use license-based subscriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProductUserSummary) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["Product"] = value["product"]
    import capo_license_manager_user_subscriptions.types.identity_provider

    out["IdentityProvider"] = (
        capo_license_manager_user_subscriptions.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
    out["Status"] = value["status"]
    if "product_user_arn" in value:
        out["ProductUserArn"] = value["product_user_arn"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "subscription_start_date" in value:
        out["SubscriptionStartDate"] = value["subscription_start_date"]
    if "subscription_end_date" in value:
        out["SubscriptionEndDate"] = value["subscription_end_date"]
    if "license_expiration_date" in value:
        out["LicenseExpirationDate"] = value["license_expiration_date"]
    return out


def deserialize_json(data: dict) -> ProductUserSummary:
    out: ProductUserSummary = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    if data.get("Product") is not None:
        out["product"] = data["Product"]
    else:
        out["product"] = ""
    if data.get("IdentityProvider") is not None:
        import capo_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            capo_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    else:
        out["identity_provider"] = {"$unknown": {"name": ""}}
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("ProductUserArn") is not None:
        out["product_user_arn"] = data["ProductUserArn"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("SubscriptionStartDate") is not None:
        out["subscription_start_date"] = data["SubscriptionStartDate"]
    if data.get("SubscriptionEndDate") is not None:
        out["subscription_end_date"] = data["SubscriptionEndDate"]
    if data.get("LicenseExpirationDate") is not None:
        out["license_expiration_date"] = data["LicenseExpirationDate"]
    return out
