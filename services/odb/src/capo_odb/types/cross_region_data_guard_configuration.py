"""Generated from Smithy shape ``com.amazonaws.odb#CrossRegionDataGuardConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.arn


class CrossRegionDataGuardConfiguration(TypedDict, closed=True):
    source_autonomous_database_arn: "capo_odb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the source Autonomous Database for the cross-Region Oracle Data Guard configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CrossRegionDataGuardConfiguration) -> dict:
    out: dict = {}
    out["sourceAutonomousDatabaseArn"] = value["source_autonomous_database_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CrossRegionDataGuardConfiguration:
    out: CrossRegionDataGuardConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceAutonomousDatabaseArn") is not None:
        out["source_autonomous_database_arn"] = data["sourceAutonomousDatabaseArn"]
    else:
        out["source_autonomous_database_arn"] = ""
    return out
