"""Generated from Smithy shape ``com.amazonaws.lambda#CallbackSucceededDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.event_result


class CallbackSucceededDetails(TypedDict, closed=True):
    result: "capo_lambda.types.event_result.EventResult"
    """<p>The response payload from the successful operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CallbackSucceededDetails) -> dict:
    out: dict = {}
    import capo_lambda.types.event_result

    out["Result"] = capo_lambda.types.event_result.serialize_json(value["result"])
    return out


def deserialize_json(data: dict) -> CallbackSucceededDetails:
    out: CallbackSucceededDetails = {}  # type: ignore[typeddict-item]
    if data.get("Result") is not None:
        import capo_lambda.types.event_result

        out["result"] = capo_lambda.types.event_result.deserialize_json(data["Result"])
    else:
        raise DeserializationError("CallbackSucceededDetails.result required")
    return out


def redact_sensitive(value: CallbackSucceededDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "result" in value:
        import capo_lambda.types.event_result

        out["result"] = capo_lambda.types.event_result.redact_sensitive(value["result"])
    return out
