"""Generated from Smithy shape ``com.amazonaws.pricing#GetPriceListFileUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pricing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pricing.types.file_format
    import capo_pricing.types.price_list_arn


class GetPriceListFileUrlRequest(TypedDict, closed=True):
    price_list_arn: "capo_pricing.types.price_list_arn.PriceListArn"
    """<p>The unique identifier that maps to where your Price List files are located. <code>PriceListArn</code> can be obtained from the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html">ListPriceLists</a> response. </p>"""
    file_format: "capo_pricing.types.file_format.FileFormat"
    """<p>The format that you want to retrieve your Price List files in. The <code>FileFormat</code> can be obtained from the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html">ListPriceLists</a> response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPriceListFileUrlRequest) -> dict:
    out: dict = {}
    out["PriceListArn"] = value["price_list_arn"]
    out["FileFormat"] = value["file_format"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPriceListFileUrlRequest:
    out: GetPriceListFileUrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("PriceListArn") is not None:
        out["price_list_arn"] = data["PriceListArn"]
    else:
        raise DeserializationError("GetPriceListFileUrlRequest.price_list_arn required")
    if data.get("FileFormat") is not None:
        out["file_format"] = data["FileFormat"]
    else:
        raise DeserializationError("GetPriceListFileUrlRequest.file_format required")
    return out
