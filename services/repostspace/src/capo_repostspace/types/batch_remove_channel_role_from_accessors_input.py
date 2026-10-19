"""Generated from Smithy shape ``com.amazonaws.repostspace#BatchRemoveChannelRoleFromAccessorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.accessor_id_list
    import capo_repostspace.types.channel_id
    import capo_repostspace.types.channel_role
    import capo_repostspace.types.space_id


class BatchRemoveChannelRoleFromAccessorsInput(TypedDict, closed=True):
    space_id: "capo_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""
    channel_id: "capo_repostspace.types.channel_id.ChannelId"
    """<p>The unique ID of the private re:Post channel.</p>"""
    accessor_ids: "capo_repostspace.types.accessor_id_list.AccessorIdList"
    """<p>The users or groups identifiers to remove the role from.</p>"""
    channel_role: "capo_repostspace.types.channel_role.ChannelRole"
    """<p>The channel role to remove from the users or groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRemoveChannelRoleFromAccessorsInput) -> dict:
    out: dict = {}
    import capo_repostspace.types.accessor_id_list

    out["accessorIds"] = capo_repostspace.types.accessor_id_list.serialize_json(
        value["accessor_ids"]
    )
    import capo_repostspace.types.channel_role

    out["channelRole"] = capo_repostspace.types.channel_role.serialize_json(
        value["channel_role"]
    )
    return out


def deserialize_json(data: dict) -> BatchRemoveChannelRoleFromAccessorsInput:
    out: BatchRemoveChannelRoleFromAccessorsInput = {}  # type: ignore[typeddict-item]
    if data.get("accessorIds") is not None:
        import capo_repostspace.types.accessor_id_list

        out["accessor_ids"] = capo_repostspace.types.accessor_id_list.deserialize_json(
            data["accessorIds"]
        )
    else:
        out["accessor_ids"] = []
    if data.get("channelRole") is not None:
        import capo_repostspace.types.channel_role

        out["channel_role"] = capo_repostspace.types.channel_role.deserialize_json(
            data["channelRole"]
        )
    else:
        import typing

        out["channel_role"] = typing.cast(
            "capo_repostspace.types.channel_role.ChannelRole", ""
        )
    return out
