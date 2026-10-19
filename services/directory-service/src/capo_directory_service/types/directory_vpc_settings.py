"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryVpcSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.subnet_ids
    import capo_directory_service.types.vpc_id


class DirectoryVpcSettings(TypedDict, closed=True):
    vpc_id: "capo_directory_service.types.vpc_id.VpcId"
    """<p>The identifier of the VPC in which to create the directory.</p>"""
    subnet_ids: "capo_directory_service.types.subnet_ids.SubnetIds"
    """<p>The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. Directory Service creates a directory server and a DNS server in each of these subnets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryVpcSettings) -> dict:
    out: dict = {}
    out["VpcId"] = value["vpc_id"]
    import capo_directory_service.types.subnet_ids

    out["SubnetIds"] = capo_directory_service.types.subnet_ids.serialize_aws_json_1_1(
        value["subnet_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryVpcSettings:
    out: DirectoryVpcSettings = {}  # type: ignore[typeddict-item]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("SubnetIds") is not None:
        import capo_directory_service.types.subnet_ids

        out["subnet_ids"] = (
            capo_directory_service.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    else:
        out["subnet_ids"] = []
    return out
