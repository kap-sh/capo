"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#CreateMarketplaceRevenueShareAllocationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_partnercentral_revenue_measurement.types.allocation_effective_date_string
    import capo_partnercentral_revenue_measurement.types.allocation_status
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_id
    import capo_partnercentral_revenue_measurement.types.revenue_share_percent
    import capo_partnercentral_revenue_measurement.types.revision_token


class CreateMarketplaceRevenueShareAllocationOutput(TypedDict, closed=True):
    marketplace_revenue_share_allocation_id: "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_id.MarketplaceRevenueShareAllocationId"
    """<p>The unique identifier of the newly created allocation.</p>"""
    product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId"
    """<p>The AWS Marketplace product identifier.</p>"""
    product_name: NotRequired["str"]
    """<p>The display name of the AWS Marketplace product.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the allocation.</p>"""
    effective_from: "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    """<p>The effective start date of the allocation.</p>"""
    effective_until: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    ]
    """<p>The effective end date of the allocation, or null if open-ended.</p>"""
    revenue_share_percent: "capo_partnercentral_revenue_measurement.types.revenue_share_percent.RevenueSharePercent"
    """<p>The revenue share percentage.</p>"""
    status: "capo_partnercentral_revenue_measurement.types.allocation_status.AllocationStatus"
    """<p>The status of the allocation.</p>"""
    created_date: NotRequired["datetime.datetime"]
    """<p>The date when the allocation was created.</p>"""
    last_modified_date: NotRequired["datetime.datetime"]
    """<p>The date when the allocation was last modified.</p>"""
    latest_marketplace_revenue_share_revision: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    ]
    """<p>The latest revision of the parent marketplace revenue share.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateMarketplaceRevenueShareAllocationOutput) -> dict:
    out: dict = {}
    out["MarketplaceRevenueShareAllocationId"] = value[
        "marketplace_revenue_share_allocation_id"
    ]
    out["ProductId"] = value["product_id"]
    if "product_name" in value:
        out["ProductName"] = value["product_name"]
    out["Arn"] = value["arn"]
    out["EffectiveFrom"] = value["effective_from"]
    if "effective_until" in value:
        out["EffectiveUntil"] = value["effective_until"]
    out["RevenueSharePercent"] = value["revenue_share_percent"]
    import capo_partnercentral_revenue_measurement.types.allocation_status

    out["Status"] = (
        capo_partnercentral_revenue_measurement.types.allocation_status.serialize_cbor(
            value["status"]
        )
    )
    if "created_date" in value:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["CreatedDate"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
                value["created_date"]
            )
        )
    if "last_modified_date" in value:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["LastModifiedDate"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
                value["last_modified_date"]
            )
        )
    if "latest_marketplace_revenue_share_revision" in value:
        out["LatestMarketplaceRevenueShareRevision"] = value[
            "latest_marketplace_revenue_share_revision"
        ]
    return out


def deserialize_cbor(data: dict) -> CreateMarketplaceRevenueShareAllocationOutput:
    out: CreateMarketplaceRevenueShareAllocationOutput = {}  # type: ignore[typeddict-item]
    if data.get("MarketplaceRevenueShareAllocationId") is not None:
        out["marketplace_revenue_share_allocation_id"] = data[
            "MarketplaceRevenueShareAllocationId"
        ]
    else:
        out["marketplace_revenue_share_allocation_id"] = ""
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    else:
        out["product_id"] = ""
    if data.get("ProductName") is not None:
        out["product_name"] = data["ProductName"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("EffectiveFrom") is not None:
        out["effective_from"] = data["EffectiveFrom"]
    else:
        out["effective_from"] = ""
    if data.get("EffectiveUntil") is not None:
        out["effective_until"] = data["EffectiveUntil"]
    if data.get("RevenueSharePercent") is not None:
        out["revenue_share_percent"] = data["RevenueSharePercent"]
    else:
        out["revenue_share_percent"] = ""
    if data.get("Status") is not None:
        import capo_partnercentral_revenue_measurement.types.allocation_status

        out["status"] = (
            capo_partnercentral_revenue_measurement.types.allocation_status.deserialize_cbor(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.allocation_status.AllocationStatus",
            "",
        )
    if data.get("CreatedDate") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["created_date"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["CreatedDate"]
            )
        )
    if data.get("LastModifiedDate") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["last_modified_date"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["LastModifiedDate"]
            )
        )
    if data.get("LatestMarketplaceRevenueShareRevision") is not None:
        out["latest_marketplace_revenue_share_revision"] = data[
            "LatestMarketplaceRevenueShareRevision"
        ]
    return out
