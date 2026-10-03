"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStreamDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.delivery_stream_arn
    import capo_firehose.types.delivery_stream_encryption_configuration
    import capo_firehose.types.delivery_stream_name
    import capo_firehose.types.delivery_stream_status
    import capo_firehose.types.delivery_stream_type
    import capo_firehose.types.delivery_stream_version_id
    import capo_firehose.types.destination_description_list
    import capo_firehose.types.failure_description
    import capo_firehose.types.source_description
    import capo_firehose.types.timestamp


class DeliveryStreamDescription(TypedDict, closed=True):
    delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName"
    """<p>The name of the Firehose stream.</p>"""
    delivery_stream_arn: "capo_firehose.types.delivery_stream_arn.DeliveryStreamARN"
    """<p>The Amazon Resource Name (ARN) of the Firehose stream. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    delivery_stream_status: (
        "capo_firehose.types.delivery_stream_status.DeliveryStreamStatus"
    )
    """<p>The status of the Firehose stream. If the status of a Firehose stream is <code>CREATING_FAILED</code>, this status doesn't change, and you can't invoke <code>CreateDeliveryStream</code> again on it. However, you can invoke the <a>DeleteDeliveryStream</a> operation to delete it.</p>"""
    failure_description: NotRequired[
        "capo_firehose.types.failure_description.FailureDescription"
    ]
    """<p>Provides details in case one of the following operations fails due to an error related to KMS: <a>CreateDeliveryStream</a>, <a>DeleteDeliveryStream</a>, <a>StartDeliveryStreamEncryption</a>, <a>StopDeliveryStreamEncryption</a>.</p>"""
    delivery_stream_encryption_configuration: NotRequired[
        "capo_firehose.types.delivery_stream_encryption_configuration.DeliveryStreamEncryptionConfiguration"
    ]
    """<p>Indicates the server-side encryption (SSE) status for the Firehose stream.</p>"""
    delivery_stream_type: "capo_firehose.types.delivery_stream_type.DeliveryStreamType"
    """<p>The Firehose stream type. This can be one of the following values:</p> <ul> <li> <p> <code>DirectPut</code>: Provider applications access the Firehose stream directly.</p> </li> <li> <p> <code>KinesisStreamAsSource</code>: The Firehose stream uses a Kinesis data stream as a source.</p> </li> </ul>"""
    version_id: "capo_firehose.types.delivery_stream_version_id.DeliveryStreamVersionId"
    """<p>Each time the destination is updated for a Firehose stream, the version ID is changed, and the current version ID is required when updating the destination. This is so that the service knows it is applying the changes to the correct version of the delivery stream.</p>"""
    create_timestamp: NotRequired["capo_firehose.types.timestamp.Timestamp"]
    """<p>The date and time that the Firehose stream was created.</p>"""
    last_update_timestamp: NotRequired["capo_firehose.types.timestamp.Timestamp"]
    """<p>The date and time that the Firehose stream was last updated.</p>"""
    source: NotRequired["capo_firehose.types.source_description.SourceDescription"]
    """<p>If the <code>DeliveryStreamType</code> parameter is <code>KinesisStreamAsSource</code>, a <a>SourceDescription</a> object describing the source Kinesis data stream.</p>"""
    destinations: (
        "capo_firehose.types.destination_description_list.DestinationDescriptionList"
    )
    """<p>The destinations.</p>"""
    has_more_destinations: "capo_firehose.types.boolean_object.BooleanObject"
    """<p>Indicates whether there are more destinations available to list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryStreamDescription) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    out["DeliveryStreamARN"] = value["delivery_stream_arn"]
    import capo_firehose.types.delivery_stream_status

    out["DeliveryStreamStatus"] = (
        capo_firehose.types.delivery_stream_status.serialize_aws_json_1_1(
            value["delivery_stream_status"]
        )
    )
    if "failure_description" in value:
        import capo_firehose.types.failure_description

        out["FailureDescription"] = (
            capo_firehose.types.failure_description.serialize_aws_json_1_1(
                value["failure_description"]
            )
        )
    if "delivery_stream_encryption_configuration" in value:
        import capo_firehose.types.delivery_stream_encryption_configuration

        out["DeliveryStreamEncryptionConfiguration"] = (
            capo_firehose.types.delivery_stream_encryption_configuration.serialize_aws_json_1_1(
                value["delivery_stream_encryption_configuration"]
            )
        )
    import capo_firehose.types.delivery_stream_type

    out["DeliveryStreamType"] = (
        capo_firehose.types.delivery_stream_type.serialize_aws_json_1_1(
            value["delivery_stream_type"]
        )
    )
    out["VersionId"] = value["version_id"]
    if "create_timestamp" in value:
        import capo_firehose.types.timestamp

        out["CreateTimestamp"] = capo_firehose.types.timestamp.serialize_aws_json_1_1(
            value["create_timestamp"]
        )
    if "last_update_timestamp" in value:
        import capo_firehose.types.timestamp

        out["LastUpdateTimestamp"] = (
            capo_firehose.types.timestamp.serialize_aws_json_1_1(
                value["last_update_timestamp"]
            )
        )
    if "source" in value:
        import capo_firehose.types.source_description

        out["Source"] = capo_firehose.types.source_description.serialize_aws_json_1_1(
            value["source"]
        )
    import capo_firehose.types.destination_description_list

    out["Destinations"] = (
        capo_firehose.types.destination_description_list.serialize_aws_json_1_1(
            value["destinations"]
        )
    )
    out["HasMoreDestinations"] = value["has_more_destinations"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliveryStreamDescription:
    out: DeliveryStreamDescription = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryStreamName") is not None:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        raise DeserializationError(
            "DeliveryStreamDescription.delivery_stream_name required"
        )
    if data.get("DeliveryStreamARN") is not None:
        out["delivery_stream_arn"] = data["DeliveryStreamARN"]
    else:
        raise DeserializationError(
            "DeliveryStreamDescription.delivery_stream_arn required"
        )
    if data.get("DeliveryStreamStatus") is not None:
        import capo_firehose.types.delivery_stream_status

        out["delivery_stream_status"] = (
            capo_firehose.types.delivery_stream_status.deserialize_aws_json_1_1(
                data["DeliveryStreamStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DeliveryStreamDescription.delivery_stream_status required"
        )
    if data.get("FailureDescription") is not None:
        import capo_firehose.types.failure_description

        out["failure_description"] = (
            capo_firehose.types.failure_description.deserialize_aws_json_1_1(
                data["FailureDescription"]
            )
        )
    if data.get("DeliveryStreamEncryptionConfiguration") is not None:
        import capo_firehose.types.delivery_stream_encryption_configuration

        out["delivery_stream_encryption_configuration"] = (
            capo_firehose.types.delivery_stream_encryption_configuration.deserialize_aws_json_1_1(
                data["DeliveryStreamEncryptionConfiguration"]
            )
        )
    if data.get("DeliveryStreamType") is not None:
        import capo_firehose.types.delivery_stream_type

        out["delivery_stream_type"] = (
            capo_firehose.types.delivery_stream_type.deserialize_aws_json_1_1(
                data["DeliveryStreamType"]
            )
        )
    else:
        raise DeserializationError(
            "DeliveryStreamDescription.delivery_stream_type required"
        )
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    else:
        raise DeserializationError("DeliveryStreamDescription.version_id required")
    if data.get("CreateTimestamp") is not None:
        import capo_firehose.types.timestamp

        out["create_timestamp"] = (
            capo_firehose.types.timestamp.deserialize_aws_json_1_1(
                data["CreateTimestamp"]
            )
        )
    if data.get("LastUpdateTimestamp") is not None:
        import capo_firehose.types.timestamp

        out["last_update_timestamp"] = (
            capo_firehose.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdateTimestamp"]
            )
        )
    if data.get("Source") is not None:
        import capo_firehose.types.source_description

        out["source"] = capo_firehose.types.source_description.deserialize_aws_json_1_1(
            data["Source"]
        )
    if data.get("Destinations") is not None:
        import capo_firehose.types.destination_description_list

        out["destinations"] = (
            capo_firehose.types.destination_description_list.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    else:
        raise DeserializationError("DeliveryStreamDescription.destinations required")
    if data.get("HasMoreDestinations") is not None:
        out["has_more_destinations"] = data["HasMoreDestinations"]
    else:
        raise DeserializationError(
            "DeliveryStreamDescription.has_more_destinations required"
        )
    return out
