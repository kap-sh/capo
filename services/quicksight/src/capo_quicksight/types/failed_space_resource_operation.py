"""Generated from Smithy shape ``com.amazonaws.quicksight#FailedSpaceResourceOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.space_quick_sight_resource_details
    import capo_quicksight.types.space_quick_sight_resource_type


class FailedSpaceResourceOperation(TypedDict, closed=True):
    resource_type: "capo_quicksight.types.space_quick_sight_resource_type.SpaceQuickSightResourceType"
    """<p>The type of the resource.</p>"""
    resource_details: NotRequired[
        "capo_quicksight.types.space_quick_sight_resource_details.SpaceQuickSightResourceDetails"
    ]
    """<p>The details of the resource.</p>"""
    error_message: "str"
    """<p>The error message that describes why the operation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedSpaceResourceOperation) -> dict:
    out: dict = {}
    import capo_quicksight.types.space_quick_sight_resource_type

    out["ResourceType"] = (
        capo_quicksight.types.space_quick_sight_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    if "resource_details" in value:
        import capo_quicksight.types.space_quick_sight_resource_details

        out["ResourceDetails"] = (
            capo_quicksight.types.space_quick_sight_resource_details.serialize_json(
                value["resource_details"]
            )
        )
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedSpaceResourceOperation:
    out: FailedSpaceResourceOperation = {}  # type: ignore[typeddict-item]
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
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    else:
        out["error_message"] = ""
    return out
