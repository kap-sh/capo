"""Generated from Smithy shape ``com.amazonaws.pricing#ListPriceListsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pricing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pricing.types.currency_code
    import capo_pricing.types.effective_date
    import capo_pricing.types.max_results
    import capo_pricing.types.region_code
    import capo_pricing.types.service_code
    import capo_pricing.types.string


class ListPriceListsRequest(TypedDict, closed=True):
    service_code: "capo_pricing.types.service_code.ServiceCode"
    """<p>The service code or the Savings Plans service code for the attributes that you want to retrieve. For example, to get the list of applicable Amazon EC2 price lists, use <code>AmazonEC2</code>. For a full list of service codes containing On-Demand and Reserved Instance (RI) pricing, use the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_DescribeServices.html#awscostmanagement-pricing_DescribeServices-request-FormatVersion">DescribeServices</a> API.</p> <p>To retrieve the Reserved Instance and Compute Savings Plans price lists, use <code>ComputeSavingsPlans</code>. </p> <p>To retrieve Machine Learning Savings Plans price lists, use <code>MachineLearningSavingsPlans</code>. </p>"""
    effective_date: "capo_pricing.types.effective_date.EffectiveDate"
    """<p>The date that the Price List file prices are effective from. </p>"""
    region_code: NotRequired["capo_pricing.types.region_code.RegionCode"]
    """<p>This is used to filter the Price List by Amazon Web Services Region. For example, to get the price list only for the <code>US East (N. Virginia)</code> Region, use <code>us-east-1</code>. If nothing is specified, you retrieve price lists for all applicable Regions. The available <code>RegionCode</code> list can be retrieved from <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues.html">GetAttributeValues</a> API.</p>"""
    currency_code: "capo_pricing.types.currency_code.CurrencyCode"
    """<p>The three alphabetical character ISO-4217 currency code that the Price List files are denominated in. </p>"""
    next_token: NotRequired["capo_pricing.types.string.String"]
    """<p>The pagination token that indicates the next set of results that you want to retrieve. </p>"""
    max_results: NotRequired["capo_pricing.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPriceListsRequest) -> dict:
    out: dict = {}
    out["ServiceCode"] = value["service_code"]
    import capo_pricing.types.effective_date

    out["EffectiveDate"] = capo_pricing.types.effective_date.serialize_aws_json_1_1(
        value["effective_date"]
    )
    if "region_code" in value:
        out["RegionCode"] = value["region_code"]
    out["CurrencyCode"] = value["currency_code"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPriceListsRequest:
    out: ListPriceListsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError("ListPriceListsRequest.service_code required")
    if data.get("EffectiveDate") is not None:
        import capo_pricing.types.effective_date

        out["effective_date"] = (
            capo_pricing.types.effective_date.deserialize_aws_json_1_1(
                data["EffectiveDate"]
            )
        )
    else:
        raise DeserializationError("ListPriceListsRequest.effective_date required")
    if data.get("RegionCode") is not None:
        out["region_code"] = data["RegionCode"]
    if data.get("CurrencyCode") is not None:
        out["currency_code"] = data["CurrencyCode"]
    else:
        raise DeserializationError("ListPriceListsRequest.currency_code required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
