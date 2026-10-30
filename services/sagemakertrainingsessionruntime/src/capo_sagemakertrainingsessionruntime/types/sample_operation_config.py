"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SampleOperationConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_sagemakertrainingsessionruntime.errors import (
    DeserializationError,
    SerializationError,
)
from capo_sagemakertrainingsessionruntime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.compute_logprobs_config
    import capo_sagemakertrainingsessionruntime.types.load_weights_for_sampling_config
    import capo_sagemakertrainingsessionruntime.types.sample_config


class SampleOperationConfigSampleMember(TypedDict, closed=True):
    sample: "capo_sagemakertrainingsessionruntime.types.sample_config.SampleConfig"


class SampleOperationConfigComputeLogprobsMember(TypedDict, closed=True):
    computeLogprobs: "capo_sagemakertrainingsessionruntime.types.compute_logprobs_config.ComputeLogprobsConfig"


class SampleOperationConfigLoadWeightsForSamplingMember(TypedDict, closed=True):
    loadWeightsForSampling: "capo_sagemakertrainingsessionruntime.types.load_weights_for_sampling_config.LoadWeightsForSamplingConfig"


SampleOperationConfig: TypeAlias = (
    SampleOperationConfigSampleMember
    | SampleOperationConfigComputeLogprobsMember
    | SampleOperationConfigLoadWeightsForSamplingMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SampleOperationConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SampleOperationConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "sample" in value:
        import capo_sagemakertrainingsessionruntime.types.sample_config

        return {
            "sample": capo_sagemakertrainingsessionruntime.types.sample_config.serialize_json(
                value["sample"]
            )
        }
    elif "computeLogprobs" in value:
        import capo_sagemakertrainingsessionruntime.types.compute_logprobs_config

        return {
            "computeLogprobs": capo_sagemakertrainingsessionruntime.types.compute_logprobs_config.serialize_json(
                value["computeLogprobs"]
            )
        }
    elif "loadWeightsForSampling" in value:
        import capo_sagemakertrainingsessionruntime.types.load_weights_for_sampling_config

        return {
            "loadWeightsForSampling": capo_sagemakertrainingsessionruntime.types.load_weights_for_sampling_config.serialize_json(
                value["loadWeightsForSampling"]
            )
        }
    else:
        raise SerializationError("SampleOperationConfig: no variant present")


def deserialize_json(data: dict) -> SampleOperationConfig:
    if data.get("sample") is not None:
        import capo_sagemakertrainingsessionruntime.types.sample_config

        return {
            "sample": capo_sagemakertrainingsessionruntime.types.sample_config.deserialize_json(
                data["sample"]
            )
        }
    elif data.get("computeLogprobs") is not None:
        import capo_sagemakertrainingsessionruntime.types.compute_logprobs_config

        return {
            "computeLogprobs": capo_sagemakertrainingsessionruntime.types.compute_logprobs_config.deserialize_json(
                data["computeLogprobs"]
            )
        }
    elif data.get("loadWeightsForSampling") is not None:
        import capo_sagemakertrainingsessionruntime.types.load_weights_for_sampling_config

        return {
            "loadWeightsForSampling": capo_sagemakertrainingsessionruntime.types.load_weights_for_sampling_config.deserialize_json(
                data["loadWeightsForSampling"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SampleOperationConfig: no recognized variant key")


def redact_sensitive(value: SampleOperationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sample" in value:
        import capo_sagemakertrainingsessionruntime.types.sample_config

        out["sample"] = (
            capo_sagemakertrainingsessionruntime.types.sample_config.redact_sensitive(
                value["sample"]
            )
        )
    if "computeLogprobs" in value:
        import capo_sagemakertrainingsessionruntime.types.compute_logprobs_config

        out["computeLogprobs"] = (
            capo_sagemakertrainingsessionruntime.types.compute_logprobs_config.redact_sensitive(
                value["computeLogprobs"]
            )
        )
    return out
