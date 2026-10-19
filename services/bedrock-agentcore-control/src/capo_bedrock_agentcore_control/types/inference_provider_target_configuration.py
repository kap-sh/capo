"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InferenceProviderTargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.inference_operation_configurations
    import capo_bedrock_agentcore_control.types.model_mapping
    import capo_bedrock_agentcore_control.types.passthrough_endpoint


class InferenceProviderTargetConfiguration(TypedDict, closed=True):
    endpoint: (
        "capo_bedrock_agentcore_control.types.passthrough_endpoint.PassthroughEndpoint"
    )
    """<p>The HTTPS endpoint of the inference provider that the gateway forwards requests to.</p>"""
    model_mapping: NotRequired[
        "capo_bedrock_agentcore_control.types.model_mapping.ModelMapping"
    ]
    """<p>The configuration that translates client-facing model IDs to the model IDs expected by the provider.</p>"""
    operations: NotRequired[
        "capo_bedrock_agentcore_control.types.inference_operation_configurations.InferenceOperationConfigurations"
    ]
    """<p>A list of per-operation configurations that map request paths to the models supported for each operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceProviderTargetConfiguration) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    if "model_mapping" in value:
        import capo_bedrock_agentcore_control.types.model_mapping

        out["modelMapping"] = (
            capo_bedrock_agentcore_control.types.model_mapping.serialize_json(
                value["model_mapping"]
            )
        )
    if "operations" in value:
        import capo_bedrock_agentcore_control.types.inference_operation_configurations

        out["operations"] = (
            capo_bedrock_agentcore_control.types.inference_operation_configurations.serialize_json(
                value["operations"]
            )
        )
    return out


def deserialize_json(data: dict) -> InferenceProviderTargetConfiguration:
    out: InferenceProviderTargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    if data.get("modelMapping") is not None:
        import capo_bedrock_agentcore_control.types.model_mapping

        out["model_mapping"] = (
            capo_bedrock_agentcore_control.types.model_mapping.deserialize_json(
                data["modelMapping"]
            )
        )
    if data.get("operations") is not None:
        import capo_bedrock_agentcore_control.types.inference_operation_configurations

        out["operations"] = (
            capo_bedrock_agentcore_control.types.inference_operation_configurations.deserialize_json(
                data["operations"]
            )
        )
    return out
