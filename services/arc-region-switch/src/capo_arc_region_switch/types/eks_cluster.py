"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EksCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.eks_cluster_arn
    import capo_arc_region_switch.types.iam_role_arn


class EksCluster(TypedDict, closed=True):
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    cluster_arn: "capo_arc_region_switch.types.eks_cluster_arn.EksClusterArn"
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services EKS cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EksCluster) -> dict:
    out: dict = {}
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["clusterArn"] = value["cluster_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EksCluster:
    out: EksCluster = {}  # type: ignore[typeddict-item]
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    else:
        out["cluster_arn"] = ""
    return out
