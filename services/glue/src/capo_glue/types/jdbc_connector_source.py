"""Generated from Smithy shape ``com.amazonaws.glue#JDBCConnectorSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.enclosed_in_string_property_with_quote
    import capo_glue.types.glue_schemas
    import capo_glue.types.jdbc_connector_options
    import capo_glue.types.node_name
    import capo_glue.types.sql_query


class JDBCConnectorSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data source.</p>"""
    connection_name: (
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The name of the connection that is associated with the connector.</p>"""
    connector_name: (
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The name of a connector that assists with accessing the data store in Glue Studio.</p>"""
    connection_type: (
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The type of connection, such as marketplace.jdbc or custom.jdbc, designating a connection to a JDBC data store.</p>"""
    additional_options: NotRequired[
        "capo_glue.types.jdbc_connector_options.JDBCConnectorOptions"
    ]
    """<p>Additional connection options for the connector.</p>"""
    connection_table: NotRequired[
        "capo_glue.types.enclosed_in_string_property_with_quote.EnclosedInStringPropertyWithQuote"
    ]
    """<p>The name of the table in the data source.</p>"""
    query: NotRequired["capo_glue.types.sql_query.SqlQuery"]
    """<p>The table or SQL query to get the data from. You can specify either <code>ConnectionTable</code> or <code>query</code>, but not both.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the custom JDBC source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JDBCConnectorSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ConnectionName"] = value["connection_name"]
    out["ConnectorName"] = value["connector_name"]
    out["ConnectionType"] = value["connection_type"]
    if "additional_options" in value:
        import capo_glue.types.jdbc_connector_options

        out["AdditionalOptions"] = (
            capo_glue.types.jdbc_connector_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "connection_table" in value:
        out["ConnectionTable"] = value["connection_table"]
    if "query" in value:
        out["Query"] = value["query"]
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JDBCConnectorSource:
    out: JDBCConnectorSource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    else:
        out["connection_name"] = ""
    if data.get("ConnectorName") is not None:
        out["connector_name"] = data["ConnectorName"]
    else:
        out["connector_name"] = ""
    if data.get("ConnectionType") is not None:
        out["connection_type"] = data["ConnectionType"]
    else:
        out["connection_type"] = ""
    if data.get("AdditionalOptions") is not None:
        import capo_glue.types.jdbc_connector_options

        out["additional_options"] = (
            capo_glue.types.jdbc_connector_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if data.get("ConnectionTable") is not None:
        out["connection_table"] = data["ConnectionTable"]
    if data.get("Query") is not None:
        out["query"] = data["Query"]
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
