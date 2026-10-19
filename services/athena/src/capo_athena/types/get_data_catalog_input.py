"""Generated from Smithy shape ``com.amazonaws.athena#GetDataCatalogInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.catalog_name_string
    import capo_athena.types.work_group_name


class GetDataCatalogInput(TypedDict, closed=True):
    name: "capo_athena.types.catalog_name_string.CatalogNameString"
    """<p>The name of the data catalog to return.</p>"""
    work_group: NotRequired["capo_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup. Required if making an IAM Identity Center request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataCatalogInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataCatalogInput:
    out: GetDataCatalogInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    return out
