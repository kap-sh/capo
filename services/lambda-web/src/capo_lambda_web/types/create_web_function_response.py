"""Generated from Smithy shape ``com.amazonaws.lambdaweb#CreateWebFunctionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.date_time
    import capo_lambda_web.types.function_arn
    import capo_lambda_web.types.function_endpoint_summary
    import capo_lambda_web.types.function_name
    import capo_lambda_web.types.function_revision_summary
    import capo_lambda_web.types.function_state
    import capo_lambda_web.types.tags


class CreateWebFunctionResponse(TypedDict, closed=True):
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
    revision: NotRequired[
        "capo_lambda_web.types.function_revision_summary.FunctionRevisionSummary"
    ]
    """<p>A summary of the initial revision created with the web function.</p>"""
    endpoint: NotRequired[
        "capo_lambda_web.types.function_endpoint_summary.FunctionEndpointSummary"
    ]
    """<p>A summary of the initial endpoint created with the web function.</p>"""
    tags: NotRequired["capo_lambda_web.types.tags.Tags"]
    """<p>A map of tag keys and values associated with the web function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWebFunctionResponse) -> dict:
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
    if "revision" in value:
        import capo_lambda_web.types.function_revision_summary

        out["revision"] = (
            capo_lambda_web.types.function_revision_summary.serialize_json(
                value["revision"]
            )
        )
    if "endpoint" in value:
        import capo_lambda_web.types.function_endpoint_summary

        out["endpoint"] = (
            capo_lambda_web.types.function_endpoint_summary.serialize_json(
                value["endpoint"]
            )
        )
    if "tags" in value:
        import capo_lambda_web.types.tags

        out["tags"] = capo_lambda_web.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateWebFunctionResponse:
    out: CreateWebFunctionResponse = {}  # type: ignore[typeddict-item]
    if data.get("functionName") is not None:
        out["function_name"] = data["functionName"]
    else:
        raise DeserializationError("CreateWebFunctionResponse.function_name required")
    if data.get("functionArn") is not None:
        out["function_arn"] = data["functionArn"]
    else:
        raise DeserializationError("CreateWebFunctionResponse.function_arn required")
    if data.get("state") is not None:
        import capo_lambda_web.types.function_state

        out["state"] = capo_lambda_web.types.function_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("CreateWebFunctionResponse.state required")
    if data.get("stateReason") is not None:
        out["state_reason"] = data["stateReason"]
    else:
        raise DeserializationError("CreateWebFunctionResponse.state_reason required")
    if data.get("createdAt") is not None:
        import capo_lambda_web.types.date_time

        out["created_at"] = capo_lambda_web.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateWebFunctionResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_lambda_web.types.date_time

        out["updated_at"] = capo_lambda_web.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("CreateWebFunctionResponse.updated_at required")
    if data.get("revision") is not None:
        import capo_lambda_web.types.function_revision_summary

        out["revision"] = (
            capo_lambda_web.types.function_revision_summary.deserialize_json(
                data["revision"]
            )
        )
    if data.get("endpoint") is not None:
        import capo_lambda_web.types.function_endpoint_summary

        out["endpoint"] = (
            capo_lambda_web.types.function_endpoint_summary.deserialize_json(
                data["endpoint"]
            )
        )
    if data.get("tags") is not None:
        import capo_lambda_web.types.tags

        out["tags"] = capo_lambda_web.types.tags.deserialize_json(data["tags"])
    return out
