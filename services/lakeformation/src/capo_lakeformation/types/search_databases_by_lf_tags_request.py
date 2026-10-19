"""Generated from Smithy shape ``com.amazonaws.lakeformation#SearchDatabasesByLFTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.expression
    import capo_lakeformation.types.search_page_size
    import capo_lakeformation.types.token


class SearchDatabasesByLFTagsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is not the first call to retrieve this list.</p>"""
    max_results: NotRequired["capo_lakeformation.types.search_page_size.SearchPageSize"]
    """<p>The maximum number of results to return.</p>"""
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    expression: "capo_lakeformation.types.expression.Expression"
    """<p>A list of conditions (<code>LFTag</code> structures) to search for in database resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDatabasesByLFTagsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import capo_lakeformation.types.expression

    out["Expression"] = capo_lakeformation.types.expression.serialize_json(
        value["expression"]
    )
    return out


def deserialize_json(data: dict) -> SearchDatabasesByLFTagsRequest:
    out: SearchDatabasesByLFTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("Expression") is not None:
        import capo_lakeformation.types.expression

        out["expression"] = capo_lakeformation.types.expression.deserialize_json(
            data["Expression"]
        )
    else:
        out["expression"] = []
    return out
