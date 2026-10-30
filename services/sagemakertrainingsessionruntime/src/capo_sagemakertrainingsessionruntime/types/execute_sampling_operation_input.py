"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#ExecuteSamplingOperationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.sample_operation_config
    import capo_sagemakertrainingsessionruntime.types.training_session_name


class ExecuteSamplingOperationInput(TypedDict, closed=True):
    training_session_name: "capo_sagemakertrainingsessionruntime.types.training_session_name.TrainingSessionName"
    """<p>The name of the training session to sample from.</p>"""
    operation_config: "capo_sagemakertrainingsessionruntime.types.sample_operation_config.SampleOperationConfig"
    """<p>The configuration for the sample operation. Specify either a sample configuration to generate text or a computeLogprobs configuration to compute token log-probabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteSamplingOperationInput) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.sample_operation_config

    out["operationConfig"] = (
        capo_sagemakertrainingsessionruntime.types.sample_operation_config.serialize_json(
            value["operation_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExecuteSamplingOperationInput:
    out: ExecuteSamplingOperationInput = {}  # type: ignore[typeddict-item]
    if data.get("operationConfig") is not None:
        import capo_sagemakertrainingsessionruntime.types.sample_operation_config

        out["operation_config"] = (
            capo_sagemakertrainingsessionruntime.types.sample_operation_config.deserialize_json(
                data["operationConfig"]
            )
        )
    else:
        out["operation_config"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: ExecuteSamplingOperationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "operation_config" in value:
        import capo_sagemakertrainingsessionruntime.types.sample_operation_config

        out["operation_config"] = (
            capo_sagemakertrainingsessionruntime.types.sample_operation_config.redact_sensitive(
                value["operation_config"]
            )
        )
    return out
