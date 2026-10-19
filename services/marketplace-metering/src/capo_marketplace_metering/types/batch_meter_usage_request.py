"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#BatchMeterUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_metering.types.product_code
    import capo_marketplace_metering.types.usage_record_list


class BatchMeterUsageRequest(TypedDict, closed=True):
    usage_records: "capo_marketplace_metering.types.usage_record_list.UsageRecordList"
    """<p>The set of <code>UsageRecords</code> to submit. <code>BatchMeterUsage</code> accepts up to 25 <code>UsageRecords</code> at a time.</p>"""
    product_code: NotRequired[
        "capo_marketplace_metering.types.product_code.ProductCode"
    ]
    """<p>Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.</p> <important> <p> <code>ProductCode</code> is required only for legacy integrations that use <code>CustomerIdentifier</code>. For new integrations using <code>LicenseArn</code> (Concurrent Agreements), do NOT include <code>ProductCode</code> at the request level. The <code>LicenseArn</code> in each <code>UsageRecord</code> identifies both the product and the specific agreement.</p> <p>Sending metering records with both <code>ProductCode</code> and <code>LicenseArn</code> for the same customer within the same hour will result in duplicate billing. If you are migrating from product-based metering to license-based metering, stop sending <code>ProductCode</code> before you start sending <code>LicenseArn</code>.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchMeterUsageRequest) -> dict:
    out: dict = {}
    import capo_marketplace_metering.types.usage_record_list

    out["UsageRecords"] = (
        capo_marketplace_metering.types.usage_record_list.serialize_aws_json_1_1(
            value["usage_records"]
        )
    )
    if "product_code" in value:
        out["ProductCode"] = value["product_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchMeterUsageRequest:
    out: BatchMeterUsageRequest = {}  # type: ignore[typeddict-item]
    if data.get("UsageRecords") is not None:
        import capo_marketplace_metering.types.usage_record_list

        out["usage_records"] = (
            capo_marketplace_metering.types.usage_record_list.deserialize_aws_json_1_1(
                data["UsageRecords"]
            )
        )
    else:
        out["usage_records"] = []
    if data.get("ProductCode") is not None:
        out["product_code"] = data["ProductCode"]
    return out
