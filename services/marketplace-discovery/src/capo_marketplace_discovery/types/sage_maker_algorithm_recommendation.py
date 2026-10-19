"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SageMakerAlgorithmRecommendation``."""

from typing_extensions import NotRequired, TypedDict


class SageMakerAlgorithmRecommendation(TypedDict, closed=True):
    recommended_batch_transform_instance_type: "str"
    """<p>The recommended instance type for batch inference.</p>"""
    recommended_realtime_inference_instance_type: NotRequired["str"]
    """<p>The recommended instance type for real-time inference.</p>"""
    recommended_training_instance_type: "str"
    """<p>The recommended instance type for training.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerAlgorithmRecommendation) -> dict:
    out: dict = {}
    out["recommendedBatchTransformInstanceType"] = value[
        "recommended_batch_transform_instance_type"
    ]
    if "recommended_realtime_inference_instance_type" in value:
        out["recommendedRealtimeInferenceInstanceType"] = value[
            "recommended_realtime_inference_instance_type"
        ]
    out["recommendedTrainingInstanceType"] = value["recommended_training_instance_type"]
    return out


def deserialize_json(data: dict) -> SageMakerAlgorithmRecommendation:
    out: SageMakerAlgorithmRecommendation = {}  # type: ignore[typeddict-item]
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
    if data.get("recommendedTrainingInstanceType") is not None:
        out["recommended_training_instance_type"] = data[
            "recommendedTrainingInstanceType"
        ]
    else:
        out["recommended_training_instance_type"] = ""
    return out
