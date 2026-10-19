"""Generated from Smithy shape ``com.amazonaws.entityresolution#BatchDeleteUniqueIdOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.delete_unique_id_errors_list
    import capo_entityresolution.types.delete_unique_id_status
    import capo_entityresolution.types.deleted_unique_id_list
    import capo_entityresolution.types.disconnected_unique_ids_list


class BatchDeleteUniqueIdOutput(TypedDict, closed=True):
    status: "capo_entityresolution.types.delete_unique_id_status.DeleteUniqueIdStatus"
    """<p>The status of the batch delete unique ID operation.</p>"""
    errors: "capo_entityresolution.types.delete_unique_id_errors_list.DeleteUniqueIdErrorsList"
    """<p> The errors from deleting multiple unique IDs.</p>"""
    deleted: "capo_entityresolution.types.deleted_unique_id_list.DeletedUniqueIdList"
    """<p>The unique IDs that were deleted.</p>"""
    disconnected_unique_ids: "capo_entityresolution.types.disconnected_unique_ids_list.DisconnectedUniqueIdsList"
    """<p>The unique IDs that were disconnected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteUniqueIdOutput) -> dict:
    out: dict = {}
    import capo_entityresolution.types.delete_unique_id_status

    out["status"] = capo_entityresolution.types.delete_unique_id_status.serialize_json(
        value["status"]
    )
    import capo_entityresolution.types.delete_unique_id_errors_list

    out["errors"] = (
        capo_entityresolution.types.delete_unique_id_errors_list.serialize_json(
            value["errors"]
        )
    )
    import capo_entityresolution.types.deleted_unique_id_list

    out["deleted"] = capo_entityresolution.types.deleted_unique_id_list.serialize_json(
        value["deleted"]
    )
    import capo_entityresolution.types.disconnected_unique_ids_list

    out["disconnectedUniqueIds"] = (
        capo_entityresolution.types.disconnected_unique_ids_list.serialize_json(
            value["disconnected_unique_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteUniqueIdOutput:
    out: BatchDeleteUniqueIdOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_entityresolution.types.delete_unique_id_status

        out["status"] = (
            capo_entityresolution.types.delete_unique_id_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_entityresolution.types.delete_unique_id_status.DeleteUniqueIdStatus",
            "",
        )
    if data.get("errors") is not None:
        import capo_entityresolution.types.delete_unique_id_errors_list

        out["errors"] = (
            capo_entityresolution.types.delete_unique_id_errors_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    if data.get("deleted") is not None:
        import capo_entityresolution.types.deleted_unique_id_list

        out["deleted"] = (
            capo_entityresolution.types.deleted_unique_id_list.deserialize_json(
                data["deleted"]
            )
        )
    else:
        out["deleted"] = []
    if data.get("disconnectedUniqueIds") is not None:
        import capo_entityresolution.types.disconnected_unique_ids_list

        out["disconnected_unique_ids"] = (
            capo_entityresolution.types.disconnected_unique_ids_list.deserialize_json(
                data["disconnectedUniqueIds"]
            )
        )
    else:
        out["disconnected_unique_ids"] = []
    return out
