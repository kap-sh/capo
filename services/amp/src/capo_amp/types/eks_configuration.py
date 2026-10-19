"""Generated from Smithy shape ``com.amazonaws.amp#EksConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.cluster_arn
    import capo_amp.types.security_group_ids
    import capo_amp.types.subnet_ids


class EksConfiguration(TypedDict, closed=True):
    cluster_arn: "capo_amp.types.cluster_arn.ClusterArn"
    """<p>ARN of the Amazon EKS cluster.</p>"""
    security_group_ids: NotRequired[
        "capo_amp.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of the security group IDs for the Amazon EKS cluster VPC configuration.</p>"""
    subnet_ids: "capo_amp.types.subnet_ids.SubnetIds"
    """<p>A list of subnet IDs for the Amazon EKS cluster VPC configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksConfiguration) -> dict:
    out: dict = {}
    out["clusterArn"] = value["cluster_arn"]
    if "security_group_ids" in value:
        import capo_amp.types.security_group_ids

        out["securityGroupIds"] = capo_amp.types.security_group_ids.serialize_json(
            value["security_group_ids"]
        )
    import capo_amp.types.subnet_ids

    out["subnetIds"] = capo_amp.types.subnet_ids.serialize_json(value["subnet_ids"])
    return out


def deserialize_json(data: dict) -> EksConfiguration:
    out: EksConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    else:
        out["cluster_arn"] = ""
    if data.get("securityGroupIds") is not None:
        import capo_amp.types.security_group_ids

        out["security_group_ids"] = capo_amp.types.security_group_ids.deserialize_json(
            data["securityGroupIds"]
        )
    if data.get("subnetIds") is not None:
        import capo_amp.types.subnet_ids

        out["subnet_ids"] = capo_amp.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    return out
