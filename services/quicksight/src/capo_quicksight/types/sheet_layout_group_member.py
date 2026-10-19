"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetLayoutGroupMember``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_layout_group_member_type
    import capo_quicksight.types.short_restrictive_resource_id


class SheetLayoutGroupMember(TypedDict, closed=True):
    id: "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier of the group member.</p>"""
    type: "capo_quicksight.types.sheet_layout_group_member_type.SheetLayoutGroupMemberType"
    """<p>The type of the group member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetLayoutGroupMember) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_quicksight.types.sheet_layout_group_member_type

    out["Type"] = capo_quicksight.types.sheet_layout_group_member_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> SheetLayoutGroupMember:
    out: SheetLayoutGroupMember = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Type") is not None:
        import capo_quicksight.types.sheet_layout_group_member_type

        out["type"] = (
            capo_quicksight.types.sheet_layout_group_member_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_quicksight.types.sheet_layout_group_member_type.SheetLayoutGroupMemberType",
            "",
        )
    return out
