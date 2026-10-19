"""Generated from Smithy shape ``com.amazonaws.glue#BatchDeleteTableVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.batch_delete_table_version_list
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string


class BatchDeleteTableVersionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table. For Hive compatibility, this name is entirely lowercase.</p>"""
    version_ids: (
        "capo_glue.types.batch_delete_table_version_list.BatchDeleteTableVersionList"
    )
    """<p>A list of the IDs of versions to be deleted. A <code>VersionId</code> is a string representation of an integer. Each version is incremented by 1.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteTableVersionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.batch_delete_table_version_list

    out["VersionIds"] = (
        capo_glue.types.batch_delete_table_version_list.serialize_aws_json_1_1(
            value["version_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteTableVersionRequest:
    out: BatchDeleteTableVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("VersionIds") is not None:
        import capo_glue.types.batch_delete_table_version_list

        out["version_ids"] = (
            capo_glue.types.batch_delete_table_version_list.deserialize_aws_json_1_1(
                data["VersionIds"]
            )
        )
    else:
        out["version_ids"] = []
    return out
