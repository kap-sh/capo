"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureManagementGroupsQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_management_group_id


class AzureManagementGroupsQuery(TypedDict, closed=True):
    parent_management_group_id: NotRequired[
        "capo_observabilityadmin.types.azure_management_group_id.AzureManagementGroupId"
    ]
    """<p>Lists the management groups under this management group. If you omit this value, the query starts at the tenant root group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureManagementGroupsQuery) -> dict:
    out: dict = {}
    if "parent_management_group_id" in value:
        out["ParentManagementGroupId"] = value["parent_management_group_id"]
    return out


def deserialize_json(data: dict) -> AzureManagementGroupsQuery:
    out: AzureManagementGroupsQuery = {}  # type: ignore[typeddict-item]
    if data.get("ParentManagementGroupId") is not None:
        out["parent_management_group_id"] = data["ParentManagementGroupId"]
    return out
