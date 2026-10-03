"""Generated from Smithy shape ``com.amazonaws.glue#ConnectorDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.connector_options
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.glue_schemas
    import capo_glue.types.node_name


class ConnectorDataSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of this source node.</p>"""
    connection_type: (
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The <code>connectionType</code>, as provided to the underlying Glue library. This node type supports the following connection types: </p> <ul> <li> <p> <code>opensearch</code> </p> </li> <li> <p> <code>azuresql</code> </p> </li> <li> <p> <code>azurecosmos</code> </p> </li> <li> <p> <code>bigquery</code> </p> </li> <li> <p> <code>saphana</code> </p> </li> <li> <p> <code>teradata</code> </p> </li> <li> <p> <code>vertica</code> </p> </li> </ul>"""
    data: "capo_glue.types.connector_options.ConnectorOptions"
    """<p>A map specifying connection options for the node. You can find standard connection options for the corresponding connection type in the <a href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html"> Connection parameters</a> section of the Glue documentation.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for this source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorDataSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ConnectionType"] = value["connection_type"]
    import capo_glue.types.connector_options

    out["Data"] = capo_glue.types.connector_options.serialize_aws_json_1_1(
        value["data"]
    )
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorDataSource:
    out: ConnectorDataSource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ConnectorDataSource.name required")
    if data.get("ConnectionType") is not None:
        out["connection_type"] = data["ConnectionType"]
    else:
        raise DeserializationError("ConnectorDataSource.connection_type required")
    if data.get("Data") is not None:
        import capo_glue.types.connector_options

        out["data"] = capo_glue.types.connector_options.deserialize_aws_json_1_1(
            data["Data"]
        )
    else:
        raise DeserializationError("ConnectorDataSource.data required")
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
