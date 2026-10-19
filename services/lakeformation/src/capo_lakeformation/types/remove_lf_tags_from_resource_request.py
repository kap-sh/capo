"""Generated from Smithy shape ``com.amazonaws.lakeformation#RemoveLFTagsFromResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.lf_tags_list
    import capo_lakeformation.types.resource


class RemoveLFTagsFromResourceRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    resource: "capo_lakeformation.types.resource.Resource"
    """<p>The database, table, or column resource where you want to remove an LF-tag.</p>"""
    lf_tags: "capo_lakeformation.types.lf_tags_list.LFTagsList"
    """<p>The LF-tags to be removed from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveLFTagsFromResourceRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import capo_lakeformation.types.resource

    out["Resource"] = capo_lakeformation.types.resource.serialize_json(
        value["resource"]
    )
    import capo_lakeformation.types.lf_tags_list

    out["LFTags"] = capo_lakeformation.types.lf_tags_list.serialize_json(
        value["lf_tags"]
    )
    return out


def deserialize_json(data: dict) -> RemoveLFTagsFromResourceRequest:
    out: RemoveLFTagsFromResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("Resource") is not None:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    else:
        raise DeserializationError("RemoveLFTagsFromResourceRequest.resource required")
    if data.get("LFTags") is not None:
        import capo_lakeformation.types.lf_tags_list

        out["lf_tags"] = capo_lakeformation.types.lf_tags_list.deserialize_json(
            data["LFTags"]
        )
    else:
        out["lf_tags"] = []
    return out
