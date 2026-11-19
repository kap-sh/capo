"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricStreamEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.amazon_resource_name
    import capo_cloudwatch.types.metric_stream_name
    import capo_cloudwatch.types.metric_stream_output_format
    import capo_cloudwatch.types.metric_stream_state
    import capo_cloudwatch.types.timestamp


class MetricStreamEntry(TypedDict, closed=True):
    arn: NotRequired["capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"]
    """<p>The ARN of the metric stream.</p>"""
    creation_date: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date that the metric stream was originally created.</p>"""
    last_update_date: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date that the configuration of this metric stream was most recently updated.</p>"""
    name: NotRequired["capo_cloudwatch.types.metric_stream_name.MetricStreamName"]
    """<p>The name of the metric stream.</p>"""
    firehose_arn: NotRequired[
        "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the Kinesis Firehose devlivery stream that is used for this metric stream.</p>"""
    state: NotRequired["capo_cloudwatch.types.metric_stream_state.MetricStreamState"]
    """<p>The current state of this stream. Valid values are <code>running</code> and <code>stopped</code>.</p>"""
    output_format: NotRequired[
        "capo_cloudwatch.types.metric_stream_output_format.MetricStreamOutputFormat"
    ]
    """<p>The output format of this metric stream. Valid values are <code>json</code>, <code>opentelemetry1.0</code>, and <code>opentelemetry0.7</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricStreamEntry) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
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
    if "name" in value:
        out["Name"] = value["name"]
    if "firehose_arn" in value:
        out["FirehoseArn"] = value["firehose_arn"]
    if "state" in value:
        out["State"] = value["state"]
    if "output_format" in value:
        import capo_cloudwatch.types.metric_stream_output_format

        out["OutputFormat"] = (
            capo_cloudwatch.types.metric_stream_output_format.serialize_aws_json_1_0(
                value["output_format"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricStreamEntry:
    out: MetricStreamEntry = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
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
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("FirehoseArn") is not None:
        out["firehose_arn"] = data["FirehoseArn"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("OutputFormat") is not None:
        import capo_cloudwatch.types.metric_stream_output_format

        out["output_format"] = (
            capo_cloudwatch.types.metric_stream_output_format.deserialize_aws_json_1_0(
                data["OutputFormat"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricStreamEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
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
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "firehose_arn" in value:
        pairs.append((f"{key_prefix}FirehoseArn", str(value["firehose_arn"])))
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))
    if "output_format" in value:
        import capo_cloudwatch.types.metric_stream_output_format

        capo_cloudwatch.types.metric_stream_output_format.serialize_query(
            value["output_format"], pairs, f"{key_prefix}OutputFormat"
        )


def deserialize_query(el: Element) -> MetricStreamEntry:
    out: MetricStreamEntry = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
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
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_firehose_arn = el.find("FirehoseArn")
    if child_firehose_arn is not None:
        out["firehose_arn"] = str(child_firehose_arn.text or "")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_output_format = el.find("OutputFormat")
    if child_output_format is not None:
        import capo_cloudwatch.types.metric_stream_output_format

        out["output_format"] = (
            capo_cloudwatch.types.metric_stream_output_format.deserialize_query(
                child_output_format
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricStreamEntry) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_date" in value:
        import capo_cloudwatch.types.timestamp

        out["CreationDate"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["creation_date"]
        )
    if "last_update_date" in value:
        import capo_cloudwatch.types.timestamp

        out["LastUpdateDate"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["last_update_date"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "firehose_arn" in value:
        out["FirehoseArn"] = value["firehose_arn"]
    if "state" in value:
        out["State"] = value["state"]
    if "output_format" in value:
        import capo_cloudwatch.types.metric_stream_output_format

        out["OutputFormat"] = (
            capo_cloudwatch.types.metric_stream_output_format.serialize_cbor(
                value["output_format"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> MetricStreamEntry:
    out: MetricStreamEntry = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreationDate") is not None:
        import capo_cloudwatch.types.timestamp

        out["creation_date"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["CreationDate"]
        )
    if data.get("LastUpdateDate") is not None:
        import capo_cloudwatch.types.timestamp

        out["last_update_date"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["LastUpdateDate"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("FirehoseArn") is not None:
        out["firehose_arn"] = data["FirehoseArn"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("OutputFormat") is not None:
        import capo_cloudwatch.types.metric_stream_output_format

        out["output_format"] = (
            capo_cloudwatch.types.metric_stream_output_format.deserialize_cbor(
                data["OutputFormat"]
            )
        )
    return out
