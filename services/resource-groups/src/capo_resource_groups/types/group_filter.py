"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_filter_name
    import capo_resource_groups.types.group_filter_values


class GroupFilter(TypedDict, closed=True):
    name: "capo_resource_groups.types.group_filter_name.GroupFilterName"
    """<p>The name of the filter. Filter names are case-sensitive.</p>"""
    values: "capo_resource_groups.types.group_filter_values.GroupFilterValues"
    """<p>One or more filter values. Allowed filter values vary by group filter name, and are case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupFilter) -> dict:
    out: dict = {}
    import capo_resource_groups.types.group_filter_name

    out["Name"] = capo_resource_groups.types.group_filter_name.serialize_json(
        value["name"]
    )
    import capo_resource_groups.types.group_filter_values

    out["Values"] = capo_resource_groups.types.group_filter_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> GroupFilter:
    out: GroupFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_resource_groups.types.group_filter_name

        out["name"] = capo_resource_groups.types.group_filter_name.deserialize_json(
            data["Name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_resource_groups.types.group_filter_name.GroupFilterName", ""
        )
    if data.get("Values") is not None:
        import capo_resource_groups.types.group_filter_values

        out["values"] = capo_resource_groups.types.group_filter_values.deserialize_json(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
