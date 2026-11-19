"""Generated from Smithy shape ``com.amazonaws.memorydb#SubnetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.network_type_list
    import capo_memorydb.types.string
    import capo_memorydb.types.subnet_list


class SubnetGroup(TypedDict, closed=True):
    name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the subnet group</p>"""
    description: NotRequired["capo_memorydb.types.string.String"]
    """<p>A description of the subnet group</p>"""
    vpc_id: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.</p>"""
    subnets: NotRequired["capo_memorydb.types.subnet_list.SubnetList"]
    """<p>A list of subnets associated with the subnet group.</p>"""
    arn: NotRequired["capo_memorydb.types.string.String"]
    """<p>The ARN (Amazon Resource Name) of the subnet group.</p>"""
    supported_network_types: NotRequired[
        "capo_memorydb.types.network_type_list.NetworkTypeList"
    ]
    """<p>The network types supported by this subnet group. Returns an array of strings that can include 'ipv4', 'ipv6', or both, indicating the IP address types that can be used for clusters deployed in this subnet group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnets" in value:
        import capo_memorydb.types.subnet_list

        out["Subnets"] = capo_memorydb.types.subnet_list.serialize_aws_json_1_1(
            value["subnets"]
        )
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "supported_network_types" in value:
        import capo_memorydb.types.network_type_list

        out["SupportedNetworkTypes"] = (
            capo_memorydb.types.network_type_list.serialize_aws_json_1_1(
                value["supported_network_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubnetGroup:
    out: SubnetGroup = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("Subnets") is not None:
        import capo_memorydb.types.subnet_list

        out["subnets"] = capo_memorydb.types.subnet_list.deserialize_aws_json_1_1(
            data["Subnets"]
        )
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("SupportedNetworkTypes") is not None:
        import capo_memorydb.types.network_type_list

        out["supported_network_types"] = (
            capo_memorydb.types.network_type_list.deserialize_aws_json_1_1(
                data["SupportedNetworkTypes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubnetGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnets" in value:
        import capo_memorydb.types.subnet_list

        out["Subnets"] = capo_memorydb.types.subnet_list.serialize_cbor(
            value["subnets"]
        )
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "supported_network_types" in value:
        import capo_memorydb.types.network_type_list

        out["SupportedNetworkTypes"] = (
            capo_memorydb.types.network_type_list.serialize_cbor(
                value["supported_network_types"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> SubnetGroup:
    out: SubnetGroup = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("Subnets") is not None:
        import capo_memorydb.types.subnet_list

        out["subnets"] = capo_memorydb.types.subnet_list.deserialize_cbor(
            data["Subnets"]
        )
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("SupportedNetworkTypes") is not None:
        import capo_memorydb.types.network_type_list

        out["supported_network_types"] = (
            capo_memorydb.types.network_type_list.deserialize_cbor(
                data["SupportedNetworkTypes"]
            )
        )
    return out
