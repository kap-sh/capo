"""Generated from Smithy shape ``com.amazonaws.firehose#MSKSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.authentication_configuration
    import capo_firehose.types.msk_cluster_arn
    import capo_firehose.types.read_from_timestamp
    import capo_firehose.types.topic_name


class MSKSourceConfiguration(TypedDict, closed=True):
    msk_cluster_arn: "capo_firehose.types.msk_cluster_arn.MSKClusterARN"
    """<p>The ARN of the Amazon MSK cluster.</p>"""
    topic_name: "capo_firehose.types.topic_name.TopicName"
    """<p>The topic name within the Amazon MSK cluster. </p>"""
    authentication_configuration: (
        "capo_firehose.types.authentication_configuration.AuthenticationConfiguration"
    )
    """<p>The authentication configuration of the Amazon MSK cluster.</p>"""
    read_from_timestamp: NotRequired[
        "capo_firehose.types.read_from_timestamp.ReadFromTimestamp"
    ]
    """<p>The start date and time in UTC for the offset position within your MSK topic from where Firehose begins to read. By default, this is set to timestamp when Firehose becomes Active. </p> <p>If you want to create a Firehose stream with Earliest start position from SDK or CLI, you need to set the <code>ReadFromTimestamp</code> parameter to Epoch (1970-01-01T00:00:00Z). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MSKSourceConfiguration) -> dict:
    out: dict = {}
    out["MSKClusterARN"] = value["msk_cluster_arn"]
    out["TopicName"] = value["topic_name"]
    import capo_firehose.types.authentication_configuration

    out["AuthenticationConfiguration"] = (
        capo_firehose.types.authentication_configuration.serialize_aws_json_1_1(
            value["authentication_configuration"]
        )
    )
    if "read_from_timestamp" in value:
        import capo_firehose.types.read_from_timestamp

        out["ReadFromTimestamp"] = (
            capo_firehose.types.read_from_timestamp.serialize_aws_json_1_1(
                value["read_from_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MSKSourceConfiguration:
    out: MSKSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("MSKClusterARN") is not None:
        out["msk_cluster_arn"] = data["MSKClusterARN"]
    else:
        out["msk_cluster_arn"] = ""
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    else:
        out["topic_name"] = ""
    if data.get("AuthenticationConfiguration") is not None:
        import capo_firehose.types.authentication_configuration

        out["authentication_configuration"] = (
            capo_firehose.types.authentication_configuration.deserialize_aws_json_1_1(
                data["AuthenticationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "MSKSourceConfiguration.authentication_configuration required"
        )
    if data.get("ReadFromTimestamp") is not None:
        import capo_firehose.types.read_from_timestamp

        out["read_from_timestamp"] = (
            capo_firehose.types.read_from_timestamp.deserialize_aws_json_1_1(
                data["ReadFromTimestamp"]
            )
        )
    return out
