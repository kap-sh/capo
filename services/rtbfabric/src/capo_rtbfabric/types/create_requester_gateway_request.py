"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateRequesterGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.security_group_id_list
    import capo_rtbfabric.types.subnet_id_list
    import capo_rtbfabric.types.tags_map
    import capo_rtbfabric.types.vpc_id


class CreateRequesterGatewayRequest(TypedDict, closed=True):
    vpc_id: "capo_rtbfabric.types.vpc_id.VpcId"
    """<p>The unique identifier of the Virtual Private Cloud (VPC).</p>"""
    subnet_ids: "capo_rtbfabric.types.subnet_id_list.SubnetIdList"
    """<p>The unique identifiers of the subnets.</p>"""
    security_group_ids: (
        "capo_rtbfabric.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The unique identifiers of the security groups.</p>"""
    client_token: "str"
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    description: NotRequired["str"]
    """<p>An optional description for the requester gateway.</p>"""
    tags: NotRequired["capo_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRequesterGatewayRequest) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import capo_rtbfabric.types.subnet_id_list

    out["subnetIds"] = capo_rtbfabric.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    import capo_rtbfabric.types.security_group_id_list

    out["securityGroupIds"] = (
        capo_rtbfabric.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRequesterGatewayRequest:
    out: CreateRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("CreateRequesterGatewayRequest.vpc_id required")
    if data.get("subnetIds") is not None:
        import capo_rtbfabric.types.subnet_id_list

        out["subnet_ids"] = capo_rtbfabric.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("CreateRequesterGatewayRequest.subnet_ids required")
    if data.get("securityGroupIds") is not None:
        import capo_rtbfabric.types.security_group_id_list

        out["security_group_ids"] = (
            capo_rtbfabric.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRequesterGatewayRequest.security_group_ids required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "CreateRequesterGatewayRequest.client_token required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    return out
