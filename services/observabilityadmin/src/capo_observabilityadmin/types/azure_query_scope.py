"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureQueryScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_management_group_id
    import capo_observabilityadmin.types.azure_subscription_id_list


class AzureQueryScope(TypedDict, closed=True):
    management_group_id: NotRequired[
        "capo_observabilityadmin.types.azure_management_group_id.AzureManagementGroupId"
    ]
    """<p>Limits the query to resources under this management group.</p>"""
    subscription_ids: NotRequired[
        "capo_observabilityadmin.types.azure_subscription_id_list.AzureSubscriptionIdList"
    ]
    """<p>Limits the query to these subscriptions. You can specify 1–1000 subscriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureQueryScope) -> dict:
    out: dict = {}
    if "management_group_id" in value:
        out["ManagementGroupId"] = value["management_group_id"]
    if "subscription_ids" in value:
        import capo_observabilityadmin.types.azure_subscription_id_list

        out["SubscriptionIds"] = (
            capo_observabilityadmin.types.azure_subscription_id_list.serialize_json(
                value["subscription_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> AzureQueryScope:
    out: AzureQueryScope = {}  # type: ignore[typeddict-item]
    if data.get("ManagementGroupId") is not None:
        out["management_group_id"] = data["ManagementGroupId"]
    if data.get("SubscriptionIds") is not None:
        import capo_observabilityadmin.types.azure_subscription_id_list

        out["subscription_ids"] = (
            capo_observabilityadmin.types.azure_subscription_id_list.deserialize_json(
                data["SubscriptionIds"]
            )
        )
    return out
