"""Generated from Smithy shape ``com.amazonaws.sagemaker#RoutingTargetAsyncInferenceNotificationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_router_sns_topic_arn


class RoutingTargetAsyncInferenceNotificationConfig(TypedDict, closed=True):
    success_topic: NotRequired[
        "capo_sagemaker.types.inference_router_sns_topic_arn.InferenceRouterSnsTopicArn"
    ]
    """<p>The ARN of the Amazon SNS topic to publish to when a request completes. The topic must be a standard topic, and can be in any Amazon Web Services Region.</p>"""
    error_topic: NotRequired[
        "capo_sagemaker.types.inference_router_sns_topic_arn.InferenceRouterSnsTopicArn"
    ]
    """<p>The ARN of the Amazon SNS topic to publish to when a request fails, or when the router can't place it on any destination. The topic must be a standard topic, and can be in any Amazon Web Services Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: RoutingTargetAsyncInferenceNotificationConfig,
) -> dict:
    out: dict = {}
    if "success_topic" in value:
        out["SuccessTopic"] = value["success_topic"]
    if "error_topic" in value:
        out["ErrorTopic"] = value["error_topic"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> RoutingTargetAsyncInferenceNotificationConfig:
    out: RoutingTargetAsyncInferenceNotificationConfig = {}  # type: ignore[typeddict-item]
    if data.get("SuccessTopic") is not None:
        out["success_topic"] = data["SuccessTopic"]
    if data.get("ErrorTopic") is not None:
        out["error_topic"] = data["ErrorTopic"]
    return out
