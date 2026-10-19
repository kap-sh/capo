"""Generated from Smithy shape ``com.amazonaws.glue#GetCatalogsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_list
    import capo_glue.types.token


class GetCatalogsResponse(TypedDict, closed=True):
    catalog_list: "capo_glue.types.catalog_list.CatalogList"
    """<p>An array of <code>Catalog</code> objects. A list of <code>Catalog</code> objects from the specified parent catalog.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCatalogsResponse) -> dict:
    out: dict = {}
    import capo_glue.types.catalog_list

    out["CatalogList"] = capo_glue.types.catalog_list.serialize_aws_json_1_1(
        value["catalog_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCatalogsResponse:
    out: GetCatalogsResponse = {}  # type: ignore[typeddict-item]
    if data.get("CatalogList") is not None:
        import capo_glue.types.catalog_list

        out["catalog_list"] = capo_glue.types.catalog_list.deserialize_aws_json_1_1(
            data["CatalogList"]
        )
    else:
        out["catalog_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
