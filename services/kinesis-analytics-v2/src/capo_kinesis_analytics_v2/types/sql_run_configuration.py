"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SqlRunConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.id
    import capo_kinesis_analytics_v2.types.input_starting_position_configuration


class SqlRunConfiguration(TypedDict, closed=True):
    input_id: "capo_kinesis_analytics_v2.types.id.Id"
    """<p>The input source ID. You can get this ID by calling the <a>DescribeApplication</a> operation. </p>"""
    input_starting_position_configuration: "capo_kinesis_analytics_v2.types.input_starting_position_configuration.InputStartingPositionConfiguration"
    """<p>The point at which you want the application to start processing records from the streaming source. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlRunConfiguration) -> dict:
    out: dict = {}
    out["InputId"] = value["input_id"]
    import capo_kinesis_analytics_v2.types.input_starting_position_configuration

    out["InputStartingPositionConfiguration"] = (
        capo_kinesis_analytics_v2.types.input_starting_position_configuration.serialize_aws_json_1_1(
            value["input_starting_position_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SqlRunConfiguration:
    out: SqlRunConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("InputId") is not None:
        out["input_id"] = data["InputId"]
    else:
        out["input_id"] = ""
    if data.get("InputStartingPositionConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.input_starting_position_configuration

        out["input_starting_position_configuration"] = (
            capo_kinesis_analytics_v2.types.input_starting_position_configuration.deserialize_aws_json_1_1(
                data["InputStartingPositionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "SqlRunConfiguration.input_starting_position_configuration required"
        )
    return out
