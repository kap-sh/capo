"""Generated from Smithy shape ``com.amazonaws.glue#CreateCatalogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_input
    import capo_glue.types.catalog_name_string
    import capo_glue.types.tags_map


class CreateCatalogRequest(TypedDict, closed=True):
    name: "capo_glue.types.catalog_name_string.CatalogNameString"
    """<p>The name of the catalog to create.</p>"""
    catalog_input: "capo_glue.types.catalog_input.CatalogInput"
    """<p>A <code>CatalogInput</code> object that defines the metadata for the catalog.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>A map array of key-value pairs, not more than 50 pairs. Each key is a UTF-8 string, not less than 1 or more than 128 bytes long. Each value is a UTF-8 string, not more than 256 bytes long. The tags you assign to the catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCatalogRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.catalog_input

    out["CatalogInput"] = capo_glue.types.catalog_input.serialize_aws_json_1_1(
        value["catalog_input"]
    )
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCatalogRequest:
    out: CreateCatalogRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("CatalogInput") is not None:
        import capo_glue.types.catalog_input

        out["catalog_input"] = capo_glue.types.catalog_input.deserialize_aws_json_1_1(
            data["CatalogInput"]
        )
    else:
        raise DeserializationError("CreateCatalogRequest.catalog_input required")
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
