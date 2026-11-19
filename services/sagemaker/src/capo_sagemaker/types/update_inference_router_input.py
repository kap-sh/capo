"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateInferenceRouterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_router_name
    import capo_sagemaker.types.routing_target_list


class UpdateInferenceRouterInput(TypedDict, closed=True):
    inference_router_name: NotRequired[
        "capo_sagemaker.types.inference_router_name.InferenceRouterName"
    ]
    """<p>The name of the inference router to update.</p>"""
    routing_targets: NotRequired[
        "capo_sagemaker.types.routing_target_list.RoutingTargetList"
    ]
    """<p>The complete list of routing targets for the inference router. To remove the last routing target, delete the router.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInferenceRouterInput) -> dict:
    out: dict = {}
    if "inference_router_name" in value:
        out["InferenceRouterName"] = value["inference_router_name"]
    if "routing_targets" in value:
        import capo_sagemaker.types.routing_target_list

        out["RoutingTargets"] = (
            capo_sagemaker.types.routing_target_list.serialize_aws_json_1_1(
                value["routing_targets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInferenceRouterInput:
    out: UpdateInferenceRouterInput = {}  # type: ignore[typeddict-item]
    if data.get("InferenceRouterName") is not None:
        out["inference_router_name"] = data["InferenceRouterName"]
    if data.get("RoutingTargets") is not None:
        import capo_sagemaker.types.routing_target_list

        out["routing_targets"] = (
            capo_sagemaker.types.routing_target_list.deserialize_aws_json_1_1(
                data["RoutingTargets"]
            )
        )
    return out
