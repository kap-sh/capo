"""Generated from Smithy shape ``com.amazonaws.amp#VpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.security_group_ids
    import capo_amp.types.subnet_ids


class VpcConfiguration(TypedDict, closed=True):
    security_group_ids: "capo_amp.types.security_group_ids.SecurityGroupIds"
    """<p>The security group IDs that control network access for the Prometheus collector. These security groups must allow the collector to communicate with your Amazon MSK cluster on the required ports.</p>"""
    subnet_ids: "capo_amp.types.subnet_ids.SubnetIds"
    """<p>The subnet IDs where the Prometheus collector will be deployed. The subnets must be in the same Amazon VPC as your Amazon MSK cluster and have network connectivity to the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfiguration) -> dict:
    out: dict = {}
    import capo_amp.types.security_group_ids

    out["securityGroupIds"] = capo_amp.types.security_group_ids.serialize_json(
        value["security_group_ids"]
    )
    import capo_amp.types.subnet_ids

    out["subnetIds"] = capo_amp.types.subnet_ids.serialize_json(value["subnet_ids"])
    return out


def deserialize_json(data: dict) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("securityGroupIds") is not None:
        import capo_amp.types.security_group_ids

        out["security_group_ids"] = capo_amp.types.security_group_ids.deserialize_json(
            data["securityGroupIds"]
        )
    else:
        out["security_group_ids"] = []
    if data.get("subnetIds") is not None:
        import capo_amp.types.subnet_ids

        out["subnet_ids"] = capo_amp.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    return out
