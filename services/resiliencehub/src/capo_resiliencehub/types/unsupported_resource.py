"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UnsupportedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.logical_resource_id
    import capo_resiliencehub.types.physical_resource_id
    import capo_resiliencehub.types.string255


class UnsupportedResource(TypedDict, closed=True):
    logical_resource_id: (
        "capo_resiliencehub.types.logical_resource_id.LogicalResourceId"
    )
    """<p>Logical resource identifier for the unsupported resource.</p>"""
    physical_resource_id: (
        "capo_resiliencehub.types.physical_resource_id.PhysicalResourceId"
    )
    """<p>Physical resource identifier for the unsupported resource.</p>"""
    resource_type: "capo_resiliencehub.types.string255.String255"
    """<p>The type of resource.</p>"""
    unsupported_resource_status: NotRequired[
        "capo_resiliencehub.types.string255.String255"
    ]
    """<p>The status of the unsupported resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedResource) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.logical_resource_id

    out["logicalResourceId"] = (
        capo_resiliencehub.types.logical_resource_id.serialize_json(
            value["logical_resource_id"]
        )
    )
    import capo_resiliencehub.types.physical_resource_id

    out["physicalResourceId"] = (
        capo_resiliencehub.types.physical_resource_id.serialize_json(
            value["physical_resource_id"]
        )
    )
    out["resourceType"] = value["resource_type"]
    if "unsupported_resource_status" in value:
        out["unsupportedResourceStatus"] = value["unsupported_resource_status"]
    return out


def deserialize_json(data: dict) -> UnsupportedResource:
    out: UnsupportedResource = {}  # type: ignore[typeddict-item]
    if data.get("logicalResourceId") is not None:
        import capo_resiliencehub.types.logical_resource_id

        out["logical_resource_id"] = (
            capo_resiliencehub.types.logical_resource_id.deserialize_json(
                data["logicalResourceId"]
            )
        )
    else:
        raise DeserializationError("UnsupportedResource.logical_resource_id required")
    if data.get("physicalResourceId") is not None:
        import capo_resiliencehub.types.physical_resource_id

        out["physical_resource_id"] = (
            capo_resiliencehub.types.physical_resource_id.deserialize_json(
                data["physicalResourceId"]
            )
        )
    else:
        raise DeserializationError("UnsupportedResource.physical_resource_id required")
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("unsupportedResourceStatus") is not None:
        out["unsupported_resource_status"] = data["unsupportedResourceStatus"]
    return out
