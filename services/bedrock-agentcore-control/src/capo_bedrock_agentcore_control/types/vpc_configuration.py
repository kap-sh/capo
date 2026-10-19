"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#VpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.security_group_id_list
    import capo_bedrock_agentcore_control.types.subnet_id_list


class VpcConfiguration(TypedDict, closed=True):
    subnets: "capo_bedrock_agentcore_control.types.subnet_id_list.SubnetIdList"
    """<p>The IDs of the subnets in which to launch instances. You must specify at least one subnet.</p>"""
    security_groups: "capo_bedrock_agentcore_control.types.security_group_id_list.SecurityGroupIdList"
    """<p>The IDs of the security groups to associate with the instances. You must specify at least one security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.subnet_id_list

    out["subnets"] = capo_bedrock_agentcore_control.types.subnet_id_list.serialize_json(
        value["subnets"]
    )
    import capo_bedrock_agentcore_control.types.security_group_id_list

    out["securityGroups"] = (
        capo_bedrock_agentcore_control.types.security_group_id_list.serialize_json(
            value["security_groups"]
        )
    )
    return out


def deserialize_json(data: dict) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("subnets") is not None:
        import capo_bedrock_agentcore_control.types.subnet_id_list

        out["subnets"] = (
            capo_bedrock_agentcore_control.types.subnet_id_list.deserialize_json(
                data["subnets"]
            )
        )
    else:
        out["subnets"] = []
    if data.get("securityGroups") is not None:
        import capo_bedrock_agentcore_control.types.security_group_id_list

        out["security_groups"] = (
            capo_bedrock_agentcore_control.types.security_group_id_list.deserialize_json(
                data["securityGroups"]
            )
        )
    else:
        out["security_groups"] = []
    return out
