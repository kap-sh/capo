"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSourceVpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.security_group_ids
    import capo_qbusiness.types.subnet_ids


class DataSourceVpcConfiguration(TypedDict, closed=True):
    subnet_ids: "capo_qbusiness.types.subnet_ids.SubnetIds"
    """<p>A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.</p>"""
    security_group_ids: "capo_qbusiness.types.security_group_ids.SecurityGroupIds"
    """<p>A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Q Business to connect to the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceVpcConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.subnet_ids

    out["subnetIds"] = capo_qbusiness.types.subnet_ids.serialize_json(
        value["subnet_ids"]
    )
    import capo_qbusiness.types.security_group_ids

    out["securityGroupIds"] = capo_qbusiness.types.security_group_ids.serialize_json(
        value["security_group_ids"]
    )
    return out


def deserialize_json(data: dict) -> DataSourceVpcConfiguration:
    out: DataSourceVpcConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("subnetIds") is not None:
        import capo_qbusiness.types.subnet_ids

        out["subnet_ids"] = capo_qbusiness.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("securityGroupIds") is not None:
        import capo_qbusiness.types.security_group_ids

        out["security_group_ids"] = (
            capo_qbusiness.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        out["security_group_ids"] = []
    return out
