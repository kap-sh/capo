"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateContinuousBackupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.point_in_time_recovery_specification
    import capo_dynamodb.types.table_arn


class UpdateContinuousBackupsInput(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    point_in_time_recovery_specification: "capo_dynamodb.types.point_in_time_recovery_specification.PointInTimeRecoverySpecification"
    """<p>Represents the settings used to enable point in time recovery.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateContinuousBackupsInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    import capo_dynamodb.types.point_in_time_recovery_specification

    out["PointInTimeRecoverySpecification"] = (
        capo_dynamodb.types.point_in_time_recovery_specification.serialize_aws_json_1_0(
            value["point_in_time_recovery_specification"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateContinuousBackupsInput:
    out: UpdateContinuousBackupsInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("PointInTimeRecoverySpecification") is not None:
        import capo_dynamodb.types.point_in_time_recovery_specification

        out["point_in_time_recovery_specification"] = (
            capo_dynamodb.types.point_in_time_recovery_specification.deserialize_aws_json_1_0(
                data["PointInTimeRecoverySpecification"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateContinuousBackupsInput.point_in_time_recovery_specification required"
        )
    return out
