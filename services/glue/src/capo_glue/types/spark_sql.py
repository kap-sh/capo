"""Generated from Smithy shape ``com.amazonaws.glue#SparkSQL``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.glue_schemas
    import capo_glue.types.many_inputs
    import capo_glue.types.node_name
    import capo_glue.types.sql_aliases
    import capo_glue.types.sql_query


class SparkSQL(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.many_inputs.ManyInputs"
    """<p>The data inputs identified by their node names. You can associate a table name with each input node to use in the SQL query. The name you choose must meet the Spark SQL naming restrictions.</p>"""
    sql_query: "capo_glue.types.sql_query.SqlQuery"
    """<p>A SQL query that must use Spark SQL syntax and return a single data set.</p>"""
    sql_aliases: "capo_glue.types.sql_aliases.SqlAliases"
    """<p>A list of aliases. An alias allows you to specify what name to use in the SQL for a given input. For example, you have a datasource named "MyDataSource". If you specify <code>From</code> as MyDataSource, and <code>Alias</code> as SqlName, then in your SQL you can do:</p> <p> <code>select * from SqlName</code> </p> <p>and that gets data from MyDataSource.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the SparkSQL transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SparkSQL) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.many_inputs

    out["Inputs"] = capo_glue.types.many_inputs.serialize_aws_json_1_1(value["inputs"])
    out["SqlQuery"] = value["sql_query"]
    import capo_glue.types.sql_aliases

    out["SqlAliases"] = capo_glue.types.sql_aliases.serialize_aws_json_1_1(
        value["sql_aliases"]
    )
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SparkSQL:
    out: SparkSQL = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SparkSQL.name required")
    if data.get("Inputs") is not None:
        import capo_glue.types.many_inputs

        out["inputs"] = capo_glue.types.many_inputs.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("SparkSQL.inputs required")
    if data.get("SqlQuery") is not None:
        out["sql_query"] = data["SqlQuery"]
    else:
        raise DeserializationError("SparkSQL.sql_query required")
    if data.get("SqlAliases") is not None:
        import capo_glue.types.sql_aliases

        out["sql_aliases"] = capo_glue.types.sql_aliases.deserialize_aws_json_1_1(
            data["SqlAliases"]
        )
    else:
        raise DeserializationError("SparkSQL.sql_aliases required")
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
