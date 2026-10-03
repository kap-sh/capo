"""Generated from Smithy shape ``com.amazonaws.appflow#GlueDataCatalogConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.glue_data_catalog_database_name
    import capo_appflow.types.glue_data_catalog_iam_role
    import capo_appflow.types.glue_data_catalog_table_prefix


class GlueDataCatalogConfig(TypedDict, closed=True):
    role_arn: "capo_appflow.types.glue_data_catalog_iam_role.GlueDataCatalogIAMRole"
    """<p>The Amazon Resource Name (ARN) of an IAM role that grants Amazon AppFlow the permissions it needs to create Data Catalog tables, databases, and partitions.</p> <p>For an example IAM policy that has the required permissions, see <a href="https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_id-based-policy-examples.html">Identity-based policy examples for Amazon AppFlow</a>.</p>"""
    database_name: (
        "capo_appflow.types.glue_data_catalog_database_name.GlueDataCatalogDatabaseName"
    )
    """<p>The name of the Data Catalog database that stores the metadata tables that Amazon AppFlow creates in your Amazon Web Services account. These tables contain metadata for the data that's transferred by the flow that you configure with this parameter.</p> <note> <p>When you configure a new flow with this parameter, you must specify an existing database.</p> </note>"""
    table_prefix: (
        "capo_appflow.types.glue_data_catalog_table_prefix.GlueDataCatalogTablePrefix"
    )
    """<p>A naming prefix for each Data Catalog table that Amazon AppFlow creates for the flow that you configure with this setting. Amazon AppFlow adds the prefix to the beginning of the each table name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueDataCatalogConfig) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["databaseName"] = value["database_name"]
    out["tablePrefix"] = value["table_prefix"]
    return out


def deserialize_json(data: dict) -> GlueDataCatalogConfig:
    out: GlueDataCatalogConfig = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GlueDataCatalogConfig.role_arn required")
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError("GlueDataCatalogConfig.database_name required")
    if data.get("tablePrefix") is not None:
        out["table_prefix"] = data["tablePrefix"]
    else:
        raise DeserializationError("GlueDataCatalogConfig.table_prefix required")
    return out
