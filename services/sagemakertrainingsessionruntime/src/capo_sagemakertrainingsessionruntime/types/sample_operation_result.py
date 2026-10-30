"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SampleOperationResult``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_sagemakertrainingsessionruntime.errors import (
    DeserializationError,
    SerializationError,
)
from capo_sagemakertrainingsessionruntime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.compute_logprobs_result
    import capo_sagemakertrainingsessionruntime.types.load_weights_for_sampling_result
    import capo_sagemakertrainingsessionruntime.types.sample_response


class SampleOperationResultSampleMember(TypedDict, closed=True):
    sample: "capo_sagemakertrainingsessionruntime.types.sample_response.SampleResponse"


class SampleOperationResultComputeLogprobsMember(TypedDict, closed=True):
    computeLogprobs: "capo_sagemakertrainingsessionruntime.types.compute_logprobs_result.ComputeLogprobsResult"


class SampleOperationResultLoadWeightsForSamplingMember(TypedDict, closed=True):
    loadWeightsForSampling: "capo_sagemakertrainingsessionruntime.types.load_weights_for_sampling_result.LoadWeightsForSamplingResult"


SampleOperationResult: TypeAlias = (
    SampleOperationResultSampleMember
    | SampleOperationResultComputeLogprobsMember
    | SampleOperationResultLoadWeightsForSamplingMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SampleOperationResult) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SampleOperationResult: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "sample" in value:
        import capo_sagemakertrainingsessionruntime.types.sample_response

        return {
            "sample": capo_sagemakertrainingsessionruntime.types.sample_response.serialize_json(
                value["sample"]
            )
        }
    elif "computeLogprobs" in value:
        import capo_sagemakertrainingsessionruntime.types.compute_logprobs_result

        return {
            "computeLogprobs": capo_sagemakertrainingsessionruntime.types.compute_logprobs_result.serialize_json(
                value["computeLogprobs"]
            )
        }
    elif "loadWeightsForSampling" in value:
        import capo_sagemakertrainingsessionruntime.types.load_weights_for_sampling_result

        return {
            "loadWeightsForSampling": capo_sagemakertrainingsessionruntime.types.load_weights_for_sampling_result.serialize_json(
                value["loadWeightsForSampling"]
            )
        }
    else:
        raise SerializationError("SampleOperationResult: no variant present")


def deserialize_json(data: dict) -> SampleOperationResult:
    if data.get("sample") is not None:
        import capo_sagemakertrainingsessionruntime.types.sample_response

        return {
            "sample": capo_sagemakertrainingsessionruntime.types.sample_response.deserialize_json(
                data["sample"]
            )
        }
    elif data.get("computeLogprobs") is not None:
        import capo_sagemakertrainingsessionruntime.types.compute_logprobs_result

        return {
            "computeLogprobs": capo_sagemakertrainingsessionruntime.types.compute_logprobs_result.deserialize_json(
                data["computeLogprobs"]
            )
        }
    elif data.get("loadWeightsForSampling") is not None:
        import capo_sagemakertrainingsessionruntime.types.load_weights_for_sampling_result

        return {
            "loadWeightsForSampling": capo_sagemakertrainingsessionruntime.types.load_weights_for_sampling_result.deserialize_json(
                data["loadWeightsForSampling"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SampleOperationResult: no recognized variant key")


def redact_sensitive(value: SampleOperationResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sample" in value:
        out["sample"] = "*** Sensitive Data Redacted ***"
    return out
