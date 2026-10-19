"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateEndpointAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.owner_account
    import capo_redshift_serverless.types.subnet_id_list
    import capo_redshift_serverless.types.vpc_security_group_id_list


class CreateEndpointAccessRequest(TypedDict, closed=True):
    endpoint_name: "str"
    """<p>The name of the VPC endpoint. An endpoint name must contain 1-30 characters. Valid characters are A-Z, a-z, 0-9, and hyphen(-). The first character must be a letter. The name can't contain two consecutive hyphens or end with a hyphen.</p>"""
    subnet_ids: "capo_redshift_serverless.types.subnet_id_list.SubnetIdList"
    """<p>The unique identifers of subnets from which Amazon Redshift Serverless chooses one to deploy a VPC endpoint.</p>"""
    workgroup_name: "str"
    """<p>The name of the workgroup to associate with the VPC endpoint.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>The unique identifiers of the security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>"""
    owner_account: NotRequired[
        "capo_redshift_serverless.types.owner_account.OwnerAccount"
    ]
    """<p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointAccessRequest) -> dict:
    out: dict = {}
    out["endpointName"] = value["endpoint_name"]
    import capo_redshift_serverless.types.subnet_id_list

    out["subnetIds"] = (
        capo_redshift_serverless.types.subnet_id_list.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    )
    out["workgroupName"] = value["workgroup_name"]
    if "vpc_security_group_ids" in value:
        import capo_redshift_serverless.types.vpc_security_group_id_list

        out["vpcSecurityGroupIds"] = (
            capo_redshift_serverless.types.vpc_security_group_id_list.serialize_aws_json_1_1(
                value["vpc_security_group_ids"]
            )
        )
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointAccessRequest:
    out: CreateEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    if data.get("endpointName") is not None:
        out["endpoint_name"] = data["endpointName"]
    else:
        out["endpoint_name"] = ""
    if data.get("subnetIds") is not None:
        import capo_redshift_serverless.types.subnet_id_list

        out["subnet_ids"] = (
            capo_redshift_serverless.types.subnet_id_list.deserialize_aws_json_1_1(
                data["subnetIds"]
            )
        )
    else:
        out["subnet_ids"] = []
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    else:
        out["workgroup_name"] = ""
    if data.get("vpcSecurityGroupIds") is not None:
        import capo_redshift_serverless.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_redshift_serverless.types.vpc_security_group_id_list.deserialize_aws_json_1_1(
                data["vpcSecurityGroupIds"]
            )
        )
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    return out
