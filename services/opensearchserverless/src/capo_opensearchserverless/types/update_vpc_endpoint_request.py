"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateVpcEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.security_group_ids
    import capo_opensearchserverless.types.subnet_ids
    import capo_opensearchserverless.types.vpc_endpoint_id


class UpdateVpcEndpointRequest(TypedDict, closed=True):
    id: "capo_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId"
    """<p>The unique identifier of the interface endpoint to update.</p>"""
    add_subnet_ids: NotRequired["capo_opensearchserverless.types.subnet_ids.SubnetIds"]
    """<p>The ID of one or more subnets to add to the endpoint.</p>"""
    remove_subnet_ids: NotRequired[
        "capo_opensearchserverless.types.subnet_ids.SubnetIds"
    ]
    """<p>The unique identifiers of the subnets to remove from the endpoint.</p>"""
    add_security_group_ids: NotRequired[
        "capo_opensearchserverless.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The unique identifiers of the security groups to add to the endpoint. Security groups define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>"""
    remove_security_group_ids: NotRequired[
        "capo_opensearchserverless.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The unique identifiers of the security groups to remove from the endpoint.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateVpcEndpointRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "add_subnet_ids" in value:
        import capo_opensearchserverless.types.subnet_ids

        out["addSubnetIds"] = (
            capo_opensearchserverless.types.subnet_ids.serialize_aws_json_1_0(
                value["add_subnet_ids"]
            )
        )
    if "remove_subnet_ids" in value:
        import capo_opensearchserverless.types.subnet_ids

        out["removeSubnetIds"] = (
            capo_opensearchserverless.types.subnet_ids.serialize_aws_json_1_0(
                value["remove_subnet_ids"]
            )
        )
    if "add_security_group_ids" in value:
        import capo_opensearchserverless.types.security_group_ids

        out["addSecurityGroupIds"] = (
            capo_opensearchserverless.types.security_group_ids.serialize_aws_json_1_0(
                value["add_security_group_ids"]
            )
        )
    if "remove_security_group_ids" in value:
        import capo_opensearchserverless.types.security_group_ids

        out["removeSecurityGroupIds"] = (
            capo_opensearchserverless.types.security_group_ids.serialize_aws_json_1_0(
                value["remove_security_group_ids"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateVpcEndpointRequest:
    out: UpdateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("addSubnetIds") is not None:
        import capo_opensearchserverless.types.subnet_ids

        out["add_subnet_ids"] = (
            capo_opensearchserverless.types.subnet_ids.deserialize_aws_json_1_0(
                data["addSubnetIds"]
            )
        )
    if data.get("removeSubnetIds") is not None:
        import capo_opensearchserverless.types.subnet_ids

        out["remove_subnet_ids"] = (
            capo_opensearchserverless.types.subnet_ids.deserialize_aws_json_1_0(
                data["removeSubnetIds"]
            )
        )
    if data.get("addSecurityGroupIds") is not None:
        import capo_opensearchserverless.types.security_group_ids

        out["add_security_group_ids"] = (
            capo_opensearchserverless.types.security_group_ids.deserialize_aws_json_1_0(
                data["addSecurityGroupIds"]
            )
        )
    if data.get("removeSecurityGroupIds") is not None:
        import capo_opensearchserverless.types.security_group_ids

        out["remove_security_group_ids"] = (
            capo_opensearchserverless.types.security_group_ids.deserialize_aws_json_1_0(
                data["removeSecurityGroupIds"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
