"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_step_errors
    import capo_deadline.types.batch_get_step_items


class BatchGetStepResponse(TypedDict, closed=True):
    steps: "capo_deadline.types.batch_get_step_items.BatchGetStepItems"
    """A list of steps that were successfully retrieved."""
    errors: "capo_deadline.types.batch_get_step_errors.BatchGetStepErrors"
    """A list of errors for steps that could not be retrieved."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_get_step_items

    out["steps"] = capo_deadline.types.batch_get_step_items.serialize_json(
        value["steps"]
    )
    import capo_deadline.types.batch_get_step_errors

    out["errors"] = capo_deadline.types.batch_get_step_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetStepResponse:
    out: BatchGetStepResponse = {}  # type: ignore[typeddict-item]
    if data.get("steps") is not None:
        import capo_deadline.types.batch_get_step_items

        out["steps"] = capo_deadline.types.batch_get_step_items.deserialize_json(
            data["steps"]
        )
    else:
        out["steps"] = []
    if data.get("errors") is not None:
        import capo_deadline.types.batch_get_step_errors

        out["errors"] = capo_deadline.types.batch_get_step_errors.deserialize_json(
            data["errors"]
        )
    else:
        out["errors"] = []
    return out


def redact_sensitive(value: BatchGetStepResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "steps" in value:
        import capo_deadline.types.batch_get_step_items

        out["steps"] = capo_deadline.types.batch_get_step_items.redact_sensitive(
            value["steps"]
        )
    return out
