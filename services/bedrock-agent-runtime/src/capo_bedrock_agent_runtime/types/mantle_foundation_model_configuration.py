"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#MantleFoundationModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.mantle_foundation_model_model_configuration


class MantleFoundationModelConfiguration(TypedDict, closed=True):
    model_configuration: "capo_bedrock_agent_runtime.types.mantle_foundation_model_model_configuration.MantleFoundationModelModelConfiguration"
    """<p>The model configuration containing the model ARN and project ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MantleFoundationModelConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.mantle_foundation_model_model_configuration

    out["modelConfiguration"] = (
        capo_bedrock_agent_runtime.types.mantle_foundation_model_model_configuration.serialize_json(
            value["model_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> MantleFoundationModelConfiguration:
    out: MantleFoundationModelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("modelConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.mantle_foundation_model_model_configuration

        out["model_configuration"] = (
            capo_bedrock_agent_runtime.types.mantle_foundation_model_model_configuration.deserialize_json(
                data["modelConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "MantleFoundationModelConfiguration.model_configuration required"
        )
    return out
