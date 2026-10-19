"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContinuousBackupsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.continuous_backups_status
    import capo_dynamodb.types.point_in_time_recovery_description


class ContinuousBackupsDescription(TypedDict, closed=True):
    continuous_backups_status: (
        "capo_dynamodb.types.continuous_backups_status.ContinuousBackupsStatus"
    )
    """<p> <code>ContinuousBackupsStatus</code> can be one of the following states: ENABLED, DISABLED</p>"""
    point_in_time_recovery_description: NotRequired[
        "capo_dynamodb.types.point_in_time_recovery_description.PointInTimeRecoveryDescription"
    ]
    """<p>The description of the point in time recovery settings applied to the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContinuousBackupsDescription) -> dict:
    out: dict = {}
    import capo_dynamodb.types.continuous_backups_status

    out["ContinuousBackupsStatus"] = (
        capo_dynamodb.types.continuous_backups_status.serialize_aws_json_1_0(
            value["continuous_backups_status"]
        )
    )
    if "point_in_time_recovery_description" in value:
        import capo_dynamodb.types.point_in_time_recovery_description

        out["PointInTimeRecoveryDescription"] = (
            capo_dynamodb.types.point_in_time_recovery_description.serialize_aws_json_1_0(
                value["point_in_time_recovery_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ContinuousBackupsDescription:
    out: ContinuousBackupsDescription = {}  # type: ignore[typeddict-item]
    if data.get("ContinuousBackupsStatus") is not None:
        import capo_dynamodb.types.continuous_backups_status

        out["continuous_backups_status"] = (
            capo_dynamodb.types.continuous_backups_status.deserialize_aws_json_1_0(
                data["ContinuousBackupsStatus"]
            )
        )
    else:
        import typing

        out["continuous_backups_status"] = typing.cast(
            "capo_dynamodb.types.continuous_backups_status.ContinuousBackupsStatus", ""
        )
    if data.get("PointInTimeRecoveryDescription") is not None:
        import capo_dynamodb.types.point_in_time_recovery_description

        out["point_in_time_recovery_description"] = (
            capo_dynamodb.types.point_in_time_recovery_description.deserialize_aws_json_1_0(
                data["PointInTimeRecoveryDescription"]
            )
        )
    return out
