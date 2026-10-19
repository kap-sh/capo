"""Generated from Smithy shape ``com.amazonaws.repostspace#BatchRemoveRoleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.accessor_id_list
    import capo_repostspace.types.batch_error_list


class BatchRemoveRoleOutput(TypedDict, closed=True):
    removed_accessor_ids: "capo_repostspace.types.accessor_id_list.AccessorIdList"
    """<p>An array of successfully updated accessor identifiers.</p>"""
    errors: "capo_repostspace.types.batch_error_list.BatchErrorList"
    """<p>An array of errors that occurred when roles were removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRemoveRoleOutput) -> dict:
    out: dict = {}
    import capo_repostspace.types.accessor_id_list

    out["removedAccessorIds"] = capo_repostspace.types.accessor_id_list.serialize_json(
        value["removed_accessor_ids"]
    )
    import capo_repostspace.types.batch_error_list

    out["errors"] = capo_repostspace.types.batch_error_list.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchRemoveRoleOutput:
    out: BatchRemoveRoleOutput = {}  # type: ignore[typeddict-item]
    if data.get("removedAccessorIds") is not None:
        import capo_repostspace.types.accessor_id_list

        out["removed_accessor_ids"] = (
            capo_repostspace.types.accessor_id_list.deserialize_json(
                data["removedAccessorIds"]
            )
        )
    else:
        out["removed_accessor_ids"] = []
    if data.get("errors") is not None:
        import capo_repostspace.types.batch_error_list

        out["errors"] = capo_repostspace.types.batch_error_list.deserialize_json(
            data["errors"]
        )
    else:
        out["errors"] = []
    return out
