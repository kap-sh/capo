"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#AddApplicationOutputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.output_descriptions
    import capo_kinesis_analytics_v2.types.resource_arn


class AddApplicationOutputResponse(TypedDict, closed=True):
    application_arn: NotRequired[
        "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    ]
    """<p>The application Amazon Resource Name (ARN).</p>"""
    application_version_id: NotRequired[
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The updated application version ID. Kinesis Data Analytics increments this ID when the application is updated.</p>"""
    output_descriptions: NotRequired[
        "capo_kinesis_analytics_v2.types.output_descriptions.OutputDescriptions"
    ]
    """<p>Describes the application output configuration. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html">Configuring Application Output</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddApplicationOutputResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationARN"] = value["application_arn"]
    if "application_version_id" in value:
        out["ApplicationVersionId"] = value["application_version_id"]
    if "output_descriptions" in value:
        import capo_kinesis_analytics_v2.types.output_descriptions

        out["OutputDescriptions"] = (
            capo_kinesis_analytics_v2.types.output_descriptions.serialize_aws_json_1_1(
                value["output_descriptions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddApplicationOutputResponse:
    out: AddApplicationOutputResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationARN") is not None:
        out["application_arn"] = data["ApplicationARN"]
    if data.get("ApplicationVersionId") is not None:
        out["application_version_id"] = data["ApplicationVersionId"]
    if data.get("OutputDescriptions") is not None:
        import capo_kinesis_analytics_v2.types.output_descriptions

        out["output_descriptions"] = (
            capo_kinesis_analytics_v2.types.output_descriptions.deserialize_aws_json_1_1(
                data["OutputDescriptions"]
            )
        )
    return out
