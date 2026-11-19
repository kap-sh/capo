"""Generated from Smithy shape ``com.amazonaws.sagemaker#RoutingTargetAsyncInferenceOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_router_s3_uri
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.routing_target_async_inference_notification_config


class RoutingTargetAsyncInferenceOutputConfig(TypedDict, closed=True):
    s3_output_path: NotRequired[
        "capo_sagemaker.types.inference_router_s3_uri.InferenceRouterS3Uri"
    ]
    """<p>The Amazon S3 location for the results of successful requests. The bucket must be in the inference router's Amazon Web Services Region and owned by the router's account.</p>"""
    s3_failure_path: NotRequired[
        "capo_sagemaker.types.inference_router_s3_uri.InferenceRouterS3Uri"
    ]
    """<p>The Amazon S3 location for the failure details of failed requests. The bucket must be in the inference router's Amazon Web Services Region and owned by the router's account.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The KMS key that encrypts the results in Amazon S3. You can specify a key ID, key ARN, alias name, or alias ARN. If any destination is in a different account or Amazon Web Services Region from the inference router, specify a key ARN or an alias ARN.</p>"""
    notification_config: NotRequired[
        "capo_sagemaker.types.routing_target_async_inference_notification_config.RoutingTargetAsyncInferenceNotificationConfig"
    ]
    """<p>The Amazon SNS topics that the inference router publishes to when a request completes or fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoutingTargetAsyncInferenceOutputConfig) -> dict:
    out: dict = {}
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    if "s3_failure_path" in value:
        out["S3FailurePath"] = value["s3_failure_path"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "notification_config" in value:
        import capo_sagemaker.types.routing_target_async_inference_notification_config

        out["NotificationConfig"] = (
            capo_sagemaker.types.routing_target_async_inference_notification_config.serialize_aws_json_1_1(
                value["notification_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RoutingTargetAsyncInferenceOutputConfig:
    out: RoutingTargetAsyncInferenceOutputConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3OutputPath") is not None:
        out["s3_output_path"] = data["S3OutputPath"]
    if data.get("S3FailurePath") is not None:
        out["s3_failure_path"] = data["S3FailurePath"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("NotificationConfig") is not None:
        import capo_sagemaker.types.routing_target_async_inference_notification_config

        out["notification_config"] = (
            capo_sagemaker.types.routing_target_async_inference_notification_config.deserialize_aws_json_1_1(
                data["NotificationConfig"]
            )
        )
    return out
