"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GetAsyncInvokeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.async_invoke_arn
    import capo_bedrock_runtime.types.async_invoke_idempotency_token
    import capo_bedrock_runtime.types.async_invoke_message
    import capo_bedrock_runtime.types.async_invoke_output_data_config
    import capo_bedrock_runtime.types.async_invoke_status
    import capo_bedrock_runtime.types.invocation_arn
    import capo_bedrock_runtime.types.timestamp


class GetAsyncInvokeResponse(TypedDict, closed=True):
    invocation_arn: "capo_bedrock_runtime.types.invocation_arn.InvocationArn"
    """<p>The invocation's ARN.</p>"""
    model_arn: "capo_bedrock_runtime.types.async_invoke_arn.AsyncInvokeArn"
    """<p>The invocation's model ARN.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock_runtime.types.async_invoke_idempotency_token.AsyncInvokeIdempotencyToken"
    ]
    """<p>The invocation's idempotency token.</p>"""
    status: "capo_bedrock_runtime.types.async_invoke_status.AsyncInvokeStatus"
    """<p>The invocation's status.</p>"""
    failure_message: NotRequired[
        "capo_bedrock_runtime.types.async_invoke_message.AsyncInvokeMessage"
    ]
    """<p>An error message.</p>"""
    submit_time: "capo_bedrock_runtime.types.timestamp.Timestamp"
    """<p>When the invocation request was submitted.</p>"""
    last_modified_time: NotRequired["capo_bedrock_runtime.types.timestamp.Timestamp"]
    """<p>The invocation's last modified time.</p>"""
    end_time: NotRequired["capo_bedrock_runtime.types.timestamp.Timestamp"]
    """<p>When the invocation ended.</p>"""
    output_data_config: "capo_bedrock_runtime.types.async_invoke_output_data_config.AsyncInvokeOutputDataConfig"
    """<p>Output data settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAsyncInvokeResponse) -> dict:
    out: dict = {}
    out["invocationArn"] = value["invocation_arn"]
    out["modelArn"] = value["model_arn"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    import capo_bedrock_runtime.types.async_invoke_status

    out["status"] = capo_bedrock_runtime.types.async_invoke_status.serialize_json(
        value["status"]
    )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    import capo_bedrock_runtime.types.timestamp

    out["submitTime"] = capo_bedrock_runtime.types.timestamp.serialize_json(
        value["submit_time"]
    )
    if "last_modified_time" in value:
        import capo_bedrock_runtime.types.timestamp

        out["lastModifiedTime"] = capo_bedrock_runtime.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "end_time" in value:
        import capo_bedrock_runtime.types.timestamp

        out["endTime"] = capo_bedrock_runtime.types.timestamp.serialize_json(
            value["end_time"]
        )
    import capo_bedrock_runtime.types.async_invoke_output_data_config

    out["outputDataConfig"] = (
        capo_bedrock_runtime.types.async_invoke_output_data_config.serialize_json(
            value["output_data_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAsyncInvokeResponse:
    out: GetAsyncInvokeResponse = {}  # type: ignore[typeddict-item]
    if data.get("invocationArn") is not None:
        out["invocation_arn"] = data["invocationArn"]
    else:
        out["invocation_arn"] = ""
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("status") is not None:
        import capo_bedrock_runtime.types.async_invoke_status

        out["status"] = capo_bedrock_runtime.types.async_invoke_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_runtime.types.async_invoke_status.AsyncInvokeStatus", ""
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("submitTime") is not None:
        import capo_bedrock_runtime.types.timestamp

        out["submit_time"] = capo_bedrock_runtime.types.timestamp.deserialize_json(
            data["submitTime"]
        )
    else:
        import datetime

        out["submit_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModifiedTime") is not None:
        import capo_bedrock_runtime.types.timestamp

        out["last_modified_time"] = (
            capo_bedrock_runtime.types.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if data.get("endTime") is not None:
        import capo_bedrock_runtime.types.timestamp

        out["end_time"] = capo_bedrock_runtime.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if data.get("outputDataConfig") is not None:
        import capo_bedrock_runtime.types.async_invoke_output_data_config

        out["output_data_config"] = (
            capo_bedrock_runtime.types.async_invoke_output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        import capo_bedrock_runtime.types._unknown

        out["output_data_config"] = (
            capo_bedrock_runtime.types._unknown.UnknownUnionMember("")
        )
    return out


def redact_sensitive(value: GetAsyncInvokeResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "failure_message" in value:
        out["failure_message"] = "*** Sensitive Data Redacted ***"
    return out
