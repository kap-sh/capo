"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#GetRevenueAttributionAllocationsTaskOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_revenue_measurement.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail_list
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_id
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_status
    import capo_partnercentral_revenue_measurement.types.revision_token


class GetRevenueAttributionAllocationsTaskOutput(TypedDict, closed=True):
    task_id: "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_id.RevenueAttributionAllocationTaskId"
    """<p>The unique identifier for the asynchronous task.</p>"""
    status: "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_status.RevenueAttributionAllocationTaskStatus"
    """<p>Current task status.</p>"""
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog used for this task.</p>"""
    revenue_attribution_arn: "str"
    """<p>ARN of the revenue attribution resource.</p>"""
    started_at: "datetime.datetime"
    """<p>When processing started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>When processing ended. Only present when COMPLETE or FAILED.</p>"""
    total_revenue_attribution_allocation_records: "int"
    """<p>Total revenue attribution allocation records in the batch.</p>"""
    description: NotRequired["str"]
    """<p>Human-readable description, if provided at creation.</p>"""
    revenue_attribution_latest_revision: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    ]
    """<p>The revision number assigned to this batch. Only present when COMPLETE.</p>"""
    error_detail_list: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail_list.RevenueAttributionAllocationErrorDetailList"
    ]
    """<p>All errors discovered during async processing. Only present when FAILED.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetRevenueAttributionAllocationsTaskOutput) -> dict:
    out: dict = {}
    out["TaskId"] = value["task_id"]
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_status

    out["Status"] = (
        capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_status.serialize_cbor(
            value["status"]
        )
    )
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    out["RevenueAttributionArn"] = value["revenue_attribution_arn"]
    import capo_partnercentral_revenue_measurement.types._prelude.timestamp

    out["StartedAt"] = (
        capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
            value["started_at"]
        )
    )
    if "ended_at" in value:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["EndedAt"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
                value["ended_at"]
            )
        )
    out["TotalRevenueAttributionAllocationRecords"] = value[
        "total_revenue_attribution_allocation_records"
    ]
    if "description" in value:
        out["Description"] = value["description"]
    if "revenue_attribution_latest_revision" in value:
        out["RevenueAttributionLatestRevision"] = value[
            "revenue_attribution_latest_revision"
        ]
    if "error_detail_list" in value:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail_list

        out["ErrorDetailList"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail_list.serialize_cbor(
                value["error_detail_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetRevenueAttributionAllocationsTaskOutput:
    out: GetRevenueAttributionAllocationsTaskOutput = {}  # type: ignore[typeddict-item]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationsTaskOutput.task_id required"
        )
    if data.get("Status") is not None:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_status

        out["status"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_status.deserialize_cbor(
                data["Status"]
            )
        )
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationsTaskOutput.status required"
        )
    if data.get("Catalog") is not None:
        import capo_partnercentral_revenue_measurement.types.catalog_name

        out["catalog"] = (
            capo_partnercentral_revenue_measurement.types.catalog_name.deserialize_cbor(
                data["Catalog"]
            )
        )
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationsTaskOutput.catalog required"
        )
    if data.get("RevenueAttributionArn") is not None:
        out["revenue_attribution_arn"] = data["RevenueAttributionArn"]
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationsTaskOutput.revenue_attribution_arn required"
        )
    if data.get("StartedAt") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["started_at"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["StartedAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationsTaskOutput.started_at required"
        )
    if data.get("EndedAt") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["ended_at"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["EndedAt"]
            )
        )
    if data.get("TotalRevenueAttributionAllocationRecords") is not None:
        out["total_revenue_attribution_allocation_records"] = data[
            "TotalRevenueAttributionAllocationRecords"
        ]
    else:
        raise DeserializationError(
            "GetRevenueAttributionAllocationsTaskOutput.total_revenue_attribution_allocation_records required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RevenueAttributionLatestRevision") is not None:
        out["revenue_attribution_latest_revision"] = data[
            "RevenueAttributionLatestRevision"
        ]
    if data.get("ErrorDetailList") is not None:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail_list

        out["error_detail_list"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail_list.deserialize_cbor(
                data["ErrorDetailList"]
            )
        )
    return out


def redact_sensitive(
    value: GetRevenueAttributionAllocationsTaskOutput,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "error_detail_list" in value:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail_list

        out["error_detail_list"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail_list.redact_sensitive(
                value["error_detail_list"]
            )
        )
    return out
