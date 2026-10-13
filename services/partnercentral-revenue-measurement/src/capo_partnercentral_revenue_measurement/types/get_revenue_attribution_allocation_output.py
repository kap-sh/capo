"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#GetRevenueAttributionAllocationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_revenue_measurement.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_partnercentral_revenue_measurement.types.allocation_effective_date_string
    import capo_partnercentral_revenue_measurement.types.allocation_status
    import capo_partnercentral_revenue_measurement.types.customer_aws_account_id
    import capo_partnercentral_revenue_measurement.types.entity_identifier
    import capo_partnercentral_revenue_measurement.types.entity_type
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_id
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier
    import capo_partnercentral_revenue_measurement.types.revenue_share_percent
    import capo_partnercentral_revenue_measurement.types.revision_token


class GetRevenueAttributionAllocationOutput(TypedDict, closed=True):
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
    created_date: "datetime.datetime"
    """<p>When the allocation was first created.</p>"""
    last_modified_date: "datetime.datetime"
    """<p>When the allocation was last modified.</p>"""
    revenue_attribution_revision: (
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    )
    """<p>The revision of this allocation version.</p>"""
    revenue_attribution_latest_revision: (
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    )
    """<p>The latest committed revision.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetRevenueAttributionAllocationOutput) -> dict:
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
    import capo_partnercentral_revenue_measurement.types._prelude.timestamp

    out["CreatedDate"] = (
        capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
            value["created_date"]
        )
    )
    import capo_partnercentral_revenue_measurement.types._prelude.timestamp

    out["LastModifiedDate"] = (
        capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
            value["last_modified_date"]
        )
    )
    out["RevenueAttributionRevision"] = value["revenue_attribution_revision"]
    out["RevenueAttributionLatestRevision"] = value[
        "revenue_attribution_latest_revision"
    ]
    return out


def deserialize_cbor(data: dict) -> GetRevenueAttributionAllocationOutput:
    out: GetRevenueAttributionAllocationOutput = {}  # type: ignore[typeddict-item]
    if data.get("RevenueAttributionAllocationId") is not None:
        out["revenue_attribution_allocation_id"] = data[
            "RevenueAttributionAllocationId"
        ]
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationOutput.revenue_attribution_allocation_id required"
        )
    if data.get("RevenueAttributionIdentifier") is not None:
        out["revenue_attribution_identifier"] = data["RevenueAttributionIdentifier"]
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationOutput.revenue_attribution_identifier required"
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
            "GetRevenueAttributionAllocationOutput.entity_type required"
        )
    if data.get("EntityIdentifier") is not None:
        out["entity_identifier"] = data["EntityIdentifier"]
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationOutput.entity_identifier required"
        )
    if data.get("EntityName") is not None:
        out["entity_name"] = data["EntityName"]
    if data.get("CustomerAwsAccountId") is not None:
        out["customer_aws_account_id"] = data["CustomerAwsAccountId"]
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationOutput.customer_aws_account_id required"
        )
    if data.get("RevenueSharePercent") is not None:
        out["revenue_share_percent"] = data["RevenueSharePercent"]
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationOutput.revenue_share_percent required"
        )
    if data.get("EffectiveFrom") is not None:
        out["effective_from"] = data["EffectiveFrom"]
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationOutput.effective_from required"
        )
    if data.get("EffectiveUntil") is not None:
        out["effective_until"] = data["EffectiveUntil"]
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationOutput.effective_until required"
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
            "GetRevenueAttributionAllocationOutput.status required"
        )
    if data.get("CreatedDate") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["created_date"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["CreatedDate"]
            )
        )
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationOutput.created_date required"
        )
    if data.get("LastModifiedDate") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["last_modified_date"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["LastModifiedDate"]
            )
        )
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationOutput.last_modified_date required"
        )
    if data.get("RevenueAttributionRevision") is not None:
        out["revenue_attribution_revision"] = data["RevenueAttributionRevision"]
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationOutput.revenue_attribution_revision required"
        )
    if data.get("RevenueAttributionLatestRevision") is not None:
        out["revenue_attribution_latest_revision"] = data[
            "RevenueAttributionLatestRevision"
        ]
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationOutput.revenue_attribution_latest_revision required"
        )
    return out


def redact_sensitive(value: GetRevenueAttributionAllocationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer_aws_account_id" in value:
        out["customer_aws_account_id"] = "*** Sensitive Data Redacted ***"
    return out
