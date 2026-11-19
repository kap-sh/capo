"""Generated from Smithy shape ``com.amazonaws.codedeploy#TrafficRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.listener_arn_list


class TrafficRoute(TypedDict, closed=True):
    listener_arns: NotRequired[
        "capo_codedeploy.types.listener_arn_list.ListenerArnList"
    ]
    """<p> The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrafficRoute) -> dict:
    out: dict = {}
    if "listener_arns" in value:
        import capo_codedeploy.types.listener_arn_list

        out["listenerArns"] = (
            capo_codedeploy.types.listener_arn_list.serialize_aws_json_1_1(
                value["listener_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrafficRoute:
    out: TrafficRoute = {}  # type: ignore[typeddict-item]
    if data.get("listenerArns") is not None:
        import capo_codedeploy.types.listener_arn_list

        out["listener_arns"] = (
            capo_codedeploy.types.listener_arn_list.deserialize_aws_json_1_1(
                data["listenerArns"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TrafficRoute) -> dict:
    out: dict = {}
    if "listener_arns" in value:
        import capo_codedeploy.types.listener_arn_list

        out["listenerArns"] = capo_codedeploy.types.listener_arn_list.serialize_cbor(
            value["listener_arns"]
        )
    return out


def deserialize_cbor(data: dict) -> TrafficRoute:
    out: TrafficRoute = {}  # type: ignore[typeddict-item]
    if data.get("listenerArns") is not None:
        import capo_codedeploy.types.listener_arn_list

        out["listener_arns"] = capo_codedeploy.types.listener_arn_list.deserialize_cbor(
            data["listenerArns"]
        )
    return out
