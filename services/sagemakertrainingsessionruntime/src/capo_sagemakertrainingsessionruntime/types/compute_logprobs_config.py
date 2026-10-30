"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#ComputeLogprobsConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sagemakertrainingsessionruntime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.model_input


class ComputeLogprobsConfig(TypedDict, closed=True):
    prompt: "capo_sagemakertrainingsessionruntime.types.model_input.ModelInput"
    """<p>The input prompt whose token log-probabilities will be computed.</p>"""
    model_package_arn: NotRequired["str"]
    """<p>The ARN of the model package whose checkpoint this operation should run against. Must be a valid SageMaker model package ARN in the format <code>arn:aws:sagemaker:REGION:ACCOUNT:model-package/PACKAGE_NAME/VERSION</code>. When absent, the operation runs against the session's latest checkpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeLogprobsConfig) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.model_input

    out["prompt"] = (
        capo_sagemakertrainingsessionruntime.types.model_input.serialize_json(
            value["prompt"]
        )
    )
    if "model_package_arn" in value:
        out["modelPackageArn"] = value["model_package_arn"]
    return out


def deserialize_json(data: dict) -> ComputeLogprobsConfig:
    out: ComputeLogprobsConfig = {}  # type: ignore[typeddict-item]
    if data.get("prompt") is not None:
        import capo_sagemakertrainingsessionruntime.types.model_input

        out["prompt"] = (
            capo_sagemakertrainingsessionruntime.types.model_input.deserialize_json(
                data["prompt"]
            )
        )
    else:
        raise DeserializationError("ComputeLogprobsConfig.prompt required")
    if data.get("modelPackageArn") is not None:
        out["model_package_arn"] = data["modelPackageArn"]
    return out


def redact_sensitive(value: ComputeLogprobsConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "prompt" in value:
        out["prompt"] = "*** Sensitive Data Redacted ***"
    return out
