"""Generated from Smithy shape ``com.amazonaws.glue#DynamoDBCatalogSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boxed_boolean
    import capo_glue.types.ddbelt_catalog_additional_options
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.node_name


class DynamoDBCatalogSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data source.</p>"""
    database: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to read from.</p>"""
    table: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to read from.</p>"""
    pitr_enabled: NotRequired["capo_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether Point-in-Time Recovery (PITR) is enabled for the DynamoDB table. When set to <code>true</code>, allows reading from a specific point in time. The default value is <code>false</code>.</p>"""
    additional_options: NotRequired[
        "capo_glue.types.ddbelt_catalog_additional_options.DDBELTCatalogAdditionalOptions"
    ]
    """<p>Specifies additional connection options for the DynamoDB data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamoDBCatalogSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    if "pitr_enabled" in value:
        out["PitrEnabled"] = value["pitr_enabled"]
    if "additional_options" in value:
        import capo_glue.types.ddbelt_catalog_additional_options

        out["AdditionalOptions"] = (
            capo_glue.types.ddbelt_catalog_additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DynamoDBCatalogSource:
    out: DynamoDBCatalogSource = {}  # type: ignore[typeddict-item]
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
    if data.get("PitrEnabled") is not None:
        out["pitr_enabled"] = data["PitrEnabled"]
    if data.get("AdditionalOptions") is not None:
        import capo_glue.types.ddbelt_catalog_additional_options

        out["additional_options"] = (
            capo_glue.types.ddbelt_catalog_additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    return out
