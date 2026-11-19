"""Generated from Smithy shape ``com.amazonaws.codedeploy#ECSService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.ecs_cluster_name
    import capo_codedeploy.types.ecs_service_name


class ECSService(TypedDict, closed=True):
    service_name: NotRequired["capo_codedeploy.types.ecs_service_name.ECSServiceName"]
    """<p> The name of the target Amazon ECS service. </p>"""
    cluster_name: NotRequired["capo_codedeploy.types.ecs_cluster_name.ECSClusterName"]
    """<p> The name of the cluster that the Amazon ECS service is associated with. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ECSService) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ECSService:
    out: ECSService = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSService) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    return out


def deserialize_cbor(data: dict) -> ECSService:
    out: ECSService = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    return out
