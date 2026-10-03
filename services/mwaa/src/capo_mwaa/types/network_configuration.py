"""Generated from Smithy shape ``com.amazonaws.mwaa#NetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.security_group_list
    import capo_mwaa.types.subnet_list


class NetworkConfiguration(TypedDict, closed=True):
    subnet_ids: NotRequired["capo_mwaa.types.subnet_list.SubnetList"]
    """<p>A list of subnet IDs. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html">About networking on Amazon MWAA</a>.</p>"""
    security_group_ids: NotRequired[
        "capo_mwaa.types.security_group_list.SecurityGroupList"
    ]
    """<p>A list of security group IDs. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-security.html">Security in your VPC on Amazon MWAA</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConfiguration) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import capo_mwaa.types.subnet_list

        out["SubnetIds"] = capo_mwaa.types.subnet_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_mwaa.types.security_group_list

        out["SecurityGroupIds"] = capo_mwaa.types.security_group_list.serialize_json(
            value["security_group_ids"]
        )
    return out


def deserialize_json(data: dict) -> NetworkConfiguration:
    out: NetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SubnetIds") is not None:
        import capo_mwaa.types.subnet_list

        out["subnet_ids"] = capo_mwaa.types.subnet_list.deserialize_json(
            data["SubnetIds"]
        )
    if data.get("SecurityGroupIds") is not None:
        import capo_mwaa.types.security_group_list

        out["security_group_ids"] = (
            capo_mwaa.types.security_group_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    return out
