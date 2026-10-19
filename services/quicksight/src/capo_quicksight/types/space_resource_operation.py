"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceResourceOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.space_quick_sight_resource_details
    import capo_quicksight.types.space_quick_sight_resource_type


class SpaceResourceOperation(TypedDict, closed=True):
    resource_type: "capo_quicksight.types.space_quick_sight_resource_type.SpaceQuickSightResourceType"
    """<p>The type of the resource.</p>"""
    resource_details: "capo_quicksight.types.space_quick_sight_resource_details.SpaceQuickSightResourceDetails"
    """<p>The details of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceResourceOperation) -> dict:
    out: dict = {}
    import capo_quicksight.types.space_quick_sight_resource_type

    out["ResourceType"] = (
        capo_quicksight.types.space_quick_sight_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    import capo_quicksight.types.space_quick_sight_resource_details

    out["ResourceDetails"] = (
        capo_quicksight.types.space_quick_sight_resource_details.serialize_json(
            value["resource_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> SpaceResourceOperation:
    out: SpaceResourceOperation = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        import capo_quicksight.types.space_quick_sight_resource_type

        out["resource_type"] = (
            capo_quicksight.types.space_quick_sight_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_quicksight.types.space_quick_sight_resource_type.SpaceQuickSightResourceType",
            "",
        )
    if data.get("ResourceDetails") is not None:
        import capo_quicksight.types.space_quick_sight_resource_details

        out["resource_details"] = (
            capo_quicksight.types.space_quick_sight_resource_details.deserialize_json(
                data["ResourceDetails"]
            )
        )
    else:
        import capo_quicksight.types._unknown

        out["resource_details"] = capo_quicksight.types._unknown.UnknownUnionMember("")
    return out
