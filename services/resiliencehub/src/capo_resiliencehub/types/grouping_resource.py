"""Generated from Smithy shape ``com.amazonaws.resiliencehub#GroupingResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.logical_resource_id
    import capo_resiliencehub.types.physical_resource_id
    import capo_resiliencehub.types.string255
    import capo_resiliencehub.types.string255_list


class GroupingResource(TypedDict, closed=True):
    resource_name: "capo_resiliencehub.types.string255.String255"
    """<p>Indicates the resource name.</p>"""
    resource_type: "capo_resiliencehub.types.string255.String255"
    """<p>Indicates the resource type.</p>"""
    physical_resource_id: (
        "capo_resiliencehub.types.physical_resource_id.PhysicalResourceId"
    )
    """<p>Indicates the physical identifier of the resource.</p>"""
    logical_resource_id: (
        "capo_resiliencehub.types.logical_resource_id.LogicalResourceId"
    )
    """<p>Indicates the logical identifier of the resource.</p>"""
    source_app_component_ids: "capo_resiliencehub.types.string255_list.String255List"
    """<p>Indicates the identifier of the source AppComponents in which the resources were previously grouped into.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupingResource) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    out["resourceType"] = value["resource_type"]
    import capo_resiliencehub.types.physical_resource_id

    out["physicalResourceId"] = (
        capo_resiliencehub.types.physical_resource_id.serialize_json(
            value["physical_resource_id"]
        )
    )
    import capo_resiliencehub.types.logical_resource_id

    out["logicalResourceId"] = (
        capo_resiliencehub.types.logical_resource_id.serialize_json(
            value["logical_resource_id"]
        )
    )
    import capo_resiliencehub.types.string255_list

    out["sourceAppComponentIds"] = (
        capo_resiliencehub.types.string255_list.serialize_json(
            value["source_app_component_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> GroupingResource:
    out: GroupingResource = {}  # type: ignore[typeddict-item]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    else:
        out["resource_name"] = ""
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("physicalResourceId") is not None:
        import capo_resiliencehub.types.physical_resource_id

        out["physical_resource_id"] = (
            capo_resiliencehub.types.physical_resource_id.deserialize_json(
                data["physicalResourceId"]
            )
        )
    else:
        raise DeserializationError("GroupingResource.physical_resource_id required")
    if data.get("logicalResourceId") is not None:
        import capo_resiliencehub.types.logical_resource_id

        out["logical_resource_id"] = (
            capo_resiliencehub.types.logical_resource_id.deserialize_json(
                data["logicalResourceId"]
            )
        )
    else:
        raise DeserializationError("GroupingResource.logical_resource_id required")
    if data.get("sourceAppComponentIds") is not None:
        import capo_resiliencehub.types.string255_list

        out["source_app_component_ids"] = (
            capo_resiliencehub.types.string255_list.deserialize_json(
                data["sourceAppComponentIds"]
            )
        )
    else:
        out["source_app_component_ids"] = []
    return out
