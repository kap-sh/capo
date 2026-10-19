"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#CreateDbParameterGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_parameter_group_name
    import capo_timestream_influxdb.types.parameters
    import capo_timestream_influxdb.types.request_tag_map


class CreateDbParameterGroupInput(TypedDict, closed=True):
    name: "capo_timestream_influxdb.types.db_parameter_group_name.DbParameterGroupName"
    """<p>The name of the DB parameter group. The name must be unique per customer and per region.</p>"""
    description: NotRequired["str"]
    """<p>A description of the DB parameter group.</p>"""
    parameters: NotRequired["capo_timestream_influxdb.types.parameters.Parameters"]
    """<p>A list of the parameters that comprise the DB parameter group.</p>"""
    tags: NotRequired["capo_timestream_influxdb.types.request_tag_map.RequestTagMap"]
    """<p>A list of key-value pairs to associate with the DB parameter group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDbParameterGroupInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "parameters" in value:
        import capo_timestream_influxdb.types.parameters

        out["parameters"] = (
            capo_timestream_influxdb.types.parameters.serialize_aws_json_1_0(
                value["parameters"]
            )
        )
    if "tags" in value:
        import capo_timestream_influxdb.types.request_tag_map

        out["tags"] = (
            capo_timestream_influxdb.types.request_tag_map.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDbParameterGroupInput:
    out: CreateDbParameterGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("parameters") is not None:
        import capo_timestream_influxdb.types.parameters

        out["parameters"] = (
            capo_timestream_influxdb.types.parameters.deserialize_aws_json_1_0(
                data["parameters"]
            )
        )
    if data.get("tags") is not None:
        import capo_timestream_influxdb.types.request_tag_map

        out["tags"] = (
            capo_timestream_influxdb.types.request_tag_map.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
