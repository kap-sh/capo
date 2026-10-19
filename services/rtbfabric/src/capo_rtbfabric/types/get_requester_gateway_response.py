"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetRequesterGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rtbfabric.types.domain_name
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.requester_gateway_status
    import capo_rtbfabric.types.security_group_id_list
    import capo_rtbfabric.types.subnet_id_list
    import capo_rtbfabric.types.tags_map
    import capo_rtbfabric.types.vpc_id


class GetRequesterGatewayResponse(TypedDict, closed=True):
    status: "capo_rtbfabric.types.requester_gateway_status.RequesterGatewayStatus"
    """<p>The status of the request.</p>"""
    domain_name: "capo_rtbfabric.types.domain_name.DomainName"
    """<p>The domain name of the requester gateway.</p>"""
    description: NotRequired["str"]
    """<p>The description of the requester gateway.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the requester gateway was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the requester gateway was updated.</p>"""
    vpc_id: "capo_rtbfabric.types.vpc_id.VpcId"
    """<p>The unique identifier of the Virtual Private Cloud (VPC).</p>"""
    subnet_ids: "capo_rtbfabric.types.subnet_id_list.SubnetIdList"
    """<p>The unique identifiers of the subnets.</p>"""
    security_group_ids: (
        "capo_rtbfabric.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The unique identifiers of the security groups.</p>"""
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    tags: NotRequired["capo_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs for the tag or tags assigned to the specified resource.</p>"""
    active_links_count: NotRequired["int"]
    """<p>The count of active links for the requester gateway.</p>"""
    total_links_count: NotRequired["int"]
    """<p>The total count of links for the requester gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRequesterGatewayResponse) -> dict:
    out: dict = {}
    import capo_rtbfabric.types.requester_gateway_status

    out["status"] = capo_rtbfabric.types.requester_gateway_status.serialize_json(
        value["status"]
    )
    out["domainName"] = value["domain_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_rtbfabric.types._prelude.timestamp

        out["createdAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_rtbfabric.types._prelude.timestamp

        out["updatedAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
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
    out["gatewayId"] = value["gateway_id"]
    if "tags" in value:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.serialize_json(value["tags"])
    if "active_links_count" in value:
        out["activeLinksCount"] = value["active_links_count"]
    if "total_links_count" in value:
        out["totalLinksCount"] = value["total_links_count"]
    return out


def deserialize_json(data: dict) -> GetRequesterGatewayResponse:
    out: GetRequesterGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_rtbfabric.types.requester_gateway_status

        out["status"] = capo_rtbfabric.types.requester_gateway_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_rtbfabric.types.requester_gateway_status.RequesterGatewayStatus", ""
        )
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_rtbfabric.types._prelude.timestamp

        out["created_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_rtbfabric.types._prelude.timestamp

        out["updated_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("subnetIds") is not None:
        import capo_rtbfabric.types.subnet_id_list

        out["subnet_ids"] = capo_rtbfabric.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("securityGroupIds") is not None:
        import capo_rtbfabric.types.security_group_id_list

        out["security_group_ids"] = (
            capo_rtbfabric.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        out["security_group_ids"] = []
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    else:
        out["gateway_id"] = ""
    if data.get("tags") is not None:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    if data.get("activeLinksCount") is not None:
        out["active_links_count"] = data["activeLinksCount"]
    if data.get("totalLinksCount") is not None:
        out["total_links_count"] = data["totalLinksCount"]
    return out
