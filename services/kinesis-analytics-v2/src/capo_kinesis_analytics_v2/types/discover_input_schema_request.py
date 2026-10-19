"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DiscoverInputSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.input_processing_configuration
    import capo_kinesis_analytics_v2.types.input_starting_position_configuration
    import capo_kinesis_analytics_v2.types.resource_arn
    import capo_kinesis_analytics_v2.types.role_arn
    import capo_kinesis_analytics_v2.types.s3_configuration


class DiscoverInputSchemaRequest(TypedDict, closed=True):
    resource_arn: NotRequired[
        "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the streaming source.</p>"""
    service_execution_role: "capo_kinesis_analytics_v2.types.role_arn.RoleARN"
    """<p>The ARN of the role that is used to access the streaming source.</p>"""
    input_starting_position_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.input_starting_position_configuration.InputStartingPositionConfiguration"
    ]
    """<p>The point at which you want Kinesis Data Analytics to start reading records from the specified streaming source for discovery purposes.</p>"""
    s3_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.s3_configuration.S3Configuration"
    ]
    """<p>Specify this parameter to discover a schema from data in an Amazon S3 object.</p>"""
    input_processing_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.input_processing_configuration.InputProcessingConfiguration"
    ]
    """<p>The <a>InputProcessingConfiguration</a> to use to preprocess the records before discovering the schema of the records.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoverInputSchemaRequest) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    out["ServiceExecutionRole"] = value["service_execution_role"]
    if "input_starting_position_configuration" in value:
        import capo_kinesis_analytics_v2.types.input_starting_position_configuration

        out["InputStartingPositionConfiguration"] = (
            capo_kinesis_analytics_v2.types.input_starting_position_configuration.serialize_aws_json_1_1(
                value["input_starting_position_configuration"]
            )
        )
    if "s3_configuration" in value:
        import capo_kinesis_analytics_v2.types.s3_configuration

        out["S3Configuration"] = (
            capo_kinesis_analytics_v2.types.s3_configuration.serialize_aws_json_1_1(
                value["s3_configuration"]
            )
        )
    if "input_processing_configuration" in value:
        import capo_kinesis_analytics_v2.types.input_processing_configuration

        out["InputProcessingConfiguration"] = (
            capo_kinesis_analytics_v2.types.input_processing_configuration.serialize_aws_json_1_1(
                value["input_processing_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoverInputSchemaRequest:
    out: DiscoverInputSchemaRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("ServiceExecutionRole") is not None:
        out["service_execution_role"] = data["ServiceExecutionRole"]
    else:
        out["service_execution_role"] = ""
    if data.get("InputStartingPositionConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.input_starting_position_configuration

        out["input_starting_position_configuration"] = (
            capo_kinesis_analytics_v2.types.input_starting_position_configuration.deserialize_aws_json_1_1(
                data["InputStartingPositionConfiguration"]
            )
        )
    if data.get("S3Configuration") is not None:
        import capo_kinesis_analytics_v2.types.s3_configuration

        out["s3_configuration"] = (
            capo_kinesis_analytics_v2.types.s3_configuration.deserialize_aws_json_1_1(
                data["S3Configuration"]
            )
        )
    if data.get("InputProcessingConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.input_processing_configuration

        out["input_processing_configuration"] = (
            capo_kinesis_analytics_v2.types.input_processing_configuration.deserialize_aws_json_1_1(
                data["InputProcessingConfiguration"]
            )
        )
    return out
