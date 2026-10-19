"""Generated from Smithy shape ``com.amazonaws.lambda#StopDurableExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.execution_timestamp


class StopDurableExecutionResponse(TypedDict, closed=True):
    stop_timestamp: "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    """<p>The timestamp when the execution was stopped (ISO 8601 format).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopDurableExecutionResponse) -> dict:
    out: dict = {}
    import capo_lambda.types.execution_timestamp

    out["StopTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
        value["stop_timestamp"]
    )
    return out


def deserialize_json(data: dict) -> StopDurableExecutionResponse:
    out: StopDurableExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("StopTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["stop_timestamp"] = capo_lambda.types.execution_timestamp.deserialize_json(
            data["StopTimestamp"]
        )
    else:
        import datetime

        out["stop_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
