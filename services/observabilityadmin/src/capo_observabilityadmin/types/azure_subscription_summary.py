"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureSubscriptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_management_group_id
    import capo_observabilityadmin.types.azure_subscription_id


class AzureSubscriptionSummary(TypedDict, closed=True):
    subscription_id: (
        "capo_observabilityadmin.types.azure_subscription_id.AzureSubscriptionId"
    )
    """<p>The ID of the subscription.</p>"""
    display_name: NotRequired["str"]
    """<p>The display name of the subscription.</p>"""
    state: NotRequired["str"]
    """<p>The state of the subscription in Azure, for example <code>Enabled</code>.</p>"""
    management_group_id: NotRequired[
        "capo_observabilityadmin.types.azure_management_group_id.AzureManagementGroupId"
    ]
    """<p>The ID of the management group that contains the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureSubscriptionSummary) -> dict:
    out: dict = {}
    out["SubscriptionId"] = value["subscription_id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "state" in value:
        out["State"] = value["state"]
    if "management_group_id" in value:
        out["ManagementGroupId"] = value["management_group_id"]
    return out


def deserialize_json(data: dict) -> AzureSubscriptionSummary:
    out: AzureSubscriptionSummary = {}  # type: ignore[typeddict-item]
    if data.get("SubscriptionId") is not None:
        out["subscription_id"] = data["SubscriptionId"]
    else:
        out["subscription_id"] = ""
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("ManagementGroupId") is not None:
        out["management_group_id"] = data["ManagementGroupId"]
    return out
