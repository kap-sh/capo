"""Generated from Smithy shape ``com.amazonaws.ec2#FlowLog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.destination_options_response
    import capo_ec2.types.integer
    import capo_ec2.types.log_destination_type
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string
    import capo_ec2.types.tag_field_specification_list_response
    import capo_ec2.types.tag_list
    import capo_ec2.types.traffic_type


class FlowLog(TypedDict, closed=True):
    creation_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time the flow log was created.</p>"""
    deliver_logs_error_message: NotRequired["capo_ec2.types.string.String"]
    """<p>Information about the error that occurred. <code>Rate limited</code> indicates that CloudWatch Logs throttling has been applied for one or more network interfaces, or that you've reached the limit on the number of log groups that you can create. <code>Access error</code> indicates that the IAM role associated with the flow log does not have sufficient permissions to publish to CloudWatch Logs. <code>Unknown error</code> indicates an internal error.</p>"""
    deliver_logs_permission_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the IAM role allows the service to publish logs to CloudWatch Logs.</p>"""
    deliver_cross_account_role: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the IAM role that allows the service to publish flow logs across accounts.</p>"""
    deliver_logs_status: NotRequired["capo_ec2.types.string.String"]
    """<p>The status of the logs delivery (<code>SUCCESS</code> | <code>FAILED</code>).</p>"""
    flow_log_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the flow log.</p>"""
    flow_log_status: NotRequired["capo_ec2.types.string.String"]
    """<p>The status of the flow log (<code>ACTIVE</code>).</p>"""
    log_group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the flow log group.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource being monitored.</p>"""
    traffic_type: NotRequired["capo_ec2.types.traffic_type.TrafficType"]
    """<p>The type of traffic captured for the flow log.</p>"""
    log_destination_type: NotRequired[
        "capo_ec2.types.log_destination_type.LogDestinationType"
    ]
    """<p>The type of destination for the flow log data.</p>"""
    log_destination: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the destination for the flow log data.</p>"""
    log_format: NotRequired["capo_ec2.types.string.String"]
    """<p>The format of the flow log record.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the flow log.</p>"""
    max_aggregation_interval: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum interval of time, in seconds, during which a flow of packets is captured and aggregated into a flow log record.</p> <p>When a network interface is attached to a <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html">Nitro-based instance</a>, the aggregation interval is always 60 seconds (1 minute) or less, regardless of the specified value.</p> <p>Valid Values: <code>60</code> | <code>600</code> </p>"""
    destination_options: NotRequired[
        "capo_ec2.types.destination_options_response.DestinationOptionsResponse"
    ]
    """<p>The destination options.</p>"""
    tag_field_specifications: NotRequired[
        "capo_ec2.types.tag_field_specification_list_response.TagFieldSpecificationListResponse"
    ]
    """<p>The tag configuration associated with the Flow Logs Amazon EC2 Tags feature fields in your custom log format.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FlowLog, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "creation_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{key_prefix}CreationTime"
        )
    if "deliver_logs_error_message" in value:
        pairs.append(
            (
                f"{key_prefix}DeliverLogsErrorMessage",
                str(value["deliver_logs_error_message"]),
            )
        )
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
    if "deliver_logs_status" in value:
        pairs.append(
            (f"{key_prefix}DeliverLogsStatus", str(value["deliver_logs_status"]))
        )
    if "flow_log_id" in value:
        pairs.append((f"{key_prefix}FlowLogId", str(value["flow_log_id"])))
    if "flow_log_status" in value:
        pairs.append((f"{key_prefix}FlowLogStatus", str(value["flow_log_status"])))
    if "log_group_name" in value:
        pairs.append((f"{key_prefix}LogGroupName", str(value["log_group_name"])))
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
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
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "max_aggregation_interval" in value:
        pairs.append(
            (
                f"{key_prefix}MaxAggregationInterval",
                str(value["max_aggregation_interval"]),
            )
        )
    if "destination_options" in value:
        import capo_ec2.types.destination_options_response

        capo_ec2.types.destination_options_response.serialize_ec2_query(
            value["destination_options"], pairs, f"{key_prefix}DestinationOptions"
        )
    if "tag_field_specifications" in value:
        import capo_ec2.types.tag_field_specification_list_response

        capo_ec2.types.tag_field_specification_list_response.serialize_ec2_query(
            value["tag_field_specifications"],
            pairs,
            f"{key_prefix}TagFieldSpecificationSet",
        )


def deserialize_ec2_query(el: Element) -> FlowLog:
    out: FlowLog = {}  # type: ignore[typeddict-item]
    child_creation_time = el.find("creationTime")
    if child_creation_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["creation_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_creation_time
            )
        )
    child_deliver_logs_error_message = el.find("deliverLogsErrorMessage")
    if child_deliver_logs_error_message is not None:
        out["deliver_logs_error_message"] = str(
            child_deliver_logs_error_message.text or ""
        )
    child_deliver_logs_permission_arn = el.find("deliverLogsPermissionArn")
    if child_deliver_logs_permission_arn is not None:
        out["deliver_logs_permission_arn"] = str(
            child_deliver_logs_permission_arn.text or ""
        )
    child_deliver_cross_account_role = el.find("deliverCrossAccountRole")
    if child_deliver_cross_account_role is not None:
        out["deliver_cross_account_role"] = str(
            child_deliver_cross_account_role.text or ""
        )
    child_deliver_logs_status = el.find("deliverLogsStatus")
    if child_deliver_logs_status is not None:
        out["deliver_logs_status"] = str(child_deliver_logs_status.text or "")
    child_flow_log_id = el.find("flowLogId")
    if child_flow_log_id is not None:
        out["flow_log_id"] = str(child_flow_log_id.text or "")
    child_flow_log_status = el.find("flowLogStatus")
    if child_flow_log_status is not None:
        out["flow_log_status"] = str(child_flow_log_status.text or "")
    child_log_group_name = el.find("logGroupName")
    if child_log_group_name is not None:
        out["log_group_name"] = str(child_log_group_name.text or "")
    child_resource_id = el.find("resourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_traffic_type = el.find("trafficType")
    if child_traffic_type is not None:
        import capo_ec2.types.traffic_type

        out["traffic_type"] = capo_ec2.types.traffic_type.deserialize_ec2_query(
            child_traffic_type
        )
    child_log_destination_type = el.find("logDestinationType")
    if child_log_destination_type is not None:
        import capo_ec2.types.log_destination_type

        out["log_destination_type"] = (
            capo_ec2.types.log_destination_type.deserialize_ec2_query(
                child_log_destination_type
            )
        )
    child_log_destination = el.find("logDestination")
    if child_log_destination is not None:
        out["log_destination"] = str(child_log_destination.text or "")
    child_log_format = el.find("logFormat")
    if child_log_format is not None:
        out["log_format"] = str(child_log_format.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_max_aggregation_interval = el.find("maxAggregationInterval")
    if child_max_aggregation_interval is not None:
        out["max_aggregation_interval"] = int(child_max_aggregation_interval.text or "")
    child_destination_options = el.find("destinationOptions")
    if child_destination_options is not None:
        import capo_ec2.types.destination_options_response

        out["destination_options"] = (
            capo_ec2.types.destination_options_response.deserialize_ec2_query(
                child_destination_options
            )
        )
    child_tag_field_specifications = el.find("tagFieldSpecificationSet")
    if child_tag_field_specifications is not None:
        import capo_ec2.types.tag_field_specification_list_response

        out["tag_field_specifications"] = (
            capo_ec2.types.tag_field_specification_list_response.deserialize_ec2_query(
                child_tag_field_specifications
            )
        )
    return out
