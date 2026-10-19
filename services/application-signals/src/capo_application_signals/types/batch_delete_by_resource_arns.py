"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchDeleteByResourceArns``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.batch_delete_resource_arn_list
    import capo_application_signals.types.instrumentation_type


class BatchDeleteByResourceArns(TypedDict, closed=True):
    resource_arns: "capo_application_signals.types.batch_delete_resource_arn_list.BatchDeleteResourceArnList"
    """List of resource ARNs to delete."""
    instrumentation_type: (
        "capo_application_signals.types.instrumentation_type.InstrumentationType"
    )
    """Instrumentation type: BREAKPOINT or PROBE."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteByResourceArns) -> dict:
    out: dict = {}
    import capo_application_signals.types.batch_delete_resource_arn_list

    out["ResourceArns"] = (
        capo_application_signals.types.batch_delete_resource_arn_list.serialize_json(
            value["resource_arns"]
        )
    )
    import capo_application_signals.types.instrumentation_type

    out["InstrumentationType"] = (
        capo_application_signals.types.instrumentation_type.serialize_json(
            value["instrumentation_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteByResourceArns:
    out: BatchDeleteByResourceArns = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArns") is not None:
        import capo_application_signals.types.batch_delete_resource_arn_list

        out["resource_arns"] = (
            capo_application_signals.types.batch_delete_resource_arn_list.deserialize_json(
                data["ResourceArns"]
            )
        )
    else:
        out["resource_arns"] = []
    if data.get("InstrumentationType") is not None:
        import capo_application_signals.types.instrumentation_type

        out["instrumentation_type"] = (
            capo_application_signals.types.instrumentation_type.deserialize_json(
                data["InstrumentationType"]
            )
        )
    else:
        import typing

        out["instrumentation_type"] = typing.cast(
            "capo_application_signals.types.instrumentation_type.InstrumentationType",
            "",
        )
    return out
