"""Generated from Smithy shape ``com.amazonaws.glue#DirectJDBCSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.glue_schemas
    import capo_glue.types.jdbc_connection_type
    import capo_glue.types.node_name


class DirectJDBCSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the JDBC source connection.</p>"""
    database: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The database of the JDBC source connection.</p>"""
    table: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The table of the JDBC source connection.</p>"""
    connection_name: (
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The connection name of the JDBC source.</p>"""
    connection_type: "capo_glue.types.jdbc_connection_type.JDBCConnectionType"
    """<p>The connection type of the JDBC source.</p>"""
    redshift_tmp_dir: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The temp directory of the JDBC Redshift source.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the direct JDBC source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectJDBCSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    out["ConnectionName"] = value["connection_name"]
    import capo_glue.types.jdbc_connection_type

    out["ConnectionType"] = capo_glue.types.jdbc_connection_type.serialize_aws_json_1_1(
        value["connection_type"]
    )
    if "redshift_tmp_dir" in value:
        out["RedshiftTmpDir"] = value["redshift_tmp_dir"]
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectJDBCSource:
    out: DirectJDBCSource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        out["database"] = ""
    if data.get("Table") is not None:
        out["table"] = data["Table"]
    else:
        out["table"] = ""
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    else:
        out["connection_name"] = ""
    if data.get("ConnectionType") is not None:
        import capo_glue.types.jdbc_connection_type

        out["connection_type"] = (
            capo_glue.types.jdbc_connection_type.deserialize_aws_json_1_1(
                data["ConnectionType"]
            )
        )
    else:
        import typing

        out["connection_type"] = typing.cast(
            "capo_glue.types.jdbc_connection_type.JDBCConnectionType", ""
        )
    if data.get("RedshiftTmpDir") is not None:
        out["redshift_tmp_dir"] = data["RedshiftTmpDir"]
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
