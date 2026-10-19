"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#RevenueShareAllocation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.allocation_effective_date_string
    import capo_partnercentral_revenue_measurement.types.allocation_status
    import capo_partnercentral_revenue_measurement.types.customer_aws_account_id
    import capo_partnercentral_revenue_measurement.types.entity_identifier
    import capo_partnercentral_revenue_measurement.types.entity_type
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_id
    import capo_partnercentral_revenue_measurement.types.revenue_share_percent


class RevenueShareAllocation(TypedDict, closed=True):
    action: "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action.RevenueAttributionAllocationAction"
    """<p>The operation type: CREATE or UPDATE.</p>"""
    revenue_attribution_allocation_id: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_id.RevenueAttributionAllocationId"
    ]
    """<p>The allocation to update. Required when Action is UPDATE.</p>"""
    entity_type: "capo_partnercentral_revenue_measurement.types.entity_type.EntityType"
    """<p>The type of the associated deal entity.</p>"""
    entity_identifier: "capo_partnercentral_revenue_measurement.types.entity_identifier.EntityIdentifier"
    """<p>The unique identifier of the associated deal entity.</p>"""
    customer_aws_account_id: "capo_partnercentral_revenue_measurement.types.customer_aws_account_id.CustomerAwsAccountId"
    """<p>The customer AWS account ID for this associated deal entity.</p>"""
    revenue_share_percent: "capo_partnercentral_revenue_measurement.types.revenue_share_percent.RevenueSharePercent"
    """<p>Revenue share percentage.</p>"""
    effective_from: "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    """<p>The effective start date for this allocation.</p>"""
    effective_until: "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    """<p>The effective end date for this allocation.</p>"""
    status: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_status.AllocationStatus"
    ]
    """<p>Allocation status. Defaults to ACTIVE on CREATE.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevenueShareAllocation) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action

    out["Action"] = (
        capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action.serialize_cbor(
            value["action"]
        )
    )
    if "revenue_attribution_allocation_id" in value:
        out["RevenueAttributionAllocationId"] = value[
            "revenue_attribution_allocation_id"
        ]
    import capo_partnercentral_revenue_measurement.types.entity_type

    out["EntityType"] = (
        capo_partnercentral_revenue_measurement.types.entity_type.serialize_cbor(
            value["entity_type"]
        )
    )
    out["EntityIdentifier"] = value["entity_identifier"]
    out["CustomerAwsAccountId"] = value["customer_aws_account_id"]
    out["RevenueSharePercent"] = value["revenue_share_percent"]
    out["EffectiveFrom"] = value["effective_from"]
    out["EffectiveUntil"] = value["effective_until"]
    if "status" in value:
        import capo_partnercentral_revenue_measurement.types.allocation_status

        out["Status"] = (
            capo_partnercentral_revenue_measurement.types.allocation_status.serialize_cbor(
                value["status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RevenueShareAllocation:
    out: RevenueShareAllocation = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action

        out["action"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action.deserialize_cbor(
                data["Action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action.RevenueAttributionAllocationAction",
            "",
        )
    if data.get("RevenueAttributionAllocationId") is not None:
        out["revenue_attribution_allocation_id"] = data[
            "RevenueAttributionAllocationId"
        ]
    if data.get("EntityType") is not None:
        import capo_partnercentral_revenue_measurement.types.entity_type

        out["entity_type"] = (
            capo_partnercentral_revenue_measurement.types.entity_type.deserialize_cbor(
                data["EntityType"]
            )
        )
    else:
        import typing

        out["entity_type"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.entity_type.EntityType", ""
        )
    if data.get("EntityIdentifier") is not None:
        out["entity_identifier"] = data["EntityIdentifier"]
    else:
        out["entity_identifier"] = ""
    if data.get("CustomerAwsAccountId") is not None:
        out["customer_aws_account_id"] = data["CustomerAwsAccountId"]
    else:
        out["customer_aws_account_id"] = ""
    if data.get("RevenueSharePercent") is not None:
        out["revenue_share_percent"] = data["RevenueSharePercent"]
    else:
        out["revenue_share_percent"] = ""
    if data.get("EffectiveFrom") is not None:
        out["effective_from"] = data["EffectiveFrom"]
    else:
        out["effective_from"] = ""
    if data.get("EffectiveUntil") is not None:
        out["effective_until"] = data["EffectiveUntil"]
    else:
        out["effective_until"] = ""
    if data.get("Status") is not None:
        import capo_partnercentral_revenue_measurement.types.allocation_status

        out["status"] = (
            capo_partnercentral_revenue_measurement.types.allocation_status.deserialize_cbor(
                data["Status"]
            )
        )
    return out


def redact_sensitive(value: RevenueShareAllocation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer_aws_account_id" in value:
        out["customer_aws_account_id"] = "*** Sensitive Data Redacted ***"
    return out
