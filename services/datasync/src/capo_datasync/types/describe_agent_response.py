"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.agent_arn
    import capo_datasync.types.agent_status
    import capo_datasync.types.endpoint_type
    import capo_datasync.types.platform
    import capo_datasync.types.private_link_config
    import capo_datasync.types.tag_value
    import capo_datasync.types.time


class DescribeAgentResponse(TypedDict, closed=True):
    agent_arn: NotRequired["capo_datasync.types.agent_arn.AgentArn"]
    """<p>The ARN of the agent.</p>"""
    name: NotRequired["capo_datasync.types.tag_value.TagValue"]
    """<p>The name of the agent.</p>"""
    status: NotRequired["capo_datasync.types.agent_status.AgentStatus"]
    """<p>The status of the agent.</p> <ul> <li> <p>If the status is <code>ONLINE</code>, the agent is configured properly and ready to use.</p> </li> <li> <p>If the status is <code>OFFLINE</code>, the agent has been out of contact with DataSync for five minutes or longer. This can happen for a few reasons. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-agents.html#troubleshoot-agent-offline">What do I do if my agent is offline?</a> </p> </li> </ul>"""
    last_connection_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The last time that the agent was communicating with the DataSync service.</p>"""
    creation_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time that the agent was <a href="https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html">activated</a>.</p>"""
    endpoint_type: NotRequired["capo_datasync.types.endpoint_type.EndpointType"]
    """<p>The type of <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html">service endpoint</a> that your agent is connected to.</p>"""
    private_link_config: NotRequired[
        "capo_datasync.types.private_link_config.PrivateLinkConfig"
    ]
    """<p>The network configuration that the agent uses when connecting to a <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html#choose-service-endpoint-vpc">VPC service endpoint</a>.</p>"""
    platform: NotRequired["capo_datasync.types.platform.Platform"]
    """<p>The platform-related details about the agent, such as the version number.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAgentResponse) -> dict:
    out: dict = {}
    if "agent_arn" in value:
        out["AgentArn"] = value["agent_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_datasync.types.agent_status

        out["Status"] = capo_datasync.types.agent_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "last_connection_time" in value:
        import capo_datasync.types.time

        out["LastConnectionTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["last_connection_time"]
        )
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "endpoint_type" in value:
        import capo_datasync.types.endpoint_type

        out["EndpointType"] = capo_datasync.types.endpoint_type.serialize_aws_json_1_1(
            value["endpoint_type"]
        )
    if "private_link_config" in value:
        import capo_datasync.types.private_link_config

        out["PrivateLinkConfig"] = (
            capo_datasync.types.private_link_config.serialize_aws_json_1_1(
                value["private_link_config"]
            )
        )
    if "platform" in value:
        import capo_datasync.types.platform

        out["Platform"] = capo_datasync.types.platform.serialize_aws_json_1_1(
            value["platform"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAgentResponse:
    out: DescribeAgentResponse = {}  # type: ignore[typeddict-item]
    if data.get("AgentArn") is not None:
        out["agent_arn"] = data["AgentArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_datasync.types.agent_status

        out["status"] = capo_datasync.types.agent_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("LastConnectionTime") is not None:
        import capo_datasync.types.time

        out["last_connection_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["LastConnectionTime"]
        )
    if data.get("CreationTime") is not None:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("EndpointType") is not None:
        import capo_datasync.types.endpoint_type

        out["endpoint_type"] = (
            capo_datasync.types.endpoint_type.deserialize_aws_json_1_1(
                data["EndpointType"]
            )
        )
    if data.get("PrivateLinkConfig") is not None:
        import capo_datasync.types.private_link_config

        out["private_link_config"] = (
            capo_datasync.types.private_link_config.deserialize_aws_json_1_1(
                data["PrivateLinkConfig"]
            )
        )
    if data.get("Platform") is not None:
        import capo_datasync.types.platform

        out["platform"] = capo_datasync.types.platform.deserialize_aws_json_1_1(
            data["Platform"]
        )
    return out
