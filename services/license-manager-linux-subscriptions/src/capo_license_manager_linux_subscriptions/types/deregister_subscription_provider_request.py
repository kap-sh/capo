"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#DeregisterSubscriptionProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager_linux_subscriptions.types.subscription_provider_arn


class DeregisterSubscriptionProviderRequest(TypedDict, closed=True):
    subscription_provider_arn: "capo_license_manager_linux_subscriptions.types.subscription_provider_arn.SubscriptionProviderArn"
    """<p>The Amazon Resource Name (ARN) of the subscription provider resource to deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterSubscriptionProviderRequest) -> dict:
    out: dict = {}
    out["SubscriptionProviderArn"] = value["subscription_provider_arn"]
    return out


def deserialize_json(data: dict) -> DeregisterSubscriptionProviderRequest:
    out: DeregisterSubscriptionProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubscriptionProviderArn") is not None:
        out["subscription_provider_arn"] = data["SubscriptionProviderArn"]
    else:
        out["subscription_provider_arn"] = ""
    return out
