"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#StartAsyncInvokeRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.async_invoke_idempotency_token
    import capo_bedrock_runtime.types.async_invoke_identifier
    import capo_bedrock_runtime.types.async_invoke_output_data_config
    import capo_bedrock_runtime.types.model_input_payload
    import capo_bedrock_runtime.types.tag_list


class StartAsyncInvokeRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_bedrock_runtime.types.async_invoke_idempotency_token.AsyncInvokeIdempotencyToken"
    ]
    """<p>Specify idempotency token to ensure that requests are not duplicated.</p>"""
    model_id: "capo_bedrock_runtime.types.async_invoke_identifier.AsyncInvokeIdentifier"
    """<p>The model to invoke.</p>"""
    model_input: "capo_bedrock_runtime.types.model_input_payload.ModelInputPayload"
    """<p>Input to send to the model.</p>"""
    output_data_config: "capo_bedrock_runtime.types.async_invoke_output_data_config.AsyncInvokeOutputDataConfig"
    """<p>Where to store the output.</p>"""
    tags: NotRequired["capo_bedrock_runtime.types.tag_list.TagList"]
    """<p>Tags to apply to the invocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAsyncInvokeRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["modelId"] = value["model_id"]
    out["modelInput"] = value["model_input"]
    import capo_bedrock_runtime.types.async_invoke_output_data_config

    out["outputDataConfig"] = (
        capo_bedrock_runtime.types.async_invoke_output_data_config.serialize_json(
            value["output_data_config"]
        )
    )
    if "tags" in value:
        import capo_bedrock_runtime.types.tag_list

        out["tags"] = capo_bedrock_runtime.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartAsyncInvokeRequest:
    out: StartAsyncInvokeRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("modelInput") is not None:
        out["model_input"] = data["modelInput"]
    else:
        out["model_input"] = None
    if data.get("outputDataConfig") is not None:
        import capo_bedrock_runtime.types.async_invoke_output_data_config

        out["output_data_config"] = (
            capo_bedrock_runtime.types.async_invoke_output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        out["output_data_config"] = {"$unknown": {"name": ""}}
    if data.get("tags") is not None:
        import capo_bedrock_runtime.types.tag_list

        out["tags"] = capo_bedrock_runtime.types.tag_list.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: StartAsyncInvokeRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "model_input" in value:
        out["model_input"] = "*** Sensitive Data Redacted ***"
    return out
