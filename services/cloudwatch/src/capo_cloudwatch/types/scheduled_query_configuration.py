"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ScheduledQueryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.aggregation_expression
    import capo_cloudwatch.types.amazon_resource_name
    import capo_cloudwatch.types.log_group_identifiers
    import capo_cloudwatch.types.query_string
    import capo_cloudwatch.types.schedule_configuration
    import capo_cloudwatch.types.tag_list


class ScheduledQueryConfiguration(TypedDict, closed=True):
    query_string: NotRequired["capo_cloudwatch.types.query_string.QueryString"]
    """<p>The CloudWatch Logs query to execute on each scheduled run. Length constraints: maximum of 10,000 characters.</p>"""
    log_group_identifiers: NotRequired[
        "capo_cloudwatch.types.log_group_identifiers.LogGroupIdentifiers"
    ]
    """<p>The log groups to query. Each entry can be a log group name or ARN. Use the ARN form when querying log groups in a different account (for example, when running cross-account queries from a monitoring account). The list must contain between 1 and 50 entries.</p>"""
    query_arn: NotRequired[
        "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch Logs scheduled query that the alarm uses. This field is populated in <code>DescribeAlarms</code> responses.</p>"""
    scheduled_query_role_arn: NotRequired[
        "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that CloudWatch assumes when executing the scheduled query against the configured log groups.</p>"""
    schedule_configuration: NotRequired[
        "capo_cloudwatch.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The schedule and time-range offset configuration for the underlying scheduled query.</p>"""
    aggregation_expression: NotRequired[
        "capo_cloudwatch.types.aggregation_expression.AggregationExpression"
    ]
    """<p>The expression that defines how to aggregate query results into one or more scalar values for alarm evaluation. For example, <code>count(*)</code> or <code>avg(latency) by host | sort desc</code>. Length constraints: minimum 1 character, maximum 2048 characters.</p>"""
    tags: NotRequired["capo_cloudwatch.types.tag_list.TagList"]
    """<p>A list of key-value pairs to associate with the underlying scheduled query resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledQueryConfiguration) -> dict:
    out: dict = {}
    if "query_string" in value:
        out["QueryString"] = value["query_string"]
    if "log_group_identifiers" in value:
        import capo_cloudwatch.types.log_group_identifiers

        out["LogGroupIdentifiers"] = (
            capo_cloudwatch.types.log_group_identifiers.serialize_aws_json_1_0(
                value["log_group_identifiers"]
            )
        )
    if "query_arn" in value:
        out["QueryARN"] = value["query_arn"]
    if "scheduled_query_role_arn" in value:
        out["ScheduledQueryRoleARN"] = value["scheduled_query_role_arn"]
    if "schedule_configuration" in value:
        import capo_cloudwatch.types.schedule_configuration

        out["ScheduleConfiguration"] = (
            capo_cloudwatch.types.schedule_configuration.serialize_aws_json_1_0(
                value["schedule_configuration"]
            )
        )
    if "aggregation_expression" in value:
        out["AggregationExpression"] = value["aggregation_expression"]
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        out["Tags"] = capo_cloudwatch.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduledQueryConfiguration:
    out: ScheduledQueryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    if data.get("LogGroupIdentifiers") is not None:
        import capo_cloudwatch.types.log_group_identifiers

        out["log_group_identifiers"] = (
            capo_cloudwatch.types.log_group_identifiers.deserialize_aws_json_1_0(
                data["LogGroupIdentifiers"]
            )
        )
    if data.get("QueryARN") is not None:
        out["query_arn"] = data["QueryARN"]
    if data.get("ScheduledQueryRoleARN") is not None:
        out["scheduled_query_role_arn"] = data["ScheduledQueryRoleARN"]
    if data.get("ScheduleConfiguration") is not None:
        import capo_cloudwatch.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_cloudwatch.types.schedule_configuration.deserialize_aws_json_1_0(
                data["ScheduleConfiguration"]
            )
        )
    if data.get("AggregationExpression") is not None:
        out["aggregation_expression"] = data["AggregationExpression"]
    if data.get("Tags") is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduledQueryConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "query_string" in value:
        pairs.append((f"{key_prefix}QueryString", str(value["query_string"])))
    if "log_group_identifiers" in value:
        import capo_cloudwatch.types.log_group_identifiers

        capo_cloudwatch.types.log_group_identifiers.serialize_query(
            value["log_group_identifiers"], pairs, f"{key_prefix}LogGroupIdentifiers"
        )
    if "query_arn" in value:
        pairs.append((f"{key_prefix}QueryARN", str(value["query_arn"])))
    if "scheduled_query_role_arn" in value:
        pairs.append(
            (
                f"{key_prefix}ScheduledQueryRoleARN",
                str(value["scheduled_query_role_arn"]),
            )
        )
    if "schedule_configuration" in value:
        import capo_cloudwatch.types.schedule_configuration

        capo_cloudwatch.types.schedule_configuration.serialize_query(
            value["schedule_configuration"], pairs, f"{key_prefix}ScheduleConfiguration"
        )
    if "aggregation_expression" in value:
        pairs.append(
            (f"{key_prefix}AggregationExpression", str(value["aggregation_expression"]))
        )
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        capo_cloudwatch.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> ScheduledQueryConfiguration:
    out: ScheduledQueryConfiguration = {}  # type: ignore[typeddict-item]
    child_query_string = el.find("QueryString")
    if child_query_string is not None:
        out["query_string"] = str(child_query_string.text or "")
    child_log_group_identifiers = el.find("LogGroupIdentifiers")
    if child_log_group_identifiers is not None:
        import capo_cloudwatch.types.log_group_identifiers

        out["log_group_identifiers"] = (
            capo_cloudwatch.types.log_group_identifiers.deserialize_query(
                child_log_group_identifiers
            )
        )
    child_query_arn = el.find("QueryARN")
    if child_query_arn is not None:
        out["query_arn"] = str(child_query_arn.text or "")
    child_scheduled_query_role_arn = el.find("ScheduledQueryRoleARN")
    if child_scheduled_query_role_arn is not None:
        out["scheduled_query_role_arn"] = str(child_scheduled_query_role_arn.text or "")
    child_schedule_configuration = el.find("ScheduleConfiguration")
    if child_schedule_configuration is not None:
        import capo_cloudwatch.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_cloudwatch.types.schedule_configuration.deserialize_query(
                child_schedule_configuration
            )
        )
    child_aggregation_expression = el.find("AggregationExpression")
    if child_aggregation_expression is not None:
        out["aggregation_expression"] = str(child_aggregation_expression.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_query(child_tags)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScheduledQueryConfiguration) -> dict:
    out: dict = {}
    if "query_string" in value:
        out["QueryString"] = value["query_string"]
    if "log_group_identifiers" in value:
        import capo_cloudwatch.types.log_group_identifiers

        out["LogGroupIdentifiers"] = (
            capo_cloudwatch.types.log_group_identifiers.serialize_cbor(
                value["log_group_identifiers"]
            )
        )
    if "query_arn" in value:
        out["QueryARN"] = value["query_arn"]
    if "scheduled_query_role_arn" in value:
        out["ScheduledQueryRoleARN"] = value["scheduled_query_role_arn"]
    if "schedule_configuration" in value:
        import capo_cloudwatch.types.schedule_configuration

        out["ScheduleConfiguration"] = (
            capo_cloudwatch.types.schedule_configuration.serialize_cbor(
                value["schedule_configuration"]
            )
        )
    if "aggregation_expression" in value:
        out["AggregationExpression"] = value["aggregation_expression"]
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        out["Tags"] = capo_cloudwatch.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> ScheduledQueryConfiguration:
    out: ScheduledQueryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    if data.get("LogGroupIdentifiers") is not None:
        import capo_cloudwatch.types.log_group_identifiers

        out["log_group_identifiers"] = (
            capo_cloudwatch.types.log_group_identifiers.deserialize_cbor(
                data["LogGroupIdentifiers"]
            )
        )
    if data.get("QueryARN") is not None:
        out["query_arn"] = data["QueryARN"]
    if data.get("ScheduledQueryRoleARN") is not None:
        out["scheduled_query_role_arn"] = data["ScheduledQueryRoleARN"]
    if data.get("ScheduleConfiguration") is not None:
        import capo_cloudwatch.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_cloudwatch.types.schedule_configuration.deserialize_cbor(
                data["ScheduleConfiguration"]
            )
        )
    if data.get("AggregationExpression") is not None:
        out["aggregation_expression"] = data["AggregationExpression"]
    if data.get("Tags") is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_cbor(data["Tags"])
    return out
