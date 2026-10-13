"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobEntityResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_job_entity_errors
    import capo_deadline.types.batch_get_job_entity_list


class BatchGetJobEntityResponse(TypedDict, closed=True):
    entities: "capo_deadline.types.batch_get_job_entity_list.BatchGetJobEntityList"
    """<p>A list of the job entities, or details, in the batch.</p>"""
    errors: "capo_deadline.types.batch_get_job_entity_errors.BatchGetJobEntityErrors"
    """<p>A list of errors from the job error logs for the batch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobEntityResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_get_job_entity_list

    out["entities"] = capo_deadline.types.batch_get_job_entity_list.serialize_json(
        value["entities"]
    )
    import capo_deadline.types.batch_get_job_entity_errors

    out["errors"] = capo_deadline.types.batch_get_job_entity_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetJobEntityResponse:
    out: BatchGetJobEntityResponse = {}  # type: ignore[typeddict-item]
    if data.get("entities") is not None:
        import capo_deadline.types.batch_get_job_entity_list

        out["entities"] = (
            capo_deadline.types.batch_get_job_entity_list.deserialize_json(
                data["entities"]
            )
        )
    else:
        raise DeserializationError("BatchGetJobEntityResponse.entities required")
    if data.get("errors") is not None:
        import capo_deadline.types.batch_get_job_entity_errors

        out["errors"] = (
            capo_deadline.types.batch_get_job_entity_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchGetJobEntityResponse.errors required")
    return out


def redact_sensitive(value: BatchGetJobEntityResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entities" in value:
        import capo_deadline.types.batch_get_job_entity_list

        out["entities"] = (
            capo_deadline.types.batch_get_job_entity_list.redact_sensitive(
                value["entities"]
            )
        )
    return out
