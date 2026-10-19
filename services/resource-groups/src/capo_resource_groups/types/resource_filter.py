"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ResourceFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.resource_filter_name
    import capo_resource_groups.types.resource_filter_values


class ResourceFilter(TypedDict, closed=True):
    name: "capo_resource_groups.types.resource_filter_name.ResourceFilterName"
    """<p>The name of the filter. Filter names are case-sensitive.</p>"""
    values: "capo_resource_groups.types.resource_filter_values.ResourceFilterValues"
    """<p>One or more filter values. Allowed filter values vary by resource filter name, and are case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceFilter) -> dict:
    out: dict = {}
    import capo_resource_groups.types.resource_filter_name

    out["Name"] = capo_resource_groups.types.resource_filter_name.serialize_json(
        value["name"]
    )
    import capo_resource_groups.types.resource_filter_values

    out["Values"] = capo_resource_groups.types.resource_filter_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> ResourceFilter:
    out: ResourceFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_resource_groups.types.resource_filter_name

        out["name"] = capo_resource_groups.types.resource_filter_name.deserialize_json(
            data["Name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_resource_groups.types.resource_filter_name.ResourceFilterName", ""
        )
    if data.get("Values") is not None:
        import capo_resource_groups.types.resource_filter_values

        out["values"] = (
            capo_resource_groups.types.resource_filter_values.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
