"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceQuickSightResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.space_quick_sight_resource_details
    import capo_quicksight.types.space_quick_sight_resource_type


class SpaceQuickSightResource(TypedDict, closed=True):
    resource_type: "capo_quicksight.types.space_quick_sight_resource_type.SpaceQuickSightResourceType"
    """<p>The type of the QuickSight resource.</p>"""
    resource_details: "capo_quicksight.types.space_quick_sight_resource_details.SpaceQuickSightResourceDetails"
    """<p>The details of the QuickSight resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceQuickSightResource) -> dict:
    out: dict = {}
    import capo_quicksight.types.space_quick_sight_resource_type

    out["resourceType"] = (
        capo_quicksight.types.space_quick_sight_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    import capo_quicksight.types.space_quick_sight_resource_details

    out["resourceDetails"] = (
        capo_quicksight.types.space_quick_sight_resource_details.serialize_json(
            value["resource_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> SpaceQuickSightResource:
    out: SpaceQuickSightResource = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_quicksight.types.space_quick_sight_resource_type

        out["resource_type"] = (
            capo_quicksight.types.space_quick_sight_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_quicksight.types.space_quick_sight_resource_type.SpaceQuickSightResourceType",
            "",
        )
    if data.get("resourceDetails") is not None:
        import capo_quicksight.types.space_quick_sight_resource_details

        out["resource_details"] = (
            capo_quicksight.types.space_quick_sight_resource_details.deserialize_json(
                data["resourceDetails"]
            )
        )
    else:
        out["resource_details"] = {"$unknown": {"name": ""}}
    return out
