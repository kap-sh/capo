"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#UsageRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_metering.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_metering.types.customer_aws_account_id
    import capo_marketplace_metering.types.customer_identifier
    import capo_marketplace_metering.types.license_arn
    import capo_marketplace_metering.types.timestamp
    import capo_marketplace_metering.types.usage_allocations
    import capo_marketplace_metering.types.usage_dimension
    import capo_marketplace_metering.types.usage_quantity


class UsageRecord(TypedDict, closed=True):
    timestamp: "capo_marketplace_metering.types.timestamp.Timestamp"
    """<p>Timestamp, in UTC, for which the usage is being reported.</p> <p>Your application can meter usage for up to 24 hours in the past. Make sure the <code>timestamp</code> value is not before the start of the software usage.</p> <p>At the end of each billing cycle, you have a 6-hour grace period to submit usage records for the previous billing month before 06:00 UTC on the first day of the next month.</p>"""
    customer_identifier: (
        "capo_marketplace_metering.types.customer_identifier.CustomerIdentifier"
    )
    """<p>The <code>CustomerIdentifier</code> is obtained through the <code>ResolveCustomer</code> operation and represents an individual buyer in your application.</p> <important> <p> <code>CustomerIdentifier</code> is not supported for new SaaS product integrations. Use <code>CustomerAWSAccountId</code> to identify the buyer.</p> </important>"""
    dimension: "capo_marketplace_metering.types.usage_dimension.UsageDimension"
    """<p>During the process of registering a product on Amazon Web Services Marketplace, dimensions are specified. These represent different units of value in your application.</p>"""
    quantity: NotRequired[
        "capo_marketplace_metering.types.usage_quantity.UsageQuantity"
    ]
    """<p>The quantity of usage consumed by the customer for the given dimension and time. Defaults to <code>0</code> if not specified.</p>"""
    usage_allocations: NotRequired[
        "capo_marketplace_metering.types.usage_allocations.UsageAllocations"
    ]
    """<p>The set of <code>UsageAllocations</code> to submit. The sum of all <code>UsageAllocation</code> quantities must equal the Quantity of the <code>UsageRecord</code>.</p>"""
    customer_aws_account_id: NotRequired[
        "capo_marketplace_metering.types.customer_aws_account_id.CustomerAWSAccountId"
    ]
    """<p>The <code>CustomerAWSAccountId</code> parameter specifies the AWS account ID of the buyer.</p> <important> <p>If you have an existing integration and need the <code>CustomerAWSAccountId</code> that corresponds to a <code>CustomerIdentifier</code>, contact <a href="https://aws.amazon.com/marketplace/management/contact-us/">AWS Marketplace Seller Operations</a> to obtain the mapping. Do not request the <code>CustomerAWSAccountId</code> directly from buyers. We cannot verify that a buyer-provided account ID is authentic, which can result in incorrect metering or billing.</p> </important>"""
    license_arn: NotRequired["capo_marketplace_metering.types.license_arn.LicenseArn"]
    """<p>The <code>LicenseArn</code> is a unique identifier for a specific granted license. These are used for software purchased through Amazon Web Services Marketplace.</p> <note> <p>To access your <code>CustomerAWSAccountId</code> and <code>LicenseArn</code> mapping, visit <a href="https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-agreements.html">Agreements Feeds</a>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageRecord) -> dict:
    out: dict = {}
    import capo_marketplace_metering.types.timestamp

    out["Timestamp"] = capo_marketplace_metering.types.timestamp.serialize_aws_json_1_1(
        value["timestamp"]
    )
    out["CustomerIdentifier"] = value.get("customer_identifier", "")
    out["Dimension"] = value["dimension"]
    if "quantity" in value:
        out["Quantity"] = value["quantity"]
    if "usage_allocations" in value:
        import capo_marketplace_metering.types.usage_allocations

        out["UsageAllocations"] = (
            capo_marketplace_metering.types.usage_allocations.serialize_aws_json_1_1(
                value["usage_allocations"]
            )
        )
    if "customer_aws_account_id" in value:
        out["CustomerAWSAccountId"] = value["customer_aws_account_id"]
    if "license_arn" in value:
        out["LicenseArn"] = value["license_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UsageRecord:
    out: UsageRecord = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_marketplace_metering.types.timestamp

        out["timestamp"] = (
            capo_marketplace_metering.types.timestamp.deserialize_aws_json_1_1(
                data["Timestamp"]
            )
        )
    else:
        raise DeserializationError("UsageRecord.timestamp required")
    if data.get("CustomerIdentifier") is not None:
        out["customer_identifier"] = data["CustomerIdentifier"]
    else:
        out["customer_identifier"] = ""
    if data.get("Dimension") is not None:
        out["dimension"] = data["Dimension"]
    else:
        raise DeserializationError("UsageRecord.dimension required")
    if data.get("Quantity") is not None:
        out["quantity"] = data["Quantity"]
    if data.get("UsageAllocations") is not None:
        import capo_marketplace_metering.types.usage_allocations

        out["usage_allocations"] = (
            capo_marketplace_metering.types.usage_allocations.deserialize_aws_json_1_1(
                data["UsageAllocations"]
            )
        )
    if data.get("CustomerAWSAccountId") is not None:
        out["customer_aws_account_id"] = data["CustomerAWSAccountId"]
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    return out
