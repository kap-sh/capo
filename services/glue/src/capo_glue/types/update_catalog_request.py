"""Generated from Smithy shape ``com.amazonaws.glue#UpdateCatalogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.catalog_input


class UpdateCatalogRequest(TypedDict, closed=True):
    catalog_id: "capo_glue.types.catalog_id_string.CatalogIdString"
    """<p>The ID of the catalog.</p>"""
    catalog_input: "capo_glue.types.catalog_input.CatalogInput"
    """<p>A <code>CatalogInput</code> object specifying the new properties of an existing catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCatalogRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    import capo_glue.types.catalog_input

    out["CatalogInput"] = capo_glue.types.catalog_input.serialize_aws_json_1_1(
        value["catalog_input"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCatalogRequest:
    out: UpdateCatalogRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    else:
        out["catalog_id"] = ""
    if data.get("CatalogInput") is not None:
        import capo_glue.types.catalog_input

        out["catalog_input"] = capo_glue.types.catalog_input.deserialize_aws_json_1_1(
            data["CatalogInput"]
        )
    else:
        raise DeserializationError("UpdateCatalogRequest.catalog_input required")
    return out
