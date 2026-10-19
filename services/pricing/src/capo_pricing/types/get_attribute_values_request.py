"""Generated from Smithy shape ``com.amazonaws.pricing#GetAttributeValuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pricing.types.get_attribute_values_max_results
    import capo_pricing.types.string


class GetAttributeValuesRequest(TypedDict, closed=True):
    service_code: "capo_pricing.types.string.String"
    """<p>The service code for the service whose attributes you want to retrieve. For example, if you want the retrieve an EC2 attribute, use <code>AmazonEC2</code>.</p>"""
    attribute_name: "capo_pricing.types.string.String"
    """<p>The name of the attribute that you want to retrieve the values for, such as <code>volumeType</code>.</p>"""
    next_token: NotRequired["capo_pricing.types.string.String"]
    """<p>The pagination token that indicates the next set of results that you want to retrieve.</p>"""
    max_results: NotRequired[
        "capo_pricing.types.get_attribute_values_max_results.GetAttributeValuesMaxResults"
    ]
    """<p>The maximum number of results to return in response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAttributeValuesRequest) -> dict:
    out: dict = {}
    out["ServiceCode"] = value["service_code"]
    out["AttributeName"] = value["attribute_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAttributeValuesRequest:
    out: GetAttributeValuesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        out["service_code"] = ""
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
