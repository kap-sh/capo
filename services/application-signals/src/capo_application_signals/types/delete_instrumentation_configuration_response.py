"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DeleteInstrumentationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.dynamic_instrumentation_deletion_status


class DeleteInstrumentationConfigurationResponse(TypedDict, closed=True):
    deletion_status: "capo_application_signals.types.dynamic_instrumentation_deletion_status.DynamicInstrumentationDeletionStatus"
    """<p>The result of the delete request. The value is <code>DELETED</code> when the configuration has been removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInstrumentationConfigurationResponse) -> dict:
    out: dict = {}
    import capo_application_signals.types.dynamic_instrumentation_deletion_status

    out["DeletionStatus"] = (
        capo_application_signals.types.dynamic_instrumentation_deletion_status.serialize_json(
            value["deletion_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteInstrumentationConfigurationResponse:
    out: DeleteInstrumentationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("DeletionStatus") is not None:
        import capo_application_signals.types.dynamic_instrumentation_deletion_status

        out["deletion_status"] = (
            capo_application_signals.types.dynamic_instrumentation_deletion_status.deserialize_json(
                data["DeletionStatus"]
            )
        )
    else:
        import typing

        out["deletion_status"] = typing.cast(
            "capo_application_signals.types.dynamic_instrumentation_deletion_status.DynamicInstrumentationDeletionStatus",
            "",
        )
    return out
