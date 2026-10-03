"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetMetricStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.amazon_resource_name
    import capo_cloudwatch.types.include_linked_accounts_metrics
    import capo_cloudwatch.types.metric_stream_filters
    import capo_cloudwatch.types.metric_stream_name
    import capo_cloudwatch.types.metric_stream_output_format
    import capo_cloudwatch.types.metric_stream_state
    import capo_cloudwatch.types.metric_stream_statistics_configurations
    import capo_cloudwatch.types.timestamp


class GetMetricStreamOutput(TypedDict, closed=True):
    arn: NotRequired["capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"]
    """<p>The ARN of the metric stream.</p>"""
    name: NotRequired["capo_cloudwatch.types.metric_stream_name.MetricStreamName"]
    """<p>The name of the metric stream.</p>"""
    include_filters: NotRequired[
        "capo_cloudwatch.types.metric_stream_filters.MetricStreamFilters"
    ]
    """<p>If this array of metric namespaces is present, then these namespaces are the only metric namespaces that are streamed by this metric stream.</p>"""
    exclude_filters: NotRequired[
        "capo_cloudwatch.types.metric_stream_filters.MetricStreamFilters"
    ]
    """<p>If this array of metric namespaces is present, then these namespaces are the only metric namespaces that are not streamed by this metric stream. In this case, all other metric namespaces in the account are streamed by this metric stream.</p>"""
    firehose_arn: NotRequired[
        "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the Amazon Kinesis Data Firehose delivery stream that is used by this metric stream.</p>"""
    role_arn: NotRequired[
        "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the IAM role that is used by this metric stream.</p>"""
    state: NotRequired["capo_cloudwatch.types.metric_stream_state.MetricStreamState"]
    """<p>The state of the metric stream. The possible values are <code>running</code> and <code>stopped</code>.</p>"""
    creation_date: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date that the metric stream was created.</p>"""
    last_update_date: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date of the most recent update to the metric stream's configuration.</p>"""
    output_format: NotRequired[
        "capo_cloudwatch.types.metric_stream_output_format.MetricStreamOutputFormat"
    ]
    """<p>The output format for the stream. Valid values are <code>json</code>, <code>opentelemetry1.0</code>, and <code>opentelemetry0.7</code>. For more information about metric stream output formats, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html">Metric streams output formats</a>.</p>"""
    statistics_configurations: NotRequired[
        "capo_cloudwatch.types.metric_stream_statistics_configurations.MetricStreamStatisticsConfigurations"
    ]
    """<p>Each entry in this array displays information about one or more metrics that include additional statistics in the metric stream. For more information about the additional statistics, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html"> CloudWatch statistics definitions</a>. </p>"""
    include_linked_accounts_metrics: NotRequired[
        "capo_cloudwatch.types.include_linked_accounts_metrics.IncludeLinkedAccountsMetrics"
    ]
    """<p>If this is <code>true</code> and this metric stream is in a monitoring account, then the stream includes metrics from source accounts that the monitoring account is linked to.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMetricStreamOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
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
    if "state" in value:
        out["State"] = value["state"]
    if "creation_date" in value:
        import capo_cloudwatch.types.timestamp

        out["CreationDate"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["creation_date"]
        )
    if "last_update_date" in value:
        import capo_cloudwatch.types.timestamp

        out["LastUpdateDate"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["last_update_date"]
        )
    if "output_format" in value:
        import capo_cloudwatch.types.metric_stream_output_format

        out["OutputFormat"] = (
            capo_cloudwatch.types.metric_stream_output_format.serialize_aws_json_1_0(
                value["output_format"]
            )
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


def deserialize_aws_json_1_0(data: dict) -> GetMetricStreamOutput:
    out: GetMetricStreamOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
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
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("CreationDate") is not None:
        import capo_cloudwatch.types.timestamp

        out["creation_date"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["CreationDate"]
        )
    if data.get("LastUpdateDate") is not None:
        import capo_cloudwatch.types.timestamp

        out["last_update_date"] = (
            capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
                data["LastUpdateDate"]
            )
        )
    if data.get("OutputFormat") is not None:
        import capo_cloudwatch.types.metric_stream_output_format

        out["output_format"] = (
            capo_cloudwatch.types.metric_stream_output_format.deserialize_aws_json_1_0(
                data["OutputFormat"]
            )
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
    value: GetMetricStreamOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
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
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))
    if "creation_date" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["creation_date"], pairs, f"{key_prefix}CreationDate"
        )
    if "last_update_date" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["last_update_date"], pairs, f"{key_prefix}LastUpdateDate"
        )
    if "output_format" in value:
        import capo_cloudwatch.types.metric_stream_output_format

        capo_cloudwatch.types.metric_stream_output_format.serialize_query(
            value["output_format"], pairs, f"{key_prefix}OutputFormat"
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


def deserialize_query(el: Element) -> GetMetricStreamOutput:
    out: GetMetricStreamOutput = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
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
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_creation_date = el.find("CreationDate")
    if child_creation_date is not None:
        import capo_cloudwatch.types.timestamp

        out["creation_date"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_creation_date
        )
    child_last_update_date = el.find("LastUpdateDate")
    if child_last_update_date is not None:
        import capo_cloudwatch.types.timestamp

        out["last_update_date"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_last_update_date
        )
    child_output_format = el.find("OutputFormat")
    if child_output_format is not None:
        import capo_cloudwatch.types.metric_stream_output_format

        out["output_format"] = (
            capo_cloudwatch.types.metric_stream_output_format.deserialize_query(
                child_output_format
            )
        )
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
