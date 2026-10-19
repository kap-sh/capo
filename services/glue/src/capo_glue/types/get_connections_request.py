"""Generated from Smithy shape ``com.amazonaws.glue#GetConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boolean
    import capo_glue.types.catalog_id_string
    import capo_glue.types.get_connections_filter
    import capo_glue.types.page_size
    import capo_glue.types.token


class GetConnectionsRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the connections reside. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    filter: NotRequired["capo_glue.types.get_connections_filter.GetConnectionsFilter"]
    """<p>A filter that controls which connections are returned.</p>"""
    hide_password: NotRequired["capo_glue.types.boolean.Boolean"]
    """<p>Allows you to retrieve the connection metadata without returning the password. For instance, the Glue console uses this flag to retrieve the connection, and does not display the password. Set this parameter when the caller might not have permission to use the KMS key to decrypt the password, but it does have permission to access the rest of the connection properties.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of connections to return in one response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConnectionsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "filter" in value:
        import capo_glue.types.get_connections_filter

        out["Filter"] = capo_glue.types.get_connections_filter.serialize_aws_json_1_1(
            value["filter"]
        )
    if "hide_password" in value:
        out["HidePassword"] = value["hide_password"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConnectionsRequest:
    out: GetConnectionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("Filter") is not None:
        import capo_glue.types.get_connections_filter

        out["filter"] = capo_glue.types.get_connections_filter.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if data.get("HidePassword") is not None:
        out["hide_password"] = data["HidePassword"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
