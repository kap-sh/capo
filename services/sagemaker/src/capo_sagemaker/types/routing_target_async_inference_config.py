"""Generated from Smithy shape ``com.amazonaws.sagemaker#RoutingTargetAsyncInferenceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.routing_target_async_inference_client_config
    import capo_sagemaker.types.routing_target_async_inference_output_config


class RoutingTargetAsyncInferenceConfig(TypedDict, closed=True):
    output_config: NotRequired[
        "capo_sagemaker.types.routing_target_async_inference_output_config.RoutingTargetAsyncInferenceOutputConfig"
    ]
    """<p>The Amazon S3 locations for the results of asynchronous requests, and the notification settings.</p>"""
    client_config: NotRequired[
        "capo_sagemaker.types.routing_target_async_inference_client_config.RoutingTargetAsyncInferenceClientConfig"
    ]
    """<p>How the inference router submits requests to destinations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoutingTargetAsyncInferenceConfig) -> dict:
    out: dict = {}
    if "output_config" in value:
        import capo_sagemaker.types.routing_target_async_inference_output_config

        out["OutputConfig"] = (
            capo_sagemaker.types.routing_target_async_inference_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "client_config" in value:
        import capo_sagemaker.types.routing_target_async_inference_client_config

        out["ClientConfig"] = (
            capo_sagemaker.types.routing_target_async_inference_client_config.serialize_aws_json_1_1(
                value["client_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RoutingTargetAsyncInferenceConfig:
    out: RoutingTargetAsyncInferenceConfig = {}  # type: ignore[typeddict-item]
    if data.get("OutputConfig") is not None:
        import capo_sagemaker.types.routing_target_async_inference_output_config

        out["output_config"] = (
            capo_sagemaker.types.routing_target_async_inference_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if data.get("ClientConfig") is not None:
        import capo_sagemaker.types.routing_target_async_inference_client_config

        out["client_config"] = (
            capo_sagemaker.types.routing_target_async_inference_client_config.deserialize_aws_json_1_1(
                data["ClientConfig"]
            )
        )
    return out
