"""Generated from Smithy shape ``com.amazonaws.glue#AthenaConnectorSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.enclosed_in_string_property_with_quote
    import capo_glue.types.glue_schemas
    import capo_glue.types.node_name


class AthenaConnectorSource(TypedDict, closed=True):
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
    """<p>The type of connection, such as marketplace.athena or custom.athena, designating a connection to an Amazon Athena data store.</p>"""
    connection_table: NotRequired[
        "capo_glue.types.enclosed_in_string_property_with_quote.EnclosedInStringPropertyWithQuote"
    ]
    """<p>The name of the table in the data source.</p>"""
    schema_name: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the Cloudwatch log group to read from. For example, <code>/aws-glue/jobs/output</code>.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the custom Athena source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AthenaConnectorSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ConnectionName"] = value["connection_name"]
    out["ConnectorName"] = value["connector_name"]
    out["ConnectionType"] = value["connection_type"]
    if "connection_table" in value:
        out["ConnectionTable"] = value["connection_table"]
    out["SchemaName"] = value["schema_name"]
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AthenaConnectorSource:
    out: AthenaConnectorSource = {}  # type: ignore[typeddict-item]
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
    if data.get("ConnectionTable") is not None:
        out["connection_table"] = data["ConnectionTable"]
    if data.get("SchemaName") is not None:
        out["schema_name"] = data["SchemaName"]
    else:
        out["schema_name"] = ""
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
