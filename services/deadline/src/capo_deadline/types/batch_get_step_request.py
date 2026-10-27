"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_step_identifiers


class BatchGetStepRequest(TypedDict, closed=True):
    identifiers: (
        "capo_deadline.types.batch_get_step_identifiers.BatchGetStepIdentifiers"
    )
    """The list of step identifiers to retrieve. You can specify up to 100 identifiers per request."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_get_step_identifiers

    out["identifiers"] = capo_deadline.types.batch_get_step_identifiers.serialize_json(
        value["identifiers"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetStepRequest:
    out: BatchGetStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifiers") is not None:
        import capo_deadline.types.batch_get_step_identifiers

        out["identifiers"] = (
            capo_deadline.types.batch_get_step_identifiers.deserialize_json(
                data["identifiers"]
            )
        )
    else:
        out["identifiers"] = []
    return out
