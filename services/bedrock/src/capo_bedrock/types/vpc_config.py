"""Generated from Smithy shape ``com.amazonaws.bedrock#VpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.security_group_ids
    import capo_bedrock.types.subnet_ids


class VpcConfig(TypedDict, closed=True):
    subnet_ids: "capo_bedrock.types.subnet_ids.SubnetIds"
    """<p>An array of IDs for each subnet in the VPC to use.</p>"""
    security_group_ids: "capo_bedrock.types.security_group_ids.SecurityGroupIds"
    """<p>An array of IDs for each security group in the VPC to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.subnet_ids

    out["subnetIds"] = capo_bedrock.types.subnet_ids.serialize_json(value["subnet_ids"])
    import capo_bedrock.types.security_group_ids

    out["securityGroupIds"] = capo_bedrock.types.security_group_ids.serialize_json(
        value["security_group_ids"]
    )
    return out


def deserialize_json(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if data.get("subnetIds") is not None:
        import capo_bedrock.types.subnet_ids

        out["subnet_ids"] = capo_bedrock.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("securityGroupIds") is not None:
        import capo_bedrock.types.security_group_ids

        out["security_group_ids"] = (
            capo_bedrock.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        out["security_group_ids"] = []
    return out
