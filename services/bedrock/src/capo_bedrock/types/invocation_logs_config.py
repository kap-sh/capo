"""Generated from Smithy shape ``com.amazonaws.bedrock#InvocationLogsConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.invocation_log_source
    import capo_bedrock.types.request_metadata_filters
    import capo_bedrock.types.use_prompt_response


class InvocationLogsConfig(TypedDict, closed=True):
    use_prompt_response: "capo_bedrock.types.use_prompt_response.UsePromptResponse"
    """<p>Whether to use the model's response for training, or just the prompt. The default value is <code>False</code>.</p>"""
    invocation_log_source: (
        "capo_bedrock.types.invocation_log_source.InvocationLogSource"
    )
    """<p>The source of the invocation logs.</p>"""
    request_metadata_filters: NotRequired[
        "capo_bedrock.types.request_metadata_filters.RequestMetadataFilters"
    ]
    """<p>Rules for filtering invocation logs based on request metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationLogsConfig) -> dict:
    out: dict = {}
    out["usePromptResponse"] = value.get("use_prompt_response", False)
    import capo_bedrock.types.invocation_log_source

    out["invocationLogSource"] = (
        capo_bedrock.types.invocation_log_source.serialize_json(
            value["invocation_log_source"]
        )
    )
    if "request_metadata_filters" in value:
        import capo_bedrock.types.request_metadata_filters

        out["requestMetadataFilters"] = (
            capo_bedrock.types.request_metadata_filters.serialize_json(
                value["request_metadata_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvocationLogsConfig:
    out: InvocationLogsConfig = {}  # type: ignore[typeddict-item]
    if data.get("usePromptResponse") is not None:
        out["use_prompt_response"] = data["usePromptResponse"]
    else:
        out["use_prompt_response"] = False
    if data.get("invocationLogSource") is not None:
        import capo_bedrock.types.invocation_log_source

        out["invocation_log_source"] = (
            capo_bedrock.types.invocation_log_source.deserialize_json(
                data["invocationLogSource"]
            )
        )
    else:
        import capo_bedrock.types._unknown

        out["invocation_log_source"] = capo_bedrock.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("requestMetadataFilters") is not None:
        import capo_bedrock.types.request_metadata_filters

        out["request_metadata_filters"] = (
            capo_bedrock.types.request_metadata_filters.deserialize_json(
                data["requestMetadataFilters"]
            )
        )
    return out


def redact_sensitive(value: InvocationLogsConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "request_metadata_filters" in value:
        import capo_bedrock.types.request_metadata_filters

        out["request_metadata_filters"] = (
            capo_bedrock.types.request_metadata_filters.redact_sensitive(
                value["request_metadata_filters"]
            )
        )
    return out
