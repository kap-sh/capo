"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#GetDbParameterGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_parameter_group_identifier


class GetDbParameterGroupInput(TypedDict, closed=True):
    identifier: "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
    """<p>The id of the DB parameter group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbParameterGroupInput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbParameterGroupInput:
    out: GetDbParameterGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
