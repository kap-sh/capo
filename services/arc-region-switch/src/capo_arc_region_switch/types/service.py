"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Service``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.ecs_cluster_arn
    import capo_arc_region_switch.types.ecs_service_arn
    import capo_arc_region_switch.types.iam_role_arn


class Service(TypedDict, closed=True):
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for a service.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the service.</p>"""
    cluster_arn: NotRequired[
        "capo_arc_region_switch.types.ecs_cluster_arn.EcsClusterArn"
    ]
    """<p>The cluster Amazon Resource Name (ARN) for a service.</p>"""
    service_arn: NotRequired[
        "capo_arc_region_switch.types.ecs_service_arn.EcsServiceArn"
    ]
    """<p>The Amazon Resource Name (ARN) for a service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Service) -> dict:
    out: dict = {}
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Service) -> dict:
    out: dict = {}
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    return out


def deserialize_cbor(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    return out
