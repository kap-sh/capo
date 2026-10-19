"""Generated from Smithy shape ``com.amazonaws.pricing#GetProductsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pricing.types.filters
    import capo_pricing.types.format_version
    import capo_pricing.types.get_products_max_results
    import capo_pricing.types.string


class GetProductsRequest(TypedDict, closed=True):
    service_code: "capo_pricing.types.string.String"
    """<p>The code for the service whose products you want to retrieve. </p>"""
    filters: NotRequired["capo_pricing.types.filters.Filters"]
    """<p>The list of filters that limit the returned products. only products that match all filters are returned.</p>"""
    format_version: NotRequired["capo_pricing.types.format_version.FormatVersion"]
    """<p>The format version that you want the response to be in.</p> <p>Valid values are: <code>aws_v1</code> </p>"""
    next_token: NotRequired["capo_pricing.types.string.String"]
    """<p>The pagination token that indicates the next set of results that you want to retrieve.</p>"""
    max_results: NotRequired[
        "capo_pricing.types.get_products_max_results.GetProductsMaxResults"
    ]
    """<p>The maximum number of results to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProductsRequest) -> dict:
    out: dict = {}
    out["ServiceCode"] = value["service_code"]
    if "filters" in value:
        import capo_pricing.types.filters

        out["Filters"] = capo_pricing.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "format_version" in value:
        out["FormatVersion"] = value["format_version"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProductsRequest:
    out: GetProductsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        out["service_code"] = ""
    if data.get("Filters") is not None:
        import capo_pricing.types.filters

        out["filters"] = capo_pricing.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("FormatVersion") is not None:
        out["format_version"] = data["FormatVersion"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
