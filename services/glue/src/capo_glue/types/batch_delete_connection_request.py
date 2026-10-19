"""Generated from Smithy shape ``com.amazonaws.glue#BatchDeleteConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.delete_connection_name_list


class BatchDeleteConnectionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the connections reside. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    connection_name_list: (
        "capo_glue.types.delete_connection_name_list.DeleteConnectionNameList"
    )
    """<p>A list of names of the connections to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteConnectionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import capo_glue.types.delete_connection_name_list

    out["ConnectionNameList"] = (
        capo_glue.types.delete_connection_name_list.serialize_aws_json_1_1(
            value["connection_name_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteConnectionRequest:
    out: BatchDeleteConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("ConnectionNameList") is not None:
        import capo_glue.types.delete_connection_name_list

        out["connection_name_list"] = (
            capo_glue.types.delete_connection_name_list.deserialize_aws_json_1_1(
                data["ConnectionNameList"]
            )
        )
    else:
        out["connection_name_list"] = []
    return out
