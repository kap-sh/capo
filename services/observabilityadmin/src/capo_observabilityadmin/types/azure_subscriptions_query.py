"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureSubscriptionsQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_management_group_id


class AzureSubscriptionsQuery(TypedDict, closed=True):
    management_group_id: NotRequired[
        "capo_observabilityadmin.types.azure_management_group_id.AzureManagementGroupId"
    ]
    """<p>Limits the results to subscriptions under this management group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureSubscriptionsQuery) -> dict:
    out: dict = {}
    if "management_group_id" in value:
        out["ManagementGroupId"] = value["management_group_id"]
    return out


def deserialize_json(data: dict) -> AzureSubscriptionsQuery:
    out: AzureSubscriptionsQuery = {}  # type: ignore[typeddict-item]
    if data.get("ManagementGroupId") is not None:
        out["management_group_id"] = data["ManagementGroupId"]
    return out
