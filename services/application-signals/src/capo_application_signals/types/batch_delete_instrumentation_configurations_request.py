"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchDeleteInstrumentationConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.batch_delete_deletion_target


class BatchDeleteInstrumentationConfigurationsRequest(TypedDict, closed=True):
    deletion_target: "capo_application_signals.types.batch_delete_deletion_target.BatchDeleteDeletionTarget"
    """The deletion target - either bulk by scope or targeted by ARN list."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteInstrumentationConfigurationsRequest) -> dict:
    out: dict = {}
    import capo_application_signals.types.batch_delete_deletion_target

    out["DeletionTarget"] = (
        capo_application_signals.types.batch_delete_deletion_target.serialize_json(
            value["deletion_target"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteInstrumentationConfigurationsRequest:
    out: BatchDeleteInstrumentationConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeletionTarget") is not None:
        import capo_application_signals.types.batch_delete_deletion_target

        out["deletion_target"] = (
            capo_application_signals.types.batch_delete_deletion_target.deserialize_json(
                data["DeletionTarget"]
            )
        )
    else:
        out["deletion_target"] = {"$unknown": {"name": ""}}
    return out
