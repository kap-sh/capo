"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListMonitoredResourcesFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.resource_permission
    import capo_devops_guru.types.resource_type_filters


class ListMonitoredResourcesFilters(TypedDict, closed=True):
    resource_permission: "capo_devops_guru.types.resource_permission.ResourcePermission"
    """<p> The permission status of a resource. </p>"""
    resource_type_filters: (
        "capo_devops_guru.types.resource_type_filters.ResourceTypeFilters"
    )
    """<p> The type of resource that you wish to retrieve, such as log groups. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMonitoredResourcesFilters) -> dict:
    out: dict = {}
    import capo_devops_guru.types.resource_permission

    out["ResourcePermission"] = (
        capo_devops_guru.types.resource_permission.serialize_json(
            value["resource_permission"]
        )
    )
    import capo_devops_guru.types.resource_type_filters

    out["ResourceTypeFilters"] = (
        capo_devops_guru.types.resource_type_filters.serialize_json(
            value["resource_type_filters"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListMonitoredResourcesFilters:
    out: ListMonitoredResourcesFilters = {}  # type: ignore[typeddict-item]
    if data.get("ResourcePermission") is not None:
        import capo_devops_guru.types.resource_permission

        out["resource_permission"] = (
            capo_devops_guru.types.resource_permission.deserialize_json(
                data["ResourcePermission"]
            )
        )
    else:
        import typing

        out["resource_permission"] = typing.cast(
            "capo_devops_guru.types.resource_permission.ResourcePermission", ""
        )
    if data.get("ResourceTypeFilters") is not None:
        import capo_devops_guru.types.resource_type_filters

        out["resource_type_filters"] = (
            capo_devops_guru.types.resource_type_filters.deserialize_json(
                data["ResourceTypeFilters"]
            )
        )
    else:
        out["resource_type_filters"] = []
    return out
