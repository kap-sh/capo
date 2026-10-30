"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SampleConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sagemakertrainingsessionruntime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.model_input
    import capo_sagemakertrainingsessionruntime.types.sampling_params


class SampleConfig(TypedDict, closed=True):
    prompt: "capo_sagemakertrainingsessionruntime.types.model_input.ModelInput"
    """<p>The input prompt to send to the model for text generation.</p>"""
    num_samples: "int"
    """<p>The number of independent samples to generate for the prompt.</p>"""
    sampling_params: (
        "capo_sagemakertrainingsessionruntime.types.sampling_params.SamplingParams"
    )
    """<p>The parameters controlling the sampling strategy.</p>"""
    include_prompt_logprobs: "bool"
    """<p>Specifies whether to include per-token log-probabilities for the input prompt in the response.</p>"""
    topk_prompt_logprobs: "int"
    """<p>The number of top-k log-probabilities to return per prompt token.</p>"""
    model_package_arn: NotRequired["str"]
    """<p>The ARN of the model package whose checkpoint this sample should run against. Must be a valid SageMaker model package ARN in the format <code>arn:aws:sagemaker:REGION:ACCOUNT:model-package/PACKAGE_NAME/VERSION</code>. When absent, the sample runs against the session's latest checkpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SampleConfig) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.model_input

    out["prompt"] = (
        capo_sagemakertrainingsessionruntime.types.model_input.serialize_json(
            value["prompt"]
        )
    )
    out["numSamples"] = value["num_samples"]
    import capo_sagemakertrainingsessionruntime.types.sampling_params

    out["samplingParams"] = (
        capo_sagemakertrainingsessionruntime.types.sampling_params.serialize_json(
            value["sampling_params"]
        )
    )
    out["includePromptLogprobs"] = value.get("include_prompt_logprobs", False)
    out["topkPromptLogprobs"] = value.get("topk_prompt_logprobs", 0)
    if "model_package_arn" in value:
        out["modelPackageArn"] = value["model_package_arn"]
    return out


def deserialize_json(data: dict) -> SampleConfig:
    out: SampleConfig = {}  # type: ignore[typeddict-item]
    if data.get("prompt") is not None:
        import capo_sagemakertrainingsessionruntime.types.model_input

        out["prompt"] = (
            capo_sagemakertrainingsessionruntime.types.model_input.deserialize_json(
                data["prompt"]
            )
        )
    else:
        raise DeserializationError("SampleConfig.prompt required")
    if data.get("numSamples") is not None:
        out["num_samples"] = data["numSamples"]
    else:
        out["num_samples"] = 0
    if data.get("samplingParams") is not None:
        import capo_sagemakertrainingsessionruntime.types.sampling_params

        out["sampling_params"] = (
            capo_sagemakertrainingsessionruntime.types.sampling_params.deserialize_json(
                data["samplingParams"]
            )
        )
    else:
        raise DeserializationError("SampleConfig.sampling_params required")
    if data.get("includePromptLogprobs") is not None:
        out["include_prompt_logprobs"] = data["includePromptLogprobs"]
    else:
        out["include_prompt_logprobs"] = False
    if data.get("topkPromptLogprobs") is not None:
        out["topk_prompt_logprobs"] = data["topkPromptLogprobs"]
    else:
        out["topk_prompt_logprobs"] = 0
    if data.get("modelPackageArn") is not None:
        out["model_package_arn"] = data["modelPackageArn"]
    return out


def redact_sensitive(value: SampleConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "prompt" in value:
        out["prompt"] = "*** Sensitive Data Redacted ***"
    return out
