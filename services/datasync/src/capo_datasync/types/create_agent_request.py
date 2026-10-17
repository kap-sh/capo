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
    """<p>Specifies the ID of the <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html#datasync-in-vpc">VPC service endpoint</a> that you're using. For example, a VPC endpoint ID looks like <code>vpce-01234d5aff67890e1</code>.</p> <important> <p>The VPC service endpoint you use must include the DataSync service name (for example, <code>com.amazonaws.us-east-2.datasync</code>).</p> </important> <p>The endpoint ID is informational. DataSync doesn't verify it or use it to connect to your agent. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html#vpc-endpoint-multiple-subnets">Using a single VPC service endpoint across multiple subnets</a>.</p>"""
    subnet_arns: NotRequired["capo_datasync.types.pl_subnet_arn_list.PLSubnetArnList"]
    """<p>Specifies the ARN of the subnet where DataSync creates the <a href="https://docs.aws.amazon.com/datasync/latest/userguide/required-network-interfaces.html">network interfaces</a> that handle data transfer traffic for your tasks. You can only specify one ARN.</p> <p>The subnet doesn't have to be the subnet that contains your VPC service endpoint. The subnet can be one that another Amazon Web Services account shared with you through <a href="https://docs.aws.amazon.com/ram/latest/userguide/what-is.html">RAM</a>, in which case the ARN must specify the account that owns the subnet. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html#vpc-endpoint-multiple-subnets">Using a single VPC service endpoint across multiple subnets</a>.</p>"""
    security_group_arns: NotRequired[
        "capo_datasync.types.pl_security_group_arn_list.PLSecurityGroupArnList"
    ]
    """<p>Specifies the Amazon Resource Name (ARN) of the security group that allows traffic between your agent and VPC service endpoint. You can only specify one ARN.</p> <p>The ARN must specify your own account, even when the security group was shared with you from the account that owns the VPC. The security group must belong to the same VPC as the subnet that you specify in <code>SubnetArns</code>.</p>"""


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
