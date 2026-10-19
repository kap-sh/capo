"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InferenceOperationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.inference_operation_path
    import capo_bedrock_agentcore_control.types.model_entries


class InferenceOperationConfiguration(TypedDict, closed=True):
    path: "capo_bedrock_agentcore_control.types.inference_operation_path.InferenceOperationPath"
    """<p>The request path for this operation (for example, <code>/v1/messages</code> or <code>/v1/responses</code>).</p>"""
    provider_path: NotRequired[
        "capo_bedrock_agentcore_control.types.inference_operation_path.InferenceOperationPath"
    ]
    """<p>The provider path to forward requests to, if it differs from the request path. For example, <code>/anthropic/v1/messages</code> when the provider expects a different path than the client-facing <code>/v1/messages</code>.</p>"""
    models: NotRequired[
        "capo_bedrock_agentcore_control.types.model_entries.ModelEntries"
    ]
    """<p>The list of models supported for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceOperationConfiguration) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    if "provider_path" in value:
        out["providerPath"] = value["provider_path"]
    if "models" in value:
        import capo_bedrock_agentcore_control.types.model_entries

        out["models"] = (
            capo_bedrock_agentcore_control.types.model_entries.serialize_json(
                value["models"]
            )
        )
    return out


def deserialize_json(data: dict) -> InferenceOperationConfiguration:
    out: InferenceOperationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    if data.get("providerPath") is not None:
        out["provider_path"] = data["providerPath"]
    if data.get("models") is not None:
        import capo_bedrock_agentcore_control.types.model_entries

        out["models"] = (
            capo_bedrock_agentcore_control.types.model_entries.deserialize_json(
                data["models"]
            )
        )
    return out
