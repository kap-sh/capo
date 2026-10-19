"""Generated from Smithy shape ``com.amazonaws.glue#CreateTableOptimizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.table_optimizer_configuration
    import capo_glue.types.table_optimizer_type


class CreateTableOptimizerRequest(TypedDict, closed=True):
    catalog_id: "capo_glue.types.catalog_id_string.CatalogIdString"
    """<p>The Catalog ID of the table.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the database in the catalog in which the table resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table.</p>"""
    type: "capo_glue.types.table_optimizer_type.TableOptimizerType"
    """<p>The type of table optimizer.</p>"""
    table_optimizer_configuration: (
        "capo_glue.types.table_optimizer_configuration.TableOptimizerConfiguration"
    )
    """<p>A <code>TableOptimizerConfiguration</code> object representing the configuration of a table optimizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTableOptimizerRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.table_optimizer_type

    out["Type"] = capo_glue.types.table_optimizer_type.serialize_aws_json_1_1(
        value["type"]
    )
    import capo_glue.types.table_optimizer_configuration

    out["TableOptimizerConfiguration"] = (
        capo_glue.types.table_optimizer_configuration.serialize_aws_json_1_1(
            value["table_optimizer_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTableOptimizerRequest:
    out: CreateTableOptimizerRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    else:
        out["catalog_id"] = ""
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("Type") is not None:
        import capo_glue.types.table_optimizer_type

        out["type"] = capo_glue.types.table_optimizer_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_glue.types.table_optimizer_type.TableOptimizerType", ""
        )
    if data.get("TableOptimizerConfiguration") is not None:
        import capo_glue.types.table_optimizer_configuration

        out["table_optimizer_configuration"] = (
            capo_glue.types.table_optimizer_configuration.deserialize_aws_json_1_1(
                data["TableOptimizerConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTableOptimizerRequest.table_optimizer_configuration required"
        )
    return out
