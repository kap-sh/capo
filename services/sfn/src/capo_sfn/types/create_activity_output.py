"""Generated from Smithy shape ``com.amazonaws.sfn#CreateActivityOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.timestamp


class CreateActivityOutput(TypedDict, closed=True):
    activity_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the created activity.</p>"""
    creation_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date the activity is created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateActivityOutput) -> dict:
    out: dict = {}
    out["activityArn"] = value["activity_arn"]
    import capo_sfn.types.timestamp

    out["creationDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateActivityOutput:
    out: CreateActivityOutput = {}  # type: ignore[typeddict-item]
    if data.get("activityArn") is not None:
        out["activity_arn"] = data["activityArn"]
    else:
        out["activity_arn"] = ""
    if data.get("creationDate") is not None:
        import capo_sfn.types.timestamp

        out["creation_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        import datetime

        out["creation_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
