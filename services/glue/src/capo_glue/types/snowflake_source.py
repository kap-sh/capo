"""Generated from Smithy shape ``com.amazonaws.glue#SnowflakeSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.glue_schemas
    import capo_glue.types.node_name
    import capo_glue.types.snowflake_node_data


class SnowflakeSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the Snowflake data source.</p>"""
    data: "capo_glue.types.snowflake_node_data.SnowflakeNodeData"
    """<p>Configuration for the Snowflake data source.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies user-defined schemas for your output data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.snowflake_node_data

    out["Data"] = capo_glue.types.snowflake_node_data.serialize_aws_json_1_1(
        value["data"]
    )
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowflakeSource:
    out: SnowflakeSource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Data") is not None:
        import capo_glue.types.snowflake_node_data

        out["data"] = capo_glue.types.snowflake_node_data.deserialize_aws_json_1_1(
            data["Data"]
        )
    else:
        raise DeserializationError("SnowflakeSource.data required")
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
