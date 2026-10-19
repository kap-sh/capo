"""Generated from Smithy shape ``com.amazonaws.athena#GetDatabaseInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.catalog_name_string
    import capo_athena.types.name_string
    import capo_athena.types.work_group_name


class GetDatabaseInput(TypedDict, closed=True):
    catalog_name: "capo_athena.types.catalog_name_string.CatalogNameString"
    """<p>The name of the data catalog that contains the database to return.</p>"""
    database_name: "capo_athena.types.name_string.NameString"
    """<p>The name of the database to return.</p>"""
    work_group: NotRequired["capo_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup for which the metadata is being fetched. Required if requesting an IAM Identity Center enabled Glue Data Catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDatabaseInput) -> dict:
    out: dict = {}
    out["CatalogName"] = value["catalog_name"]
    out["DatabaseName"] = value["database_name"]
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDatabaseInput:
    out: GetDatabaseInput = {}  # type: ignore[typeddict-item]
    if data.get("CatalogName") is not None:
        out["catalog_name"] = data["CatalogName"]
    else:
        out["catalog_name"] = ""
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    return out
