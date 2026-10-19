"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetAddonSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.addon_subscription_id


class GetAddonSubscriptionRequest(TypedDict, closed=True):
    addon_subscription_id: (
        "capo_mailmanager.types.addon_subscription_id.AddonSubscriptionId"
    )
    """<p>The Add On subscription ID to retrieve information for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAddonSubscriptionRequest) -> dict:
    out: dict = {}
    out["AddonSubscriptionId"] = value["addon_subscription_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAddonSubscriptionRequest:
    out: GetAddonSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AddonSubscriptionId") is not None:
        out["addon_subscription_id"] = data["AddonSubscriptionId"]
    else:
        out["addon_subscription_id"] = ""
    return out
