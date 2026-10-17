"""Generated from Smithy shape ``com.amazonaws.lambdaweb#FunctionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.date_time
    import capo_lambda_web.types.function_arn
    import capo_lambda_web.types.function_name
    import capo_lambda_web.types.function_state


class FunctionSummary(TypedDict, closed=True):
    function_name: "capo_lambda_web.types.function_name.FunctionName"
    """<p>The name of the web function.</p>"""
    function_arn: "capo_lambda_web.types.function_arn.FunctionArn"
    """<p>The Amazon Resource Name (ARN) of the web function.</p>"""
    state: "capo_lambda_web.types.function_state.FunctionState"
    """<p>The current state of the web function.</p>"""
    state_reason: "str"
    """<p>The reason for the current state of the web function.</p>"""
    created_at: "capo_lambda_web.types.date_time.DateTime"
    """<p>The date and time the web function was created.</p>"""
    updated_at: "capo_lambda_web.types.date_time.DateTime"
    """<p>The date and time the web function was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionSummary) -> dict:
    out: dict = {}
    out["functionName"] = value["function_name"]
    out["functionArn"] = value["function_arn"]
    import capo_lambda_web.types.function_state

    out["state"] = capo_lambda_web.types.function_state.serialize_json(value["state"])
    out["stateReason"] = value["state_reason"]
    import capo_lambda_web.types.date_time

    out["createdAt"] = capo_lambda_web.types.date_time.serialize_json(
        value["created_at"]
    )
    import capo_lambda_web.types.date_time

    out["updatedAt"] = capo_lambda_web.types.date_time.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> FunctionSummary:
    out: FunctionSummary = {}  # type: ignore[typeddict-item]
    if data.get("functionName") is not None:
        out["function_name"] = data["functionName"]
    else:
        raise DeserializationError("FunctionSummary.function_name required")
    if data.get("functionArn") is not None:
        out["function_arn"] = data["functionArn"]
    else:
        raise DeserializationError("FunctionSummary.function_arn required")
    if data.get("state") is not None:
        import capo_lambda_web.types.function_state

        out["state"] = capo_lambda_web.types.function_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("FunctionSummary.state required")
    if data.get("stateReason") is not None:
        out["state_reason"] = data["stateReason"]
    else:
        raise DeserializationError("FunctionSummary.state_reason required")
    if data.get("createdAt") is not None:
        import capo_lambda_web.types.date_time

        out["created_at"] = capo_lambda_web.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("FunctionSummary.created_at required")
    if data.get("updatedAt") is not None:
        import capo_lambda_web.types.date_time

        out["updated_at"] = capo_lambda_web.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("FunctionSummary.updated_at required")
    return out
