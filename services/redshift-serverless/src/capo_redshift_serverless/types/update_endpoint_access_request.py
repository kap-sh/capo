"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateEndpointAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.vpc_security_group_id_list


class UpdateEndpointAccessRequest(TypedDict, closed=True):
    endpoint_name: "str"
    """<p>The name of the VPC endpoint to update.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>The list of VPC security groups associated with the endpoint after the endpoint is modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEndpointAccessRequest) -> dict:
    out: dict = {}
    out["endpointName"] = value["endpoint_name"]
    if "vpc_security_group_ids" in value:
        import capo_redshift_serverless.types.vpc_security_group_id_list

        out["vpcSecurityGroupIds"] = (
            capo_redshift_serverless.types.vpc_security_group_id_list.serialize_aws_json_1_1(
                value["vpc_security_group_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEndpointAccessRequest:
    out: UpdateEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    if data.get("endpointName") is not None:
        out["endpoint_name"] = data["endpointName"]
    else:
        out["endpoint_name"] = ""
    if data.get("vpcSecurityGroupIds") is not None:
        import capo_redshift_serverless.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_redshift_serverless.types.vpc_security_group_id_list.deserialize_aws_json_1_1(
                data["vpcSecurityGroupIds"]
            )
        )
    return out
