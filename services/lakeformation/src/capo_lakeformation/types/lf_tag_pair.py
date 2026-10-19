"""Generated from Smithy shape ``com.amazonaws.lakeformation#LFTagPair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.lf_tag_key
    import capo_lakeformation.types.tag_value_list


class LFTagPair(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    tag_key: "capo_lakeformation.types.lf_tag_key.LFTagKey"
    """<p>The key-name for the LF-tag.</p>"""
    tag_values: "capo_lakeformation.types.tag_value_list.TagValueList"
    """<p>A list of possible values an attribute can take.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFTagPair) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["TagKey"] = value["tag_key"]
    import capo_lakeformation.types.tag_value_list

    out["TagValues"] = capo_lakeformation.types.tag_value_list.serialize_json(
        value["tag_values"]
    )
    return out


def deserialize_json(data: dict) -> LFTagPair:
    out: LFTagPair = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("TagKey") is not None:
        out["tag_key"] = data["TagKey"]
    else:
        out["tag_key"] = ""
    if data.get("TagValues") is not None:
        import capo_lakeformation.types.tag_value_list

        out["tag_values"] = capo_lakeformation.types.tag_value_list.deserialize_json(
            data["TagValues"]
        )
    else:
        out["tag_values"] = []
    return out
