"""Generated from Smithy shape ``com.amazonaws.glue#GetCatalogsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boolean
    import capo_glue.types.catalog_id_string
    import capo_glue.types.nullable_boolean
    import capo_glue.types.page_size
    import capo_glue.types.token


class GetCatalogsRequest(TypedDict, closed=True):
    parent_catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the parent catalog in which the catalog resides. If none is provided, the Amazon Web Services Account Number is used by default.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of catalogs to return in one response.</p>"""
    recursive: NotRequired["capo_glue.types.boolean.Boolean"]
    """<p>Whether to list all catalogs across the catalog hierarchy, starting from the <code>ParentCatalogId</code>. Defaults to <code>false</code> . When <code>true</code>, all catalog objects in the <code>ParentCatalogID</code> hierarchy are enumerated in the response.</p>"""
    include_root: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Whether to list the default catalog in the account and region in the response. Defaults to <code>false</code>. When <code>true</code> and <code>ParentCatalogId = NULL | Amazon Web Services Account ID</code>, all catalogs and the default catalog are enumerated in the response.</p> <p>When the <code>ParentCatalogId</code> is not equal to null, and this attribute is passed as <code>false</code> or <code>true</code>, an <code>InvalidInputException</code> is thrown.</p>"""
    has_databases: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>When <code>true</code>, the response only includes catalogs that can contain databases. Some catalogs are organizational containers that hold only other catalogs, not databases. When this parameter is set to <code>true</code>, those container-only catalogs are excluded, and only catalogs capable of containing databases are returned. Defaults to <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCatalogsRequest) -> dict:
    out: dict = {}
    if "parent_catalog_id" in value:
        out["ParentCatalogId"] = value["parent_catalog_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "recursive" in value:
        out["Recursive"] = value["recursive"]
    if "include_root" in value:
        out["IncludeRoot"] = value["include_root"]
    if "has_databases" in value:
        out["HasDatabases"] = value["has_databases"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCatalogsRequest:
    out: GetCatalogsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParentCatalogId") is not None:
        out["parent_catalog_id"] = data["ParentCatalogId"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Recursive") is not None:
        out["recursive"] = data["Recursive"]
    if data.get("IncludeRoot") is not None:
        out["include_root"] = data["IncludeRoot"]
    if data.get("HasDatabases") is not None:
        out["has_databases"] = data["HasDatabases"]
    return out
