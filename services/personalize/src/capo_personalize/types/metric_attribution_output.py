"""Generated from Smithy shape ``com.amazonaws.personalize#MetricAttributionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.role_arn
    import capo_personalize.types.s3_data_config


class MetricAttributionOutput(TypedDict, closed=True):
    s3_data_destination: NotRequired[
        "capo_personalize.types.s3_data_config.S3DataConfig"
    ]
    role_arn: "capo_personalize.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM service role that has permissions to add data to your output Amazon S3 bucket and add metrics to Amazon CloudWatch. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/measuring-recommendation-impact.html">Measuring impact of recommendations</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricAttributionOutput) -> dict:
    out: dict = {}
    if "s3_data_destination" in value:
        import capo_personalize.types.s3_data_config

        out["s3DataDestination"] = (
            capo_personalize.types.s3_data_config.serialize_aws_json_1_1(
                value["s3_data_destination"]
            )
        )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricAttributionOutput:
    out: MetricAttributionOutput = {}  # type: ignore[typeddict-item]
    if data.get("s3DataDestination") is not None:
        import capo_personalize.types.s3_data_config

        out["s3_data_destination"] = (
            capo_personalize.types.s3_data_config.deserialize_aws_json_1_1(
                data["s3DataDestination"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("MetricAttributionOutput.role_arn required")
    return out
