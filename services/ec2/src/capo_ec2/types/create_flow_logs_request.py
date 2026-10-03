"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFlowLogsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.destination_options_request
    import capo_ec2.types.flow_log_resource_ids
    import capo_ec2.types.flow_logs_resource_type
    import capo_ec2.types.integer
    import capo_ec2.types.log_destination_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_field_specification_list_request
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.traffic_type


class CreateFlowLogsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">How to ensure idempotency</a>.</p>"""
    deliver_logs_permission_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the IAM role that allows Amazon EC2 to publish flow logs to the log destination.</p> <p>This parameter is required if the destination type is <code>cloud-watch-logs</code>, or if the destination type is <code>kinesis-data-firehose</code> and the delivery stream and the resources to monitor are in different accounts.</p>"""
    deliver_cross_account_role: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the IAM role that allows Amazon EC2 to publish flow logs across accounts.</p>"""
    log_group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs.</p> <p>This parameter is valid only if the destination type is <code>cloud-watch-logs</code>.</p>"""
    resource_ids: NotRequired["capo_ec2.types.flow_log_resource_ids.FlowLogResourceIds"]
    """<p>The IDs of the resources to monitor. For example, if the resource type is <code>VPC</code>, specify the IDs of the VPCs.</p> <p>Constraints: Maximum of 25 for transit gateway resource types. Maximum of 300 for the other resource types.</p>"""
    resource_type: NotRequired[
        "capo_ec2.types.flow_logs_resource_type.FlowLogsResourceType"
    ]
    """<p>The type of resource to monitor.</p>"""
    traffic_type: NotRequired["capo_ec2.types.traffic_type.TrafficType"]
    """<p>The type of traffic to monitor (accepted traffic, rejected traffic, or all traffic). This parameter is not supported for transit gateway resource types. It is required for the other resource types.</p>"""
    log_destination_type: NotRequired[
        "capo_ec2.types.log_destination_type.LogDestinationType"
    ]
    """<p>The type of destination for the flow log data.</p> <p>Default: <code>cloud-watch-logs</code> </p>"""
    log_destination: NotRequired["capo_ec2.types.string.String"]
    """<p>The destination for the flow log data. The meaning of this parameter depends on the destination type.</p> <ul> <li> <p>If the destination type is <code>cloud-watch-logs</code>, specify the ARN of a CloudWatch Logs log group. For example:</p> <p>arn:aws:logs:<i>region</i>:<i>account_id</i>:log-group:<i>my_group</i> </p> <p>Alternatively, use the <code>LogGroupName</code> parameter.</p> </li> <li> <p>If the destination type is <code>s3</code>, specify the ARN of an S3 bucket. For example:</p> <p>arn:aws:s3:::<i>my_bucket</i>/<i>my_subfolder</i>/</p> <p>The subfolder is optional. Note that you can't use <code>AWSLogs</code> as a subfolder name.</p> </li> <li> <p>If the destination type is <code>kinesis-data-firehose</code>, specify the ARN of a Kinesis Data Firehose delivery stream. For example:</p> <p>arn:aws:firehose:<i>region</i>:<i>account_id</i>:deliverystream:<i>my_stream</i> </p> </li> </ul>"""
    log_format: NotRequired["capo_ec2.types.string.String"]
    """<p>The fields to include in the flow log record. List the fields in the order in which they should appear. If you omit this parameter, the flow log is created using the default format. If you specify this parameter, you must include at least one field. For more information about the available fields, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html">Flow log records</a> in the <i>Amazon VPC User Guide</i> or <a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html#flow-log-records">Transit Gateway Flow Log records</a> in the <i>Amazon Web Services Transit Gateway Guide</i>.</p> <p>Specify the fields using the <code>${field-id}</code> format, separated by spaces.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the flow logs.</p>"""
    max_aggregation_interval: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. The possible values are 60 seconds (1 minute) or 600 seconds (10 minutes). This parameter must be 60 seconds for transit gateway resource types.</p> <p>When a network interface is attached to a <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html">Nitro-based instance</a>, the aggregation interval is always 60 seconds or less, regardless of the value that you specify.</p> <p>Default: 600</p>"""
    destination_options: NotRequired[
        "capo_ec2.types.destination_options_request.DestinationOptionsRequest"
    ]
    """<p>The destination options.</p>"""
    tag_field_specifications: NotRequired[
        "capo_ec2.types.tag_field_specification_list_request.TagFieldSpecificationListRequest"
    ]
    """<p>The tag configuration associated with the Flow Logs Amazon EC2 Tags feature fields in your custom log format.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateFlowLogsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "deliver_logs_permission_arn" in value:
        pairs.append(
            (
                f"{key_prefix}DeliverLogsPermissionArn",
                str(value["deliver_logs_permission_arn"]),
            )
        )
    if "deliver_cross_account_role" in value:
        pairs.append(
            (
                f"{key_prefix}DeliverCrossAccountRole",
                str(value["deliver_cross_account_role"]),
            )
        )
    if "log_group_name" in value:
        pairs.append((f"{key_prefix}LogGroupName", str(value["log_group_name"])))
    if "resource_ids" in value:
        import capo_ec2.types.flow_log_resource_ids

        capo_ec2.types.flow_log_resource_ids.serialize_ec2_query(
            value["resource_ids"], pairs, f"{key_prefix}ResourceId"
        )
    if "resource_type" in value:
        import capo_ec2.types.flow_logs_resource_type

        capo_ec2.types.flow_logs_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "traffic_type" in value:
        import capo_ec2.types.traffic_type

        capo_ec2.types.traffic_type.serialize_ec2_query(
            value["traffic_type"], pairs, f"{key_prefix}TrafficType"
        )
    if "log_destination_type" in value:
        import capo_ec2.types.log_destination_type

        capo_ec2.types.log_destination_type.serialize_ec2_query(
            value["log_destination_type"], pairs, f"{key_prefix}LogDestinationType"
        )
    if "log_destination" in value:
        pairs.append((f"{key_prefix}LogDestination", str(value["log_destination"])))
    if "log_format" in value:
        pairs.append((f"{key_prefix}LogFormat", str(value["log_format"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "max_aggregation_interval" in value:
        pairs.append(
            (
                f"{key_prefix}MaxAggregationInterval",
                str(value["max_aggregation_interval"]),
            )
        )
    if "destination_options" in value:
        import capo_ec2.types.destination_options_request

        capo_ec2.types.destination_options_request.serialize_ec2_query(
            value["destination_options"], pairs, f"{key_prefix}DestinationOptions"
        )
    if "tag_field_specifications" in value:
        import capo_ec2.types.tag_field_specification_list_request

        capo_ec2.types.tag_field_specification_list_request.serialize_ec2_query(
            value["tag_field_specifications"],
            pairs,
            f"{key_prefix}TagFieldSpecification",
        )


def deserialize_ec2_query(el: Element) -> CreateFlowLogsRequest:
    out: CreateFlowLogsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_deliver_logs_permission_arn = el.find("DeliverLogsPermissionArn")
    if child_deliver_logs_permission_arn is not None:
        out["deliver_logs_permission_arn"] = str(
            child_deliver_logs_permission_arn.text or ""
        )
    child_deliver_cross_account_role = el.find("DeliverCrossAccountRole")
    if child_deliver_cross_account_role is not None:
        out["deliver_cross_account_role"] = str(
            child_deliver_cross_account_role.text or ""
        )
    child_log_group_name = el.find("LogGroupName")
    if child_log_group_name is not None:
        out["log_group_name"] = str(child_log_group_name.text or "")
    child_resource_ids = el.find("ResourceId")
    if child_resource_ids is not None:
        import capo_ec2.types.flow_log_resource_ids

        out["resource_ids"] = (
            capo_ec2.types.flow_log_resource_ids.deserialize_ec2_query(
                child_resource_ids
            )
        )
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import capo_ec2.types.flow_logs_resource_type

        out["resource_type"] = (
            capo_ec2.types.flow_logs_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_traffic_type = el.find("TrafficType")
    if child_traffic_type is not None:
        import capo_ec2.types.traffic_type

        out["traffic_type"] = capo_ec2.types.traffic_type.deserialize_ec2_query(
            child_traffic_type
        )
    child_log_destination_type = el.find("LogDestinationType")
    if child_log_destination_type is not None:
        import capo_ec2.types.log_destination_type

        out["log_destination_type"] = (
            capo_ec2.types.log_destination_type.deserialize_ec2_query(
                child_log_destination_type
            )
        )
    child_log_destination = el.find("LogDestination")
    if child_log_destination is not None:
        out["log_destination"] = str(child_log_destination.text or "")
    child_log_format = el.find("LogFormat")
    if child_log_format is not None:
        out["log_format"] = str(child_log_format.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_max_aggregation_interval = el.find("MaxAggregationInterval")
    if child_max_aggregation_interval is not None:
        out["max_aggregation_interval"] = int(child_max_aggregation_interval.text or "")
    child_destination_options = el.find("DestinationOptions")
    if child_destination_options is not None:
        import capo_ec2.types.destination_options_request

        out["destination_options"] = (
            capo_ec2.types.destination_options_request.deserialize_ec2_query(
                child_destination_options
            )
        )
    child_tag_field_specifications = el.find("TagFieldSpecification")
    if child_tag_field_specifications is not None:
        import capo_ec2.types.tag_field_specification_list_request

        out["tag_field_specifications"] = (
            capo_ec2.types.tag_field_specification_list_request.deserialize_ec2_query(
                child_tag_field_specifications
            )
        )
    return out
