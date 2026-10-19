"""Generated from Smithy shape ``com.amazonaws.glue#GetUserDefinedFunctionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_getter_page_size
    import capo_glue.types.catalog_id_string
    import capo_glue.types.function_type
    import capo_glue.types.name_string
    import capo_glue.types.token


class GetUserDefinedFunctionsRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the functions to be retrieved are located. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the catalog database where the functions are located. If none is provided, functions from all the databases across the catalog will be returned.</p>"""
    pattern: "capo_glue.types.name_string.NameString"
    """<p>An optional function-name pattern string that filters the function definitions returned.</p>"""
    function_type: NotRequired["capo_glue.types.function_type.FunctionType"]
    """<p>An optional function-type pattern string that filters the function definitions returned from Amazon Redshift Federated Permissions Catalog.</p> <p>Specify a value of <code>REGULAR_FUNCTION</code> or <code>STORED_PROCEDURE</code>. The <code>STORED_PROCEDURE</code> function type is only compatible with Amazon Redshift Federated Permissions Catalog. </p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""
    max_results: NotRequired[
        "capo_glue.types.catalog_getter_page_size.CatalogGetterPageSize"
    ]
    """<p>The maximum number of functions to return in one response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserDefinedFunctionsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    out["Pattern"] = value["pattern"]
    if "function_type" in value:
        import capo_glue.types.function_type

        out["FunctionType"] = capo_glue.types.function_type.serialize_aws_json_1_1(
            value["function_type"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUserDefinedFunctionsRequest:
    out: GetUserDefinedFunctionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    else:
        out["pattern"] = ""
    if data.get("FunctionType") is not None:
        import capo_glue.types.function_type

        out["function_type"] = capo_glue.types.function_type.deserialize_aws_json_1_1(
            data["FunctionType"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
