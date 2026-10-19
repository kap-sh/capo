"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchDeleteInstrumentationConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.batch_delete_error_list
    import capo_application_signals.types.batch_delete_successful_deletion_list


class BatchDeleteInstrumentationConfigurationsResponse(TypedDict, closed=True):
    deleted_count: "int"
    """Number of configurations successfully deleted. When deleting by scope, this is the total count of deleted items. When deleting by ARN list, this equals the length of SuccessfulDeletions."""
    successful_deletions: "capo_application_signals.types.batch_delete_successful_deletion_list.BatchDeleteSuccessfulDeletionList"
    """List of successfully deleted configurations. Deleting by scope populates SignalType and LocationHash per item. Deleting by ARN list populates ResourceArn per item."""
    errors: (
        "capo_application_signals.types.batch_delete_error_list.BatchDeleteErrorList"
    )
    """List of configurations that failed to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteInstrumentationConfigurationsResponse) -> dict:
    out: dict = {}
    out["DeletedCount"] = value["deleted_count"]
    import capo_application_signals.types.batch_delete_successful_deletion_list

    out["SuccessfulDeletions"] = (
        capo_application_signals.types.batch_delete_successful_deletion_list.serialize_json(
            value["successful_deletions"]
        )
    )
    import capo_application_signals.types.batch_delete_error_list

    out["Errors"] = (
        capo_application_signals.types.batch_delete_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteInstrumentationConfigurationsResponse:
    out: BatchDeleteInstrumentationConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DeletedCount") is not None:
        out["deleted_count"] = data["DeletedCount"]
    else:
        out["deleted_count"] = 0
    if data.get("SuccessfulDeletions") is not None:
        import capo_application_signals.types.batch_delete_successful_deletion_list

        out["successful_deletions"] = (
            capo_application_signals.types.batch_delete_successful_deletion_list.deserialize_json(
                data["SuccessfulDeletions"]
            )
        )
    else:
        out["successful_deletions"] = []
    if data.get("Errors") is not None:
        import capo_application_signals.types.batch_delete_error_list

        out["errors"] = (
            capo_application_signals.types.batch_delete_error_list.deserialize_json(
                data["Errors"]
            )
        )
    else:
        out["errors"] = []
    return out
