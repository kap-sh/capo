"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#RevenueAttributionAllocationErrorDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_revenue_measurement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.allocation_effective_date_string
    import capo_partnercentral_revenue_measurement.types.customer_aws_account_id
    import capo_partnercentral_revenue_measurement.types.entity_identifier
    import capo_partnercentral_revenue_measurement.types.entity_type
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_code
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_id


class RevenueAttributionAllocationErrorDetail(TypedDict, closed=True):
    revenue_attribution_allocation_id: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_id.RevenueAttributionAllocationId"
    ]
    """<p>The allocation identifier. Present for UPDATE actions; absent for CREATE actions.</p>"""
    entity_type: "capo_partnercentral_revenue_measurement.types.entity_type.EntityType"
    """<p>The deal entity type of the failing record.</p>"""
    entity_id: "capo_partnercentral_revenue_measurement.types.entity_identifier.EntityIdentifier"
    """<p>The deal entity identifier of the failing record.</p>"""
    customer_aws_account_id: "capo_partnercentral_revenue_measurement.types.customer_aws_account_id.CustomerAwsAccountId"
    """<p>The customer AWS account ID of the failing record.</p>"""
    effective_from: "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    """<p>Effective start date of the failing record.</p>"""
    effective_until: "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    """<p>Effective end date of the failing record.</p>"""
    action: "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action.RevenueAttributionAllocationAction"
    """<p>The action that was attempted.</p>"""
    error_code: "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_code.RevenueAttributionAllocationErrorCode"
    """<p>Machine-readable error code.</p>"""
    error_message: "str"
    """<p>Human-readable error description.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevenueAttributionAllocationErrorDetail) -> dict:
    out: dict = {}
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
    out["EntityId"] = value["entity_id"]
    out["CustomerAwsAccountId"] = value["customer_aws_account_id"]
    out["EffectiveFrom"] = value["effective_from"]
    out["EffectiveUntil"] = value["effective_until"]
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action

    out["Action"] = (
        capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action.serialize_cbor(
            value["action"]
        )
    )
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_code

    out["ErrorCode"] = (
        capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_code.serialize_cbor(
            value["error_code"]
        )
    )
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> RevenueAttributionAllocationErrorDetail:
    out: RevenueAttributionAllocationErrorDetail = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError(
            "RevenueAttributionAllocationErrorDetail.entity_type required"
        )
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationErrorDetail.entity_id required"
        )
    if data.get("CustomerAwsAccountId") is not None:
        out["customer_aws_account_id"] = data["CustomerAwsAccountId"]
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationErrorDetail.customer_aws_account_id required"
        )
    if data.get("EffectiveFrom") is not None:
        out["effective_from"] = data["EffectiveFrom"]
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationErrorDetail.effective_from required"
        )
    if data.get("EffectiveUntil") is not None:
        out["effective_until"] = data["EffectiveUntil"]
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationErrorDetail.effective_until required"
        )
    if data.get("Action") is not None:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action

        out["action"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_action.deserialize_cbor(
                data["Action"]
            )
        )
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationErrorDetail.action required"
        )
    if data.get("ErrorCode") is not None:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_code

        out["error_code"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_code.deserialize_cbor(
                data["ErrorCode"]
            )
        )
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationErrorDetail.error_code required"
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    else:
        raise DeserializationError(
            "RevenueAttributionAllocationErrorDetail.error_message required"
        )
    return out


def redact_sensitive(value: RevenueAttributionAllocationErrorDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer_aws_account_id" in value:
        out["customer_aws_account_id"] = "*** Sensitive Data Redacted ***"
    return out
