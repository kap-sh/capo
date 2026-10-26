"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.space_quick_sight_resource_details
    import capo_quicksight.types.space_quick_sight_resource_type


class SpaceResourceSummary(TypedDict, closed=True):
    resource_type: "capo_quicksight.types.space_quick_sight_resource_type.SpaceQuickSightResourceType"
    """<p>The type of the resource.</p>"""
    resource_details: "capo_quicksight.types.space_quick_sight_resource_details.SpaceQuickSightResourceDetails"
    """<p>The details of the resource.</p>"""
    resource_name: NotRequired["str"]
    """<p>The name of the resource.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the resource was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceResourceSummary) -> dict:
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
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    if "updated_at" in value:
        import capo_quicksight.types._prelude.timestamp

        out["UpdatedAt"] = capo_quicksight.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> SpaceResourceSummary:
    out: SpaceResourceSummary = {}  # type: ignore[typeddict-item]
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
        out["resource_details"] = {"$unknown": {"name": ""}}
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    if data.get("UpdatedAt") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["updated_at"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
