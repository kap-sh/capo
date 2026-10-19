"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#GetDbParameterGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.arn
    import capo_timestream_influxdb.types.db_parameter_group_id
    import capo_timestream_influxdb.types.db_parameter_group_name
    import capo_timestream_influxdb.types.parameters


class GetDbParameterGroupOutput(TypedDict, closed=True):
    id: "capo_timestream_influxdb.types.db_parameter_group_id.DbParameterGroupId"
    """<p>A service-generated unique identifier.</p>"""
    name: "capo_timestream_influxdb.types.db_parameter_group_name.DbParameterGroupName"
    """<p>The customer-supplied name that uniquely identifies the DB parameter group when interacting with the Amazon Timestream for InfluxDB API and CLI commands.</p>"""
    arn: "capo_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the DB parameter group.</p>"""
    description: NotRequired["str"]
    """<p>A description of the DB parameter group.</p>"""
    parameters: NotRequired["capo_timestream_influxdb.types.parameters.Parameters"]
    """<p>The parameters that comprise the DB parameter group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbParameterGroupOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "parameters" in value:
        import capo_timestream_influxdb.types.parameters

        out["parameters"] = (
            capo_timestream_influxdb.types.parameters.serialize_aws_json_1_0(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbParameterGroupOutput:
    out: GetDbParameterGroupOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("parameters") is not None:
        import capo_timestream_influxdb.types.parameters

        out["parameters"] = (
            capo_timestream_influxdb.types.parameters.deserialize_aws_json_1_0(
                data["parameters"]
            )
        )
    return out
