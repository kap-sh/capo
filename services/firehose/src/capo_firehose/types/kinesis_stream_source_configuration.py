"""Generated from Smithy shape ``com.amazonaws.firehose#KinesisStreamSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.kinesis_stream_arn
    import capo_firehose.types.role_arn


class KinesisStreamSourceConfiguration(TypedDict, closed=True):
    kinesis_stream_arn: "capo_firehose.types.kinesis_stream_arn.KinesisStreamARN"
    """<p>The ARN of the source Kinesis data stream. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams">Amazon Kinesis Data Streams ARN Format</a>.</p>"""
    role_arn: "capo_firehose.types.role_arn.RoleARN"
    """<p>The ARN of the role that provides access to the source Kinesis data stream. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam">Amazon Web Services Identity and Access Management (IAM) ARN Format</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisStreamSourceConfiguration) -> dict:
    out: dict = {}
    out["KinesisStreamARN"] = value["kinesis_stream_arn"]
    out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisStreamSourceConfiguration:
    out: KinesisStreamSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KinesisStreamARN") is not None:
        out["kinesis_stream_arn"] = data["KinesisStreamARN"]
    else:
        raise DeserializationError(
            "KinesisStreamSourceConfiguration.kinesis_stream_arn required"
        )
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("KinesisStreamSourceConfiguration.role_arn required")
    return out
