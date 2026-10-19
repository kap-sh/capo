"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateLFTagRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.lf_tag_key
    import capo_lakeformation.types.tag_value_list


class UpdateLFTagRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    tag_key: "capo_lakeformation.types.lf_tag_key.LFTagKey"
    """<p>The key-name for the LF-tag for which to add or delete values.</p>"""
    tag_values_to_delete: NotRequired[
        "capo_lakeformation.types.tag_value_list.TagValueList"
    ]
    """<p>A list of LF-tag values to delete from the LF-tag.</p>"""
    tag_values_to_add: NotRequired[
        "capo_lakeformation.types.tag_value_list.TagValueList"
    ]
    """<p>A list of LF-tag values to add from the LF-tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLFTagRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["TagKey"] = value["tag_key"]
    if "tag_values_to_delete" in value:
        import capo_lakeformation.types.tag_value_list

        out["TagValuesToDelete"] = (
            capo_lakeformation.types.tag_value_list.serialize_json(
                value["tag_values_to_delete"]
            )
        )
    if "tag_values_to_add" in value:
        import capo_lakeformation.types.tag_value_list

        out["TagValuesToAdd"] = capo_lakeformation.types.tag_value_list.serialize_json(
            value["tag_values_to_add"]
        )
    return out


def deserialize_json(data: dict) -> UpdateLFTagRequest:
    out: UpdateLFTagRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("TagKey") is not None:
        out["tag_key"] = data["TagKey"]
    else:
        out["tag_key"] = ""
    if data.get("TagValuesToDelete") is not None:
        import capo_lakeformation.types.tag_value_list

        out["tag_values_to_delete"] = (
            capo_lakeformation.types.tag_value_list.deserialize_json(
                data["TagValuesToDelete"]
            )
        )
    if data.get("TagValuesToAdd") is not None:
        import capo_lakeformation.types.tag_value_list

        out["tag_values_to_add"] = (
            capo_lakeformation.types.tag_value_list.deserialize_json(
                data["TagValuesToAdd"]
            )
        )
    return out
