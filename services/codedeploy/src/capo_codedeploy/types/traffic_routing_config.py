"""Generated from Smithy shape ``com.amazonaws.codedeploy#TrafficRoutingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.time_based_canary
    import capo_codedeploy.types.time_based_linear
    import capo_codedeploy.types.traffic_routing_type


class TrafficRoutingConfig(TypedDict, closed=True):
    type: NotRequired["capo_codedeploy.types.traffic_routing_type.TrafficRoutingType"]
    """<p>The type of traffic shifting (<code>TimeBasedCanary</code> or <code>TimeBasedLinear</code>) used by a deployment configuration.</p>"""
    time_based_canary: NotRequired[
        "capo_codedeploy.types.time_based_canary.TimeBasedCanary"
    ]
    """<p>A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in two increments. The original and target Lambda function versions or ECS task sets are specified in the deployment's AppSpec file.</p>"""
    time_based_linear: NotRequired[
        "capo_codedeploy.types.time_based_linear.TimeBasedLinear"
    ]
    """<p>A configuration that shifts traffic from one version of a Lambda function or Amazon ECS task set to another in equal increments, with an equal number of minutes between each increment. The original and target Lambda function versions or Amazon ECS task sets are specified in the deployment's AppSpec file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrafficRoutingConfig) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_codedeploy.types.traffic_routing_type

        out["type"] = capo_codedeploy.types.traffic_routing_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "time_based_canary" in value:
        import capo_codedeploy.types.time_based_canary

        out["timeBasedCanary"] = (
            capo_codedeploy.types.time_based_canary.serialize_aws_json_1_1(
                value["time_based_canary"]
            )
        )
    if "time_based_linear" in value:
        import capo_codedeploy.types.time_based_linear

        out["timeBasedLinear"] = (
            capo_codedeploy.types.time_based_linear.serialize_aws_json_1_1(
                value["time_based_linear"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrafficRoutingConfig:
    out: TrafficRoutingConfig = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codedeploy.types.traffic_routing_type

        out["type"] = (
            capo_codedeploy.types.traffic_routing_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if data.get("timeBasedCanary") is not None:
        import capo_codedeploy.types.time_based_canary

        out["time_based_canary"] = (
            capo_codedeploy.types.time_based_canary.deserialize_aws_json_1_1(
                data["timeBasedCanary"]
            )
        )
    if data.get("timeBasedLinear") is not None:
        import capo_codedeploy.types.time_based_linear

        out["time_based_linear"] = (
            capo_codedeploy.types.time_based_linear.deserialize_aws_json_1_1(
                data["timeBasedLinear"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TrafficRoutingConfig) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_codedeploy.types.traffic_routing_type

        out["type"] = capo_codedeploy.types.traffic_routing_type.serialize_cbor(
            value["type"]
        )
    if "time_based_canary" in value:
        import capo_codedeploy.types.time_based_canary

        out["timeBasedCanary"] = capo_codedeploy.types.time_based_canary.serialize_cbor(
            value["time_based_canary"]
        )
    if "time_based_linear" in value:
        import capo_codedeploy.types.time_based_linear

        out["timeBasedLinear"] = capo_codedeploy.types.time_based_linear.serialize_cbor(
            value["time_based_linear"]
        )
    return out


def deserialize_cbor(data: dict) -> TrafficRoutingConfig:
    out: TrafficRoutingConfig = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codedeploy.types.traffic_routing_type

        out["type"] = capo_codedeploy.types.traffic_routing_type.deserialize_cbor(
            data["type"]
        )
    if data.get("timeBasedCanary") is not None:
        import capo_codedeploy.types.time_based_canary

        out["time_based_canary"] = (
            capo_codedeploy.types.time_based_canary.deserialize_cbor(
                data["timeBasedCanary"]
            )
        )
    if data.get("timeBasedLinear") is not None:
        import capo_codedeploy.types.time_based_linear

        out["time_based_linear"] = (
            capo_codedeploy.types.time_based_linear.deserialize_cbor(
                data["timeBasedLinear"]
            )
        )
    return out
