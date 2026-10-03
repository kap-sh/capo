"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#MeterUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_metering.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_metering.types.boolean
    import capo_marketplace_metering.types.client_token
    import capo_marketplace_metering.types.product_code
    import capo_marketplace_metering.types.timestamp
    import capo_marketplace_metering.types.usage_allocations
    import capo_marketplace_metering.types.usage_dimension
    import capo_marketplace_metering.types.usage_quantity


class MeterUsageRequest(TypedDict, closed=True):
    product_code: "capo_marketplace_metering.types.product_code.ProductCode"
    """<p>Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.</p>"""
    timestamp: "capo_marketplace_metering.types.timestamp.Timestamp"
    """<p>Timestamp, in UTC, for which the usage is being reported. Your application can meter usage for up to six hours in the past. Make sure the <code>timestamp</code> value is not before the start of the software usage.</p>"""
    usage_dimension: "capo_marketplace_metering.types.usage_dimension.UsageDimension"
    """<p>It will be one of the fcp dimension name provided during the publishing of the product.</p>"""
    usage_quantity: NotRequired[
        "capo_marketplace_metering.types.usage_quantity.UsageQuantity"
    ]
    """<p>Consumption value for the hour. Defaults to <code>0</code> if not specified.</p>"""
    dry_run: NotRequired["capo_marketplace_metering.types.boolean.Boolean"]
    """<p>Checks whether you have the permissions required for the action, but does not make the request. If you have the permissions, the request returns <code>DryRunOperation</code>; otherwise, it returns <code>UnauthorizedException</code>. Defaults to <code>false</code> if not specified.</p>"""
    usage_allocations: NotRequired[
        "capo_marketplace_metering.types.usage_allocations.UsageAllocations"
    ]
    """<p>The set of <code>UsageAllocations</code> to submit.</p> <p>The sum of all <code>UsageAllocation</code> quantities must equal the <code>UsageQuantity</code> of the <code>MeterUsage</code> request, and each <code>UsageAllocation</code> must have a unique set of tags (include no tags).</p>"""
    client_token: NotRequired[
        "capo_marketplace_metering.types.client_token.ClientToken"
    ]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotencyConflictException</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MeterUsageRequest) -> dict:
    out: dict = {}
    out["ProductCode"] = value["product_code"]
    import capo_marketplace_metering.types.timestamp

    out["Timestamp"] = capo_marketplace_metering.types.timestamp.serialize_aws_json_1_1(
        value["timestamp"]
    )
    out["UsageDimension"] = value["usage_dimension"]
    if "usage_quantity" in value:
        out["UsageQuantity"] = value["usage_quantity"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "usage_allocations" in value:
        import capo_marketplace_metering.types.usage_allocations

        out["UsageAllocations"] = (
            capo_marketplace_metering.types.usage_allocations.serialize_aws_json_1_1(
                value["usage_allocations"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MeterUsageRequest:
    out: MeterUsageRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProductCode") is not None:
        out["product_code"] = data["ProductCode"]
    else:
        raise DeserializationError("MeterUsageRequest.product_code required")
    if data.get("Timestamp") is not None:
        import capo_marketplace_metering.types.timestamp

        out["timestamp"] = (
            capo_marketplace_metering.types.timestamp.deserialize_aws_json_1_1(
                data["Timestamp"]
            )
        )
    else:
        raise DeserializationError("MeterUsageRequest.timestamp required")
    if data.get("UsageDimension") is not None:
        out["usage_dimension"] = data["UsageDimension"]
    else:
        raise DeserializationError("MeterUsageRequest.usage_dimension required")
    if data.get("UsageQuantity") is not None:
        out["usage_quantity"] = data["UsageQuantity"]
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    if data.get("UsageAllocations") is not None:
        import capo_marketplace_metering.types.usage_allocations

        out["usage_allocations"] = (
            capo_marketplace_metering.types.usage_allocations.deserialize_aws_json_1_1(
                data["UsageAllocations"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
