"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetGroupPairInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.target_group_info_list
    import capo_codedeploy.types.traffic_route


class TargetGroupPairInfo(TypedDict, closed=True):
    target_groups: NotRequired[
        "capo_codedeploy.types.target_group_info_list.TargetGroupInfoList"
    ]
    """<p> One pair of target groups. One is associated with the original task set. The second is associated with the task set that serves traffic after the deployment is complete. </p>"""
    prod_traffic_route: NotRequired["capo_codedeploy.types.traffic_route.TrafficRoute"]
    """<p> The path used by a load balancer to route production traffic when an Amazon ECS deployment is complete. </p>"""
    test_traffic_route: NotRequired["capo_codedeploy.types.traffic_route.TrafficRoute"]
    """<p> An optional path used by a load balancer to route test traffic after an Amazon ECS deployment. Validation can occur while test traffic is served during a deployment. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetGroupPairInfo) -> dict:
    out: dict = {}
    if "target_groups" in value:
        import capo_codedeploy.types.target_group_info_list

        out["targetGroups"] = (
            capo_codedeploy.types.target_group_info_list.serialize_aws_json_1_1(
                value["target_groups"]
            )
        )
    if "prod_traffic_route" in value:
        import capo_codedeploy.types.traffic_route

        out["prodTrafficRoute"] = (
            capo_codedeploy.types.traffic_route.serialize_aws_json_1_1(
                value["prod_traffic_route"]
            )
        )
    if "test_traffic_route" in value:
        import capo_codedeploy.types.traffic_route

        out["testTrafficRoute"] = (
            capo_codedeploy.types.traffic_route.serialize_aws_json_1_1(
                value["test_traffic_route"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetGroupPairInfo:
    out: TargetGroupPairInfo = {}  # type: ignore[typeddict-item]
    if data.get("targetGroups") is not None:
        import capo_codedeploy.types.target_group_info_list

        out["target_groups"] = (
            capo_codedeploy.types.target_group_info_list.deserialize_aws_json_1_1(
                data["targetGroups"]
            )
        )
    if data.get("prodTrafficRoute") is not None:
        import capo_codedeploy.types.traffic_route

        out["prod_traffic_route"] = (
            capo_codedeploy.types.traffic_route.deserialize_aws_json_1_1(
                data["prodTrafficRoute"]
            )
        )
    if data.get("testTrafficRoute") is not None:
        import capo_codedeploy.types.traffic_route

        out["test_traffic_route"] = (
            capo_codedeploy.types.traffic_route.deserialize_aws_json_1_1(
                data["testTrafficRoute"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetGroupPairInfo) -> dict:
    out: dict = {}
    if "target_groups" in value:
        import capo_codedeploy.types.target_group_info_list

        out["targetGroups"] = (
            capo_codedeploy.types.target_group_info_list.serialize_cbor(
                value["target_groups"]
            )
        )
    if "prod_traffic_route" in value:
        import capo_codedeploy.types.traffic_route

        out["prodTrafficRoute"] = capo_codedeploy.types.traffic_route.serialize_cbor(
            value["prod_traffic_route"]
        )
    if "test_traffic_route" in value:
        import capo_codedeploy.types.traffic_route

        out["testTrafficRoute"] = capo_codedeploy.types.traffic_route.serialize_cbor(
            value["test_traffic_route"]
        )
    return out


def deserialize_cbor(data: dict) -> TargetGroupPairInfo:
    out: TargetGroupPairInfo = {}  # type: ignore[typeddict-item]
    if data.get("targetGroups") is not None:
        import capo_codedeploy.types.target_group_info_list

        out["target_groups"] = (
            capo_codedeploy.types.target_group_info_list.deserialize_cbor(
                data["targetGroups"]
            )
        )
    if data.get("prodTrafficRoute") is not None:
        import capo_codedeploy.types.traffic_route

        out["prod_traffic_route"] = (
            capo_codedeploy.types.traffic_route.deserialize_cbor(
                data["prodTrafficRoute"]
            )
        )
    if data.get("testTrafficRoute") is not None:
        import capo_codedeploy.types.traffic_route

        out["test_traffic_route"] = (
            capo_codedeploy.types.traffic_route.deserialize_cbor(
                data["testTrafficRoute"]
            )
        )
    return out
