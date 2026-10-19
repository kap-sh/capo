"""Generated from Smithy shape ``com.amazonaws.repostspace#BatchRemoveRoleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.accessor_id_list
    import capo_repostspace.types.role
    import capo_repostspace.types.space_id


class BatchRemoveRoleInput(TypedDict, closed=True):
    space_id: "capo_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""
    accessor_ids: "capo_repostspace.types.accessor_id_list.AccessorIdList"
    """<p>The user or group accessor identifiers to remove the role from.</p>"""
    role: "capo_repostspace.types.role.Role"
    """<p>The role to remove from the users or groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRemoveRoleInput) -> dict:
    out: dict = {}
    import capo_repostspace.types.accessor_id_list

    out["accessorIds"] = capo_repostspace.types.accessor_id_list.serialize_json(
        value["accessor_ids"]
    )
    import capo_repostspace.types.role

    out["role"] = capo_repostspace.types.role.serialize_json(value["role"])
    return out


def deserialize_json(data: dict) -> BatchRemoveRoleInput:
    out: BatchRemoveRoleInput = {}  # type: ignore[typeddict-item]
    if data.get("accessorIds") is not None:
        import capo_repostspace.types.accessor_id_list

        out["accessor_ids"] = capo_repostspace.types.accessor_id_list.deserialize_json(
            data["accessorIds"]
        )
    else:
        out["accessor_ids"] = []
    if data.get("role") is not None:
        import capo_repostspace.types.role

        out["role"] = capo_repostspace.types.role.deserialize_json(data["role"])
    else:
        import typing

        out["role"] = typing.cast("capo_repostspace.types.role.Role", "")
    return out
