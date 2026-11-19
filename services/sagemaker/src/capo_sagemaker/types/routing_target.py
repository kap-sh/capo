"""Generated from Smithy shape ``com.amazonaws.sagemaker#RoutingTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.destination_list
    import capo_sagemaker.types.inference_router_routing_preference
    import capo_sagemaker.types.routing_target_async_inference_config
    import capo_sagemaker.types.routing_target_name


class RoutingTarget(TypedDict, closed=True):
    name: NotRequired["capo_sagemaker.types.routing_target_name.RoutingTargetName"]
    """<p>The name of the routing target. Callers specify this name in the <code>RoutingTargetName</code> parameter when they invoke the inference router. The name must be unique within the router.</p>"""
    destinations: NotRequired["capo_sagemaker.types.destination_list.DestinationList"]
    """<p>The endpoints and inference components that serve the routing target. Each destination can appear only once in a routing target.</p> <p>In an asynchronous routing target, every destination must be an asynchronous inference endpoint. In a real-time routing target, no destination can be one. SageMaker AI checks an endpoint in another account with your credentials, so both your IAM policy and the endpoint policy must allow <code>sagemaker:DescribeEndpoint</code>. If an endpoint can't be checked, for example because it isn't found or can't be read in time, it's accepted, and requests to it fail if it's the wrong mode.</p>"""
    async_inference_config: NotRequired[
        "capo_sagemaker.types.routing_target_async_inference_config.RoutingTargetAsyncInferenceConfig"
    ]
    """<p>The asynchronous inference settings of the routing target. Specify this setting to make the routing target asynchronous. If you omit it, the routing target serves real-time requests.</p> <p>Asynchronous routing targets aren't available in all Amazon Web Services Regions. For information about asynchronous routing targets and Region availability, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-async.html">Send asynchronous requests through an inference router</a>.</p> <p>Because <code>UpdateInferenceRouter</code> replaces all routing targets, include this setting in every update of an asynchronous routing target.</p> <p>For information about asynchronous routing targets, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-async.html">Send asynchronous requests through an inference router</a>.</p>"""
    routing_preference: NotRequired[
        "capo_sagemaker.types.inference_router_routing_preference.InferenceRouterRoutingPreference"
    ]
    """<p>How the inference router chooses among the routing target's destinations. The default is <code>LocalRegionFirst</code>.</p> <dl> <dt>LocalRegionFirst</dt> <dd> <p>The router uses destinations in its own Region first. When the request leaves the Region, the router spreads it across healthy destinations in other Regions.</p> </dd> <dt>InstancePoolOrder</dt> <dd> <p>The router prefers destinations by instance type first and by Region second. Every destination must be an endpoint that lists the same two or more instance types, each with a different priority, in the same priority order. This value is supported only for asynchronous routing targets.</p> </dd> </dl> <p>With either value, the router uses destinations whose health or capacity is reduced after the others, but doesn't exclude them.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoutingTarget) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "destinations" in value:
        import capo_sagemaker.types.destination_list

        out["Destinations"] = (
            capo_sagemaker.types.destination_list.serialize_aws_json_1_1(
                value["destinations"]
            )
        )
    if "async_inference_config" in value:
        import capo_sagemaker.types.routing_target_async_inference_config

        out["AsyncInferenceConfig"] = (
            capo_sagemaker.types.routing_target_async_inference_config.serialize_aws_json_1_1(
                value["async_inference_config"]
            )
        )
    if "routing_preference" in value:
        import capo_sagemaker.types.inference_router_routing_preference

        out["RoutingPreference"] = (
            capo_sagemaker.types.inference_router_routing_preference.serialize_aws_json_1_1(
                value["routing_preference"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RoutingTarget:
    out: RoutingTarget = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Destinations") is not None:
        import capo_sagemaker.types.destination_list

        out["destinations"] = (
            capo_sagemaker.types.destination_list.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    if data.get("AsyncInferenceConfig") is not None:
        import capo_sagemaker.types.routing_target_async_inference_config

        out["async_inference_config"] = (
            capo_sagemaker.types.routing_target_async_inference_config.deserialize_aws_json_1_1(
                data["AsyncInferenceConfig"]
            )
        )
    if data.get("RoutingPreference") is not None:
        import capo_sagemaker.types.inference_router_routing_preference

        out["routing_preference"] = (
            capo_sagemaker.types.inference_router_routing_preference.deserialize_aws_json_1_1(
                data["RoutingPreference"]
            )
        )
    return out
