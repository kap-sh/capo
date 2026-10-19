"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#TimestreamConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.iam_role_arn
    import capo_iotfleetwise.types.timestream_table_arn


class TimestreamConfig(TypedDict, closed=True):
    timestream_table_arn: (
        "capo_iotfleetwise.types.timestream_table_arn.TimestreamTableArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon Timestream table.</p>"""
    execution_role_arn: "capo_iotfleetwise.types.iam_role_arn.IAMRoleArn"
    """<p>The Amazon Resource Name (ARN) of the task execution role that grants Amazon Web Services IoT FleetWise permission to deliver data to the Amazon Timestream table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimestreamConfig) -> dict:
    out: dict = {}
    out["timestreamTableArn"] = value["timestream_table_arn"]
    out["executionRoleArn"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimestreamConfig:
    out: TimestreamConfig = {}  # type: ignore[typeddict-item]
    if data.get("timestreamTableArn") is not None:
        out["timestream_table_arn"] = data["timestreamTableArn"]
    else:
        out["timestream_table_arn"] = ""
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    return out
