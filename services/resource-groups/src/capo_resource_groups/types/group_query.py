"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resource_groups.types.group_name
    import capo_resource_groups.types.resource_query


class GroupQuery(TypedDict, closed=True):
    group_name: "capo_resource_groups.types.group_name.GroupName"
    """<p>The name of the resource group that is associated with the specified resource query.</p>"""
    resource_query: "capo_resource_groups.types.resource_query.ResourceQuery"
    """<p>The resource query that determines which Amazon Web Services resources are members of the associated resource group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupQuery) -> dict:
    out: dict = {}
    out["GroupName"] = value["group_name"]
    import capo_resource_groups.types.resource_query

    out["ResourceQuery"] = capo_resource_groups.types.resource_query.serialize_json(
        value["resource_query"]
    )
    return out


def deserialize_json(data: dict) -> GroupQuery:
    out: GroupQuery = {}  # type: ignore[typeddict-item]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    else:
        out["group_name"] = ""
    if data.get("ResourceQuery") is not None:
        import capo_resource_groups.types.resource_query

        out["resource_query"] = (
            capo_resource_groups.types.resource_query.deserialize_json(
                data["ResourceQuery"]
            )
        )
    else:
        raise DeserializationError("GroupQuery.resource_query required")
    return out
