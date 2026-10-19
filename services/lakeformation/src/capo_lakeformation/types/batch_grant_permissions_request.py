"""Generated from Smithy shape ``com.amazonaws.lakeformation#BatchGrantPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.batch_permissions_request_entry_list
    import capo_lakeformation.types.catalog_id_string


class BatchGrantPermissionsRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    entries: "capo_lakeformation.types.batch_permissions_request_entry_list.BatchPermissionsRequestEntryList"
    """<p>A list of up to 20 entries for resource permissions to be granted by batch operation to the principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGrantPermissionsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import capo_lakeformation.types.batch_permissions_request_entry_list

    out["Entries"] = (
        capo_lakeformation.types.batch_permissions_request_entry_list.serialize_json(
            value["entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGrantPermissionsRequest:
    out: BatchGrantPermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("Entries") is not None:
        import capo_lakeformation.types.batch_permissions_request_entry_list

        out["entries"] = (
            capo_lakeformation.types.batch_permissions_request_entry_list.deserialize_json(
                data["Entries"]
            )
        )
    else:
        out["entries"] = []
    return out
