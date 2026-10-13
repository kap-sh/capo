"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#RevenueAttributionAllocationSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_revenue_measurement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.allocation_effective_date_string
    import capo_partnercentral_revenue_measurement.types.allocation_status
    import capo_partnercentral_revenue_measurement.types.customer_aws_account_id
    import capo_partnercentral_revenue_measurement.types.entity_identifier
    import capo_partnercentral_revenue_measurement.types.entity_type
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_id
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier
    import capo_partnercentral_revenue_measurement.types.revenue_share_percent


class RevenueAttributionAllocationSummary(TypedDict, closed=True):
    revenue_attribution_allocation_id: "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_id.RevenueAttributionAllocationId"
    """<p>Unique allocation identifier.</p>"""
    revenue_attribution_identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier"
    """<p>The revenue attribution identifier.</p>"""
    entity_type: "capo_partnercentral_revenue_measurement.types.entity_type.EntityType"
    """<p>The type of the associated deal entity.</p>"""
    entity_identifier: "capo_partnercentral_revenue_measurement.types.entity_identifier.EntityIdentifier"
    """<p>The unique identifier of the associated deal entity.</p>"""
    entity_name: NotRequired["str"]
    """<p>The display name of the associated deal entity.</p>"""
    customer_aws_account_id: "capo_partnercentral_revenue_measurement.types.customer_aws_account_id.CustomerAwsAccountId"
    """<p>The customer AWS account ID for this associated deal entity.</p>"""
    revenue_share_percent: "capo_partnercentral_revenue_measurement.types.revenue_share_percent.RevenueSharePercent"
    """<p>Revenue share percentage.</p>"""
    effective_from: "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    """<p>First day of the effective month.</p>"""
    effective_until: "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    """<p>Last day of the effective month.</p>"""
    status: "capo_partnercentral_revenue_measurement.types.allocation_status.AllocationStatus"
    """<p>Current allocation status.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevenueAttributionAllocationSummary) -> dict:
    out: dict = {}
    out["RevenueAttributionAllocationId"] = value["revenue_attribution_allocation_id"]
    out["RevenueAttributionIdentifier"] = value["revenue_attribution_identifier"]
    import capo_partnercentral_revenue_measurement.types.entity_type

    out["EntityType"] = (
        capo_partnercentral_revenue_measurement.types.entity_type.serialize_cbor(
            value["entity_type"]
        )
    )
    out["EntityIdentifier"] = value["entity_identifier"]
    if "entity_name" in value:
        out["EntityName"] = value["entity_name"]
    out["CustomerAwsAccountId"] = value["customer_aws_account_id"]
    out["RevenueSharePercent"] = value["revenue_share_percent"]
    out["EffectiveFrom"] = value["effective_from"]
    out["EffectiveUntil"] = value["effective_until"]
    import capo_partnercentral_revenue_measurement.types.allocation_status

    out["Status"] = (
        capo_partnercentral_revenue_measurement.types.allocation_status.serialize_cbor(
            value["status"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> RevenueAttributionAllocationSummary:
    out: RevenueAttributionAllocationSummary = {}  # type: ignore[typeddict-item]
    if data.get("RevenueAttributionAllocationId") is not None:
        out["revenue_attribution_allocation_id"] = data[
            "RevenueAttributionAllocationId"
        ]
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationSummary.revenue_attribution_allocation_id required"
        )
    if data.get("RevenueAttributionIdentifier") is not None:
        out["revenue_attribution_identifier"] = data["RevenueAttributionIdentifier"]
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationSummary.revenue_attribution_identifier required"
        )
    if data.get("EntityType") is not None:
        import capo_partnercentral_revenue_measurement.types.entity_type

        out["entity_type"] = (
            capo_partnercentral_revenue_measurement.types.entity_type.deserialize_cbor(
                data["EntityType"]
            )
        )
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationSummary.entity_type required"
        )
    if data.get("EntityIdentifier") is not None:
        out["entity_identifier"] = data["EntityIdentifier"]
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationSummary.entity_identifier required"
        )
    if data.get("EntityName") is not None:
        out["entity_name"] = data["EntityName"]
    if data.get("CustomerAwsAccountId") is not None:
        out["customer_aws_account_id"] = data["CustomerAwsAccountId"]
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationSummary.customer_aws_account_id required"
        )
    if data.get("RevenueSharePercent") is not None:
        out["revenue_share_percent"] = data["RevenueSharePercent"]
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationSummary.revenue_share_percent required"
        )
    if data.get("EffectiveFrom") is not None:
        out["effective_from"] = data["EffectiveFrom"]
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationSummary.effective_from required"
        )
    if data.get("EffectiveUntil") is not None:
        out["effective_until"] = data["EffectiveUntil"]
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationSummary.effective_until required"
        )
    if data.get("Status") is not None:
        import capo_partnercentral_revenue_measurement.types.allocation_status

        out["status"] = (
            capo_partnercentral_revenue_measurement.types.allocation_status.deserialize_cbor(
                data["Status"]
            )
        )
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationSummary.status required"
        )
    return out


def redact_sensitive(value: RevenueAttributionAllocationSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer_aws_account_id" in value:
        out["customer_aws_account_id"] = "*** Sensitive Data Redacted ***"
    return out
