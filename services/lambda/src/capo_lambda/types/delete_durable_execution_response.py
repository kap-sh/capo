"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteDurableExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.execution_timestamp


class DeleteDurableExecutionResponse(TypedDict, closed=True):
    deletion_request_timestamp: (
        "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    )
    """<p>The timestamp when Lambda accepted the deletion request (ISO 8601 format).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDurableExecutionResponse) -> dict:
    out: dict = {}
    import capo_lambda.types.execution_timestamp

    out["DeletionRequestTimestamp"] = (
        capo_lambda.types.execution_timestamp.serialize_json(
            value["deletion_request_timestamp"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteDurableExecutionResponse:
    out: DeleteDurableExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("DeletionRequestTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["deletion_request_timestamp"] = (
            capo_lambda.types.execution_timestamp.deserialize_json(
                data["DeletionRequestTimestamp"]
            )
        )
    else:
        import datetime

        out["deletion_request_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
