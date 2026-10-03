"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutMetricStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.amazon_resource_name
    import capo_cloudwatch.types.include_linked_accounts_metrics
    import capo_cloudwatch.types.metric_stream_filters
    import capo_cloudwatch.types.metric_stream_name
    import capo_cloudwatch.types.metric_stream_output_format
    import capo_cloudwatch.types.metric_stream_statistics_configurations
    import capo_cloudwatch.types.tag_list


class PutMetricStreamInput(TypedDict, closed=True):
    name: NotRequired["capo_cloudwatch.types.metric_stream_name.MetricStreamName"]
    """<p>If you are creating a new metric stream, this is the name for the new stream. The name must be different than the names of other metric streams in this account and Region.</p> <p>If you are updating a metric stream, specify the name of that stream here.</p> <p>Valid characters are A-Z, a-z, 0-9, "-" and "_".</p>"""
    include_filters: NotRequired[
        "capo_cloudwatch.types.metric_stream_filters.MetricStreamFilters"
    ]
    """<p>If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here.</p> <p>You cannot include <code>IncludeFilters</code> and <code>ExcludeFilters</code> in the same operation.</p>"""
    exclude_filters: NotRequired[
        "capo_cloudwatch.types.metric_stream_filters.MetricStreamFilters"
    ]
    """<p>If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here.</p> <p>You cannot include <code>ExcludeFilters</code> and <code>IncludeFilters</code> in the same operation.</p>"""
    firehose_arn: NotRequired[
        "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the Amazon Kinesis Data Firehose delivery stream to use for this metric stream. This Amazon Kinesis Data Firehose delivery stream must already exist and must be in the same account as the metric stream.</p>"""
    role_arn: NotRequired[
        "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Data Firehose resources. This IAM role must already exist and must be in the same account as the metric stream. This IAM role must include the following permissions:</p> <ul> <li> <p>firehose:PutRecord</p> </li> <li> <p>firehose:PutRecordBatch</p> </li> </ul>"""
    output_format: NotRequired[
        "capo_cloudwatch.types.metric_stream_output_format.MetricStreamOutputFormat"
    ]
    """<p>The output format for the stream. Valid values are <code>json</code>, <code>opentelemetry1.0</code>, and <code>opentelemetry0.7</code>. For more information about metric stream output formats, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html"> Metric streams output formats</a>.</p>"""
    tags: NotRequired["capo_cloudwatch.types.tag_list.TagList"]
    """<p>A list of key-value pairs to associate with the metric stream. You can associate as many as 50 tags with a metric stream.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>You can use this parameter only when you are creating a new metric stream. If you are using this operation to update an existing metric stream, any tags you specify in this parameter are ignored. To change the tags of an existing metric stream, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html">TagResource</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html">UntagResource</a>.</p>"""
    statistics_configurations: NotRequired[
        "capo_cloudwatch.types.metric_stream_statistics_configurations.MetricStreamStatisticsConfigurations"
    ]
    """<p>By default, a metric stream always sends the <code>MAX</code>, <code>MIN</code>, <code>SUM</code>, and <code>SAMPLECOUNT</code> statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.</p> <p>For each entry in this array, you specify one or more metrics and the list of additional statistics to stream for those metrics. The additional statistics that you can stream depend on the stream's <code>OutputFormat</code>. If the <code>OutputFormat</code> is <code>json</code>, you can stream any additional statistic that is supported by CloudWatch, listed in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html"> CloudWatch statistics definitions</a>. If the <code>OutputFormat</code> is <code>opentelemetry1.0</code> or <code>opentelemetry0.7</code>, you can stream percentile statistics such as p95, p99.9, and so on.</p>"""
    include_linked_accounts_metrics: NotRequired[
        "capo_cloudwatch.types.include_linked_accounts_metrics.IncludeLinkedAccountsMetrics"
    ]
    """<p>If you are creating a metric stream in a monitoring account, specify <code>true</code> to include metrics from source accounts in the metric stream.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutMetricStreamInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "include_filters" in value:
        import capo_cloudwatch.types.metric_stream_filters

        out["IncludeFilters"] = (
            capo_cloudwatch.types.metric_stream_filters.serialize_aws_json_1_0(
                value["include_filters"]
            )
        )
    if "exclude_filters" in value:
        import capo_cloudwatch.types.metric_stream_filters

        out["ExcludeFilters"] = (
            capo_cloudwatch.types.metric_stream_filters.serialize_aws_json_1_0(
                value["exclude_filters"]
            )
        )
    if "firehose_arn" in value:
        out["FirehoseArn"] = value["firehose_arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "output_format" in value:
        import capo_cloudwatch.types.metric_stream_output_format

        out["OutputFormat"] = (
            capo_cloudwatch.types.metric_stream_output_format.serialize_aws_json_1_0(
                value["output_format"]
            )
        )
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        out["Tags"] = capo_cloudwatch.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "statistics_configurations" in value:
        import capo_cloudwatch.types.metric_stream_statistics_configurations

        out["StatisticsConfigurations"] = (
            capo_cloudwatch.types.metric_stream_statistics_configurations.serialize_aws_json_1_0(
                value["statistics_configurations"]
            )
        )
    if "include_linked_accounts_metrics" in value:
        out["IncludeLinkedAccountsMetrics"] = value["include_linked_accounts_metrics"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutMetricStreamInput:
    out: PutMetricStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("IncludeFilters") is not None:
        import capo_cloudwatch.types.metric_stream_filters

        out["include_filters"] = (
            capo_cloudwatch.types.metric_stream_filters.deserialize_aws_json_1_0(
                data["IncludeFilters"]
            )
        )
    if data.get("ExcludeFilters") is not None:
        import capo_cloudwatch.types.metric_stream_filters

        out["exclude_filters"] = (
            capo_cloudwatch.types.metric_stream_filters.deserialize_aws_json_1_0(
                data["ExcludeFilters"]
            )
        )
    if data.get("FirehoseArn") is not None:
        out["firehose_arn"] = data["FirehoseArn"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("OutputFormat") is not None:
        import capo_cloudwatch.types.metric_stream_output_format

        out["output_format"] = (
            capo_cloudwatch.types.metric_stream_output_format.deserialize_aws_json_1_0(
                data["OutputFormat"]
            )
        )
    if data.get("Tags") is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("StatisticsConfigurations") is not None:
        import capo_cloudwatch.types.metric_stream_statistics_configurations

        out["statistics_configurations"] = (
            capo_cloudwatch.types.metric_stream_statistics_configurations.deserialize_aws_json_1_0(
                data["StatisticsConfigurations"]
            )
        )
    if data.get("IncludeLinkedAccountsMetrics") is not None:
        out["include_linked_accounts_metrics"] = data["IncludeLinkedAccountsMetrics"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutMetricStreamInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "include_filters" in value:
        import capo_cloudwatch.types.metric_stream_filters

        capo_cloudwatch.types.metric_stream_filters.serialize_query(
            value["include_filters"], pairs, f"{key_prefix}IncludeFilters"
        )
    if "exclude_filters" in value:
        import capo_cloudwatch.types.metric_stream_filters

        capo_cloudwatch.types.metric_stream_filters.serialize_query(
            value["exclude_filters"], pairs, f"{key_prefix}ExcludeFilters"
        )
    if "firehose_arn" in value:
        pairs.append((f"{key_prefix}FirehoseArn", str(value["firehose_arn"])))
    if "role_arn" in value:
        pairs.append((f"{key_prefix}RoleArn", str(value["role_arn"])))
    if "output_format" in value:
        import capo_cloudwatch.types.metric_stream_output_format

        capo_cloudwatch.types.metric_stream_output_format.serialize_query(
            value["output_format"], pairs, f"{key_prefix}OutputFormat"
        )
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        capo_cloudwatch.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "statistics_configurations" in value:
        import capo_cloudwatch.types.metric_stream_statistics_configurations

        capo_cloudwatch.types.metric_stream_statistics_configurations.serialize_query(
            value["statistics_configurations"],
            pairs,
            f"{key_prefix}StatisticsConfigurations",
        )
    if "include_linked_accounts_metrics" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeLinkedAccountsMetrics",
                "true" if value["include_linked_accounts_metrics"] else "false",
            )
        )


def deserialize_query(el: Element) -> PutMetricStreamInput:
    out: PutMetricStreamInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_include_filters = el.find("IncludeFilters")
    if child_include_filters is not None:
        import capo_cloudwatch.types.metric_stream_filters

        out["include_filters"] = (
            capo_cloudwatch.types.metric_stream_filters.deserialize_query(
                child_include_filters
            )
        )
    child_exclude_filters = el.find("ExcludeFilters")
    if child_exclude_filters is not None:
        import capo_cloudwatch.types.metric_stream_filters

        out["exclude_filters"] = (
            capo_cloudwatch.types.metric_stream_filters.deserialize_query(
                child_exclude_filters
            )
        )
    child_firehose_arn = el.find("FirehoseArn")
    if child_firehose_arn is not None:
        out["firehose_arn"] = str(child_firehose_arn.text or "")
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_output_format = el.find("OutputFormat")
    if child_output_format is not None:
        import capo_cloudwatch.types.metric_stream_output_format

        out["output_format"] = (
            capo_cloudwatch.types.metric_stream_output_format.deserialize_query(
                child_output_format
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_query(child_tags)
    child_statistics_configurations = el.find("StatisticsConfigurations")
    if child_statistics_configurations is not None:
        import capo_cloudwatch.types.metric_stream_statistics_configurations

        out["statistics_configurations"] = (
            capo_cloudwatch.types.metric_stream_statistics_configurations.deserialize_query(
                child_statistics_configurations
            )
        )
    child_include_linked_accounts_metrics = el.find("IncludeLinkedAccountsMetrics")
    if child_include_linked_accounts_metrics is not None:
        out["include_linked_accounts_metrics"] = (
            child_include_linked_accounts_metrics.text or ""
        ).lower() == "true"
    return out
