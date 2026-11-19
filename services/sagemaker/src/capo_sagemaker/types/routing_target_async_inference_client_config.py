"""Generated from Smithy shape ``com.amazonaws.sagemaker#RoutingTargetAsyncInferenceClientConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_router_max_time_in_backlog_seconds


class RoutingTargetAsyncInferenceClientConfig(TypedDict, closed=True):
    max_time_in_backlog_seconds: NotRequired[
        "capo_sagemaker.types.inference_router_max_time_in_backlog_seconds.InferenceRouterMaxTimeInBacklogSeconds"
    ]
    """<p>The maximum time, in seconds, that a request can wait at a destination before the inference router moves it to another destination. The default is 900 seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoutingTargetAsyncInferenceClientConfig) -> dict:
    out: dict = {}
    if "max_time_in_backlog_seconds" in value:
        out["MaxTimeInBacklogSeconds"] = value["max_time_in_backlog_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RoutingTargetAsyncInferenceClientConfig:
    out: RoutingTargetAsyncInferenceClientConfig = {}  # type: ignore[typeddict-item]
    if data.get("MaxTimeInBacklogSeconds") is not None:
        out["max_time_in_backlog_seconds"] = data["MaxTimeInBacklogSeconds"]
    return out
