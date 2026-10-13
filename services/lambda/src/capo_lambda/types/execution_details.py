"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.input_payload


class ExecutionDetails(TypedDict, closed=True):
    input_payload: NotRequired["capo_lambda.types.input_payload.InputPayload"]
    """<p>The original input payload provided for the durable execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionDetails) -> dict:
    out: dict = {}
    if "input_payload" in value:
        out["InputPayload"] = value["input_payload"]
    return out


def deserialize_json(data: dict) -> ExecutionDetails:
    out: ExecutionDetails = {}  # type: ignore[typeddict-item]
    if data.get("InputPayload") is not None:
        out["input_payload"] = data["InputPayload"]
    return out


def redact_sensitive(value: ExecutionDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_payload" in value:
        out["input_payload"] = "*** Sensitive Data Redacted ***"
    return out
