"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateTimeToLiveInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.time_to_live_specification


class UpdateTimeToLiveInput(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table to be configured. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    time_to_live_specification: (
        "capo_dynamodb.types.time_to_live_specification.TimeToLiveSpecification"
    )
    """<p>Represents the settings used to enable or disable Time to Live for the specified table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTimeToLiveInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    import capo_dynamodb.types.time_to_live_specification

    out["TimeToLiveSpecification"] = (
        capo_dynamodb.types.time_to_live_specification.serialize_aws_json_1_0(
            value["time_to_live_specification"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTimeToLiveInput:
    out: UpdateTimeToLiveInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("TimeToLiveSpecification") is not None:
        import capo_dynamodb.types.time_to_live_specification

        out["time_to_live_specification"] = (
            capo_dynamodb.types.time_to_live_specification.deserialize_aws_json_1_0(
                data["TimeToLiveSpecification"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTimeToLiveInput.time_to_live_specification required"
        )
    return out
