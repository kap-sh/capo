"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDeliverySourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.delivery_source_configuration
    import capo_cloudwatch_logs.types.delivery_source_name
    import capo_cloudwatch_logs.types.log_type
    import capo_cloudwatch_logs.types.tags


class PutDeliverySourceRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_logs.types.delivery_source_name.DeliverySourceName"
    """<p>A name for this delivery source. This name must be unique for all delivery sources in your account.</p>"""
    resource_arn: "capo_cloudwatch_logs.types.arn.Arn"
    """<p>The ARN of the Amazon Web Services resource that is generating and sending logs. For example, <code>arn:aws:workmail:us-east-1:123456789012:organization/m-1234EXAMPLEabcd1234abcd1234abcd1234</code> </p> <p>For the <code>SECURITY_FINDING_LOGS</code> logType, use a wildcard ARN for the hub resource. For Amazon Web Services Security Hub CSPM, use <code>arn:aws:securityhub:us-east-1:111122223333:hub/*</code> and for Amazon Web Services Security Hub, use <code>arn:aws:securityhub:us-east-1:111122223333:hubv2/*</code> </p>"""
    log_type: "capo_cloudwatch_logs.types.log_type.LogType"
    """<p>Defines the type of log that the source is sending.</p> <ul> <li> <p>For Application Load Balancer, the valid values are <code>ALB_ACCESS_LOGS</code>, <code>ALB_CONNECTION_LOGS</code>, and <code>ALB_HEALTH_CHECK_LOGS</code>.</p> </li> <li> <p>For Amazon Bedrock Agents, the valid values are <code>APPLICATION_LOGS</code> and <code>EVENT_LOGS</code>.</p> </li> <li> <p>For Amazon Bedrock Knowledge Bases, the valid values are <code>APPLICATION_LOGS</code> and <code>TRACES</code>.</p> </li> <li> <p>For Amazon Bedrock AgentCore Runtime, the valid values are <code>APPLICATION_LOGS</code>, <code>USAGE_LOGS</code> and <code>TRACES</code>.</p> </li> <li> <p>For Amazon Bedrock AgentCore Tools, the valid values are <code>APPLICATION_LOGS</code>, <code>USAGE_LOGS</code> and <code>TRACES</code>.</p> </li> <li> <p>For Amazon Bedrock AgentCore Identity, the valid values are <code>APPLICATION_LOGS</code> and <code>TRACES</code>.</p> </li> <li> <p>For Amazon Bedrock AgentCore Memory, the valid values are <code>APPLICATION_LOGS</code> and <code>TRACES</code>.</p> </li> <li> <p>For Amazon Bedrock AgentCore Gateway, the valid values are <code>APPLICATION_LOGS</code> and <code>TRACES</code>.</p> </li> <li> <p>For Amazon Bedrock AgentCore Payments, the valid values are <code>APPLICATION_LOGS</code> and <code>TRACES</code>.</p> </li> <li> <p>For CloudFront, the valid value is <code>ACCESS_LOGS</code>.</p> </li> <li> <p>For DevOps Agent, the valid value is <code>APPLICATION_LOGS</code>.</p> </li> <li> <p>For Amazon CodeWhisperer, the valid value is <code>EVENT_LOGS</code>.</p> </li> <li> <p>For Elemental MediaPackage, the valid values are <code>EGRESS_ACCESS_LOGS</code> and <code>INGRESS_ACCESS_LOGS</code>.</p> </li> <li> <p>For Elemental MediaTailor, the valid values are <code>AD_DECISION_SERVER_LOGS</code>, <code>MANIFEST_SERVICE_LOGS</code>, and <code>TRANSCODE_LOGS</code>.</p> </li> <li> <p>For Amazon EKS Auto Mode, the valid values are <code>AUTO_MODE_BLOCK_STORAGE_LOGS</code>, <code>AUTO_MODE_COMPUTE_LOGS</code>, <code>AUTO_MODE_IPAM_LOGS</code>, and <code>AUTO_MODE_LOAD_BALANCING_LOGS</code>.</p> </li> <li> <p>For Amazon EKS Capability Logs, the valid values are <code>EKS_CAPABILITY_ACK_LOGS</code>, <code>EKS_CAPABILITY_ARGOCD_APPLICATION_LOGS</code>, <code>EKS_CAPABILITY_ARGOCD_APPLICATIONSET_LOGS</code>, <code>EKS_CAPABILITY_ARGOCD_COMMITSERVER_LOGS</code>, <code>EKS_CAPABILITY_ARGOCD_REPOSERVER_LOGS</code>, <code>EKS_CAPABILITY_ARGOCD_SERVER_LOGS</code>, and <code>EKS_CAPABILITY_KRO_LOGS</code>.</p> </li> <li> <p>For Entity Resolution, the valid value is <code>WORKFLOW_LOGS</code>.</p> </li> <li> <p>For IAM Identity Center, the valid value is <code>ERROR_LOGS</code>.</p> </li> <li> <p>For Network Firewall Proxy, the valid values are <code>ALERT_LOGS</code>, <code>ALLOW_LOGS</code>, and <code>DENY_LOGS</code>.</p> </li> <li> <p>For Network Load Balancer, the valid value is <code>NLB_ACCESS_LOGS</code>.</p> </li> <li> <p>For PCS, the valid values are <code>PCS_SCHEDULER_LOGS</code>, <code>PCS_JOBCOMP_LOGS</code>, and <code>PCS_SCHEDULER_AUDIT_LOGS</code>.</p> </li> <li> <p>For Quick, the valid values are <code>AGENT_HOURS_LOGS</code>, <code>CHAT_LOGS</code>, <code>FEEDBACK_LOGS</code>, and <code>INDEX_USAGE_LOGS</code>.</p> </li> <li> <p>For Amazon Web Services RTB Fabric, the valid values is <code>APPLICATION_LOGS</code>.</p> </li> <li> <p>For Amazon Q, the valid values are <code>EVENT_LOGS</code> and <code>SYNC_JOB_LOGS</code>.</p> </li> <li> <p>For Amazon S3, the valid value is <code>S3_SERVER_ACCESS_LOGS</code>.</p> </li> <li> <p>For Amazon Web Services Security Hub CSPM, the valid value is <code>SECURITY_FINDING_LOGS</code>.</p> </li> <li> <p>For Amazon Web Services Security Hub, the valid value is <code>SECURITY_FINDING_LOGS</code>.</p> </li> <li> <p>For Amazon SES mail manager, the valid values are <code>APPLICATION_LOGS</code> and <code>TRAFFIC_POLICY_DEBUG_LOGS</code>.</p> </li> <li> <p>For Amazon WorkMail, the valid values are <code>ACCESS_CONTROL_LOGS</code>, <code>AUTHENTICATION_LOGS</code>, <code>WORKMAIL_AVAILABILITY_PROVIDER_LOGS</code>, <code>WORKMAIL_MAILBOX_ACCESS_LOGS</code>, and <code>WORKMAIL_PERSONAL_ACCESS_TOKEN_LOGS</code>.</p> </li> <li> <p>For Amazon VPC Route Server, the valid value is <code>EVENT_LOGS</code>.</p> </li> </ul>"""
    tags: NotRequired["capo_cloudwatch_logs.types.tags.Tags"]
    """<p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> </p>"""
    delivery_source_configuration: NotRequired[
        "capo_cloudwatch_logs.types.delivery_source_configuration.DeliverySourceConfiguration"
    ]
    """<p>A map of key-value pairs to configure the delivery source. Both keys and values must be between 1 and 255 characters in length. For example, <code>{"samplingRate": "50"}</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDeliverySourceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["resourceArn"] = value["resource_arn"]
    out["logType"] = value["log_type"]
    if "tags" in value:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "delivery_source_configuration" in value:
        import capo_cloudwatch_logs.types.delivery_source_configuration

        out["deliverySourceConfiguration"] = (
            capo_cloudwatch_logs.types.delivery_source_configuration.serialize_aws_json_1_1(
                value["delivery_source_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDeliverySourceRequest:
    out: PutDeliverySourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PutDeliverySourceRequest.name required")
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("PutDeliverySourceRequest.resource_arn required")
    if data.get("logType") is not None:
        out["log_type"] = data["logType"]
    else:
        raise DeserializationError("PutDeliverySourceRequest.log_type required")
    if data.get("tags") is not None:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("deliverySourceConfiguration") is not None:
        import capo_cloudwatch_logs.types.delivery_source_configuration

        out["delivery_source_configuration"] = (
            capo_cloudwatch_logs.types.delivery_source_configuration.deserialize_aws_json_1_1(
                data["deliverySourceConfiguration"]
            )
        )
    return out
