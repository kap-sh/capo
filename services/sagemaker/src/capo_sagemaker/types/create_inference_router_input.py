"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateInferenceRouterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_router_client_token
    import capo_sagemaker.types.inference_router_name
    import capo_sagemaker.types.routing_target_list
    import capo_sagemaker.types.tag_list


class CreateInferenceRouterInput(TypedDict, closed=True):
    inference_router_name: NotRequired[
        "capo_sagemaker.types.inference_router_name.InferenceRouterName"
    ]
    """<p>The name of the inference router. The name must be unique within your account in the current Amazon Web Services Region. The name is case sensitive.</p>"""
    routing_targets: NotRequired[
        "capo_sagemaker.types.routing_target_list.RoutingTargetList"
    ]
    """<p>The routing targets of the inference router. Each routing target is a model that callers name when they invoke the router, and the destinations that serve it.</p>"""
    client_token: NotRequired[
        "capo_sagemaker.types.inference_router_client_token.InferenceRouterClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you reuse a client token, use the same request parameters. Otherwise, the request fails.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of key-value pairs to apply to the inference router. For information about tagging, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInferenceRouterInput) -> dict:
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInferenceRouterInput:
    out: CreateInferenceRouterInput = {}  # type: ignore[typeddict-item]
    if data.get("InferenceRouterName") is not None:
        out["inference_router_name"] = data["InferenceRouterName"]
    if data.get("RoutingTargets") is not None:
        import capo_sagemaker.types.routing_target_list

        out["routing_targets"] = (
            capo_sagemaker.types.routing_target_list.deserialize_aws_json_1_1(
                data["RoutingTargets"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
