"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceVpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.security_group_id_list
    import capo_kendra.types.subnet_id_list


class DataSourceVpcConfiguration(TypedDict, closed=True):
    subnet_ids: "capo_kendra.types.subnet_id_list.SubnetIdList"
    """<p>A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.</p>"""
    security_group_ids: "capo_kendra.types.security_group_id_list.SecurityGroupIdList"
    """<p>A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceVpcConfiguration) -> dict:
    out: dict = {}
    import capo_kendra.types.subnet_id_list

    out["SubnetIds"] = capo_kendra.types.subnet_id_list.serialize_aws_json_1_1(
        value["subnet_ids"]
    )
    import capo_kendra.types.security_group_id_list

    out["SecurityGroupIds"] = (
        capo_kendra.types.security_group_id_list.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSourceVpcConfiguration:
    out: DataSourceVpcConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SubnetIds") is not None:
        import capo_kendra.types.subnet_id_list

        out["subnet_ids"] = capo_kendra.types.subnet_id_list.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("SecurityGroupIds") is not None:
        import capo_kendra.types.security_group_id_list

        out["security_group_ids"] = (
            capo_kendra.types.security_group_id_list.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    else:
        out["security_group_ids"] = []
    return out
