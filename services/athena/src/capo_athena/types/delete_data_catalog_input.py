"""Generated from Smithy shape ``com.amazonaws.athena#DeleteDataCatalogInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.boolean
    import capo_athena.types.catalog_name_string


class DeleteDataCatalogInput(TypedDict, closed=True):
    name: "capo_athena.types.catalog_name_string.CatalogNameString"
    """<p>The name of the data catalog to delete.</p>"""
    delete_catalog_only: NotRequired["capo_athena.types.boolean.Boolean"]
    """<p>Deletes the Athena Data Catalog. You can only use this with the <code>FEDERATED</code> catalogs. You usually perform this before registering the connector with Glue Data Catalog. After deletion, you will have to manage the Glue Connection and Lambda function. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataCatalogInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "delete_catalog_only" in value:
        out["DeleteCatalogOnly"] = value["delete_catalog_only"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataCatalogInput:
    out: DeleteDataCatalogInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("DeleteCatalogOnly") is not None:
        out["delete_catalog_only"] = data["DeleteCatalogOnly"]
    return out
