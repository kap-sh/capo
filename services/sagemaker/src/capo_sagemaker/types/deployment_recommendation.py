"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeploymentRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.real_time_inference_recommendations
    import capo_sagemaker.types.recommendation_status


class DeploymentRecommendation(TypedDict, closed=True):
    recommendation_status: NotRequired[
        "capo_sagemaker.types.recommendation_status.RecommendationStatus"
    ]
    """<p>Status of the deployment recommendation. The status <code>NOT_APPLICABLE</code> means that SageMaker is unable to provide a default recommendation for the model using the information provided. If the deployment status is <code>IN_PROGRESS</code>, retry your API call after a few seconds to get a <code>COMPLETED</code> deployment recommendation.</p>"""
    real_time_inference_recommendations: NotRequired[
        "capo_sagemaker.types.real_time_inference_recommendations.RealTimeInferenceRecommendations"
    ]
    """<p>A list of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RealTimeInferenceRecommendation.html">RealTimeInferenceRecommendation</a> items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentRecommendation) -> dict:
    out: dict = {}
    if "recommendation_status" in value:
        import capo_sagemaker.types.recommendation_status

        out["RecommendationStatus"] = (
            capo_sagemaker.types.recommendation_status.serialize_aws_json_1_1(
                value["recommendation_status"]
            )
        )
    if "real_time_inference_recommendations" in value:
        import capo_sagemaker.types.real_time_inference_recommendations

        out["RealTimeInferenceRecommendations"] = (
            capo_sagemaker.types.real_time_inference_recommendations.serialize_aws_json_1_1(
                value["real_time_inference_recommendations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentRecommendation:
    out: DeploymentRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("RecommendationStatus") is not None:
        import capo_sagemaker.types.recommendation_status

        out["recommendation_status"] = (
            capo_sagemaker.types.recommendation_status.deserialize_aws_json_1_1(
                data["RecommendationStatus"]
            )
        )
    if data.get("RealTimeInferenceRecommendations") is not None:
        import capo_sagemaker.types.real_time_inference_recommendations

        out["real_time_inference_recommendations"] = (
            capo_sagemaker.types.real_time_inference_recommendations.deserialize_aws_json_1_1(
                data["RealTimeInferenceRecommendations"]
            )
        )
    return out
