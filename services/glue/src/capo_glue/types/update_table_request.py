"""Generated from Smithy shape ``com.amazonaws.glue#UpdateTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.boolean
    import capo_glue.types.boolean_nullable
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.table_input
    import capo_glue.types.transaction_id_string
    import capo_glue.types.update_open_table_format_input
    import capo_glue.types.version_string
    import capo_glue.types.view_update_action


class UpdateTableRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the catalog database in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>"""
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The unique identifier for the table within the specified database that will be created in the Glue Data Catalog.</p>"""
    table_input: NotRequired["capo_glue.types.table_input.TableInput"]
    """<p>An updated <code>TableInput</code> object to define the metadata table in the catalog.</p>"""
    skip_archive: NotRequired["capo_glue.types.boolean_nullable.BooleanNullable"]
    """<p>By default, <code>UpdateTable</code> always creates an archived version of the table before updating it. However, if <code>skipArchive</code> is set to true, <code>UpdateTable</code> does not create the archived version.</p>"""
    transaction_id: NotRequired[
        "capo_glue.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The transaction ID at which to update the table contents. </p>"""
    version_id: NotRequired["capo_glue.types.version_string.VersionString"]
    """<p>The version ID at which to update the table contents. </p>"""
    view_update_action: NotRequired[
        "capo_glue.types.view_update_action.ViewUpdateAction"
    ]
    """<p>The operation to be performed when updating the view.</p>"""
    force: NotRequired["capo_glue.types.boolean.Boolean"]
    """<p>A flag that can be set to true to ignore matching storage descriptor and subobject matching requirements.</p>"""
    update_open_table_format_input: NotRequired[
        "capo_glue.types.update_open_table_format_input.UpdateOpenTableFormatInput"
    ]
    """<p>Input parameters for updating open table format tables in GlueData Catalog, serving as a wrapper for format-specific update operations such as Apache Iceberg.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTableRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "table_input" in value:
        import capo_glue.types.table_input

        out["TableInput"] = capo_glue.types.table_input.serialize_aws_json_1_1(
            value["table_input"]
        )
    if "skip_archive" in value:
        out["SkipArchive"] = value["skip_archive"]
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "view_update_action" in value:
        import capo_glue.types.view_update_action

        out["ViewUpdateAction"] = (
            capo_glue.types.view_update_action.serialize_aws_json_1_1(
                value["view_update_action"]
            )
        )
    if "force" in value:
        out["Force"] = value["force"]
    if "update_open_table_format_input" in value:
        import capo_glue.types.update_open_table_format_input

        out["UpdateOpenTableFormatInput"] = (
            capo_glue.types.update_open_table_format_input.serialize_aws_json_1_1(
                value["update_open_table_format_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTableRequest:
    out: UpdateTableRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("UpdateTableRequest.database_name required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("TableInput") is not None:
        import capo_glue.types.table_input

        out["table_input"] = capo_glue.types.table_input.deserialize_aws_json_1_1(
            data["TableInput"]
        )
    if data.get("SkipArchive") is not None:
        out["skip_archive"] = data["SkipArchive"]
    if data.get("TransactionId") is not None:
        out["transaction_id"] = data["TransactionId"]
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    if data.get("ViewUpdateAction") is not None:
        import capo_glue.types.view_update_action

        out["view_update_action"] = (
            capo_glue.types.view_update_action.deserialize_aws_json_1_1(
                data["ViewUpdateAction"]
            )
        )
    if data.get("Force") is not None:
        out["force"] = data["Force"]
    if data.get("UpdateOpenTableFormatInput") is not None:
        import capo_glue.types.update_open_table_format_input

        out["update_open_table_format_input"] = (
            capo_glue.types.update_open_table_format_input.deserialize_aws_json_1_1(
                data["UpdateOpenTableFormatInput"]
            )
        )
    return out
