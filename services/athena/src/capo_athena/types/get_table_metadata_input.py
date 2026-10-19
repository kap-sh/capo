"""Generated from Smithy shape ``com.amazonaws.athena#GetTableMetadataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.catalog_name_string
    import capo_athena.types.name_string
    import capo_athena.types.work_group_name


class GetTableMetadataInput(TypedDict, closed=True):
    catalog_name: "capo_athena.types.catalog_name_string.CatalogNameString"
    """<p>The name of the data catalog that contains the database and table metadata to return.</p>"""
    database_name: "capo_athena.types.name_string.NameString"
    """<p>The name of the database that contains the table metadata to return.</p>"""
    table_name: "capo_athena.types.name_string.NameString"
    """<p>The name of the table for which metadata is returned.</p>"""
    work_group: NotRequired["capo_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup for which the metadata is being fetched. Required if requesting an IAM Identity Center enabled Glue Data Catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableMetadataInput) -> dict:
    out: dict = {}
    out["CatalogName"] = value["catalog_name"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableMetadataInput:
    out: GetTableMetadataInput = {}  # type: ignore[typeddict-item]
    if data.get("CatalogName") is not None:
        out["catalog_name"] = data["CatalogName"]
    else:
        out["catalog_name"] = ""
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    return out
