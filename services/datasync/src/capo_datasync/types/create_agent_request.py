"""Generated from Smithy shape ``com.amazonaws.datasync#CreateAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.activation_key
    import capo_datasync.types.input_tag_list
    import capo_datasync.types.pl_security_group_arn_list
    import capo_datasync.types.pl_subnet_arn_list
    import capo_datasync.types.tag_value
    import capo_datasync.types.vpc_endpoint_id


class CreateAgentRequest(TypedDict, closed=True):
    activation_key: "capo_datasync.types.activation_key.ActivationKey"
    """<p>Specifies your DataSync agent's activation key. If you don't have an activation key, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html">Activating your agent</a>.</p>"""
    agent_name: NotRequired["capo_datasync.types.tag_value.TagValue"]
    """<p>Specifies a name for your agent. We recommend specifying a name that you can remember.</p>"""
    tags: NotRequired["capo_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least one tag for your agent.</p>"""
    vpc_endpoint_id: NotRequired["capo_datasync.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>Specifies the ID of the <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html#datasync-in-vpc">VPC service endpoint</a> that you're using. For example, a VPC endpoint ID looks like <code>vpce-01234d5aff67890e1</code>.</p> <important> <p>The VPC service endpoint you use must include the DataSync service name (for example, <code>com.amazonaws.us-east-2.datasync</code>).</p> </important>"""
    subnet_arns: NotRequired["capo_datasync.types.pl_subnet_arn_list.PLSubnetArnList"]
    """<p>Specifies the ARN of the subnet where your VPC service endpoint is located. You can only specify one ARN.</p>"""
    security_group_arns: NotRequired[
        "capo_datasync.types.pl_security_group_arn_list.PLSecurityGroupArnList"
    ]
    """<p>Specifies the Amazon Resource Name (ARN) of the security group that allows traffic between your agent and VPC service endpoint. You can only specify one ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAgentRequest) -> dict:
    out: dict = {}
    out["ActivationKey"] = value["activation_key"]
    if "agent_name" in value:
        out["AgentName"] = value["agent_name"]
    if "tags" in value:
        import capo_datasync.types.input_tag_list

        out["Tags"] = capo_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "subnet_arns" in value:
        import capo_datasync.types.pl_subnet_arn_list

        out["SubnetArns"] = (
            capo_datasync.types.pl_subnet_arn_list.serialize_aws_json_1_1(
                value["subnet_arns"]
            )
        )
    if "security_group_arns" in value:
        import capo_datasync.types.pl_security_group_arn_list

        out["SecurityGroupArns"] = (
            capo_datasync.types.pl_security_group_arn_list.serialize_aws_json_1_1(
                value["security_group_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAgentRequest:
    out: CreateAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("ActivationKey") is not None:
        out["activation_key"] = data["ActivationKey"]
    else:
        raise DeserializationError("CreateAgentRequest.activation_key required")
    if data.get("AgentName") is not None:
        out["agent_name"] = data["AgentName"]
    if data.get("Tags") is not None:
        import capo_datasync.types.input_tag_list

        out["tags"] = capo_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if data.get("SubnetArns") is not None:
        import capo_datasync.types.pl_subnet_arn_list

        out["subnet_arns"] = (
            capo_datasync.types.pl_subnet_arn_list.deserialize_aws_json_1_1(
                data["SubnetArns"]
            )
        )
    if data.get("SecurityGroupArns") is not None:
        import capo_datasync.types.pl_security_group_arn_list

        out["security_group_arns"] = (
            capo_datasync.types.pl_security_group_arn_list.deserialize_aws_json_1_1(
                data["SecurityGroupArns"]
            )
        )
    return out
