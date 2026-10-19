"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SageMakerModelRecommendation``."""

from typing_extensions import NotRequired, TypedDict


class SageMakerModelRecommendation(TypedDict, closed=True):
    recommended_batch_transform_instance_type: "str"
    """<p>The recommended instance type for batch inference.</p>"""
    recommended_realtime_inference_instance_type: NotRequired["str"]
    """<p>The recommended instance type for real-time inference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerModelRecommendation) -> dict:
    out: dict = {}
    out["recommendedBatchTransformInstanceType"] = value[
        "recommended_batch_transform_instance_type"
    ]
    if "recommended_realtime_inference_instance_type" in value:
        out["recommendedRealtimeInferenceInstanceType"] = value[
            "recommended_realtime_inference_instance_type"
        ]
    return out


def deserialize_json(data: dict) -> SageMakerModelRecommendation:
    out: SageMakerModelRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("recommendedBatchTransformInstanceType") is not None:
        out["recommended_batch_transform_instance_type"] = data[
            "recommendedBatchTransformInstanceType"
        ]
    else:
        out["recommended_batch_transform_instance_type"] = ""
    if data.get("recommendedRealtimeInferenceInstanceType") is not None:
        out["recommended_realtime_inference_instance_type"] = data[
            "recommendedRealtimeInferenceInstanceType"
        ]
    return out
