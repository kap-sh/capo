"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#StartRevenueAttributionAllocationsTaskOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_id
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_status


class StartRevenueAttributionAllocationsTaskOutput(TypedDict, closed=True):
    task_id: "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_id.RevenueAttributionAllocationTaskId"
    """<p>Unique identifier for the submitted task.</p>"""
    status: "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_status.RevenueAttributionAllocationTaskStatus"
    """<p>Initial task status. Always IN_PROGRESS on successful submission.</p>"""
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog used for this task.</p>"""
    revenue_attribution_arn: "str"
    """<p>ARN of the revenue attribution resource.</p>"""
    started_at: "datetime.datetime"
    """<p>When processing started.</p>"""
    total_revenue_attribution_allocation_records: "int"
    """<p>Total revenue attribution allocation records in the batch.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartRevenueAttributionAllocationsTaskOutput) -> dict:
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
    out["TotalRevenueAttributionAllocationRecords"] = value[
        "total_revenue_attribution_allocation_records"
    ]
    return out


def deserialize_cbor(data: dict) -> StartRevenueAttributionAllocationsTaskOutput:
    out: StartRevenueAttributionAllocationsTaskOutput = {}  # type: ignore[typeddict-item]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    if data.get("Status") is not None:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_status

        out["status"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_status.deserialize_cbor(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_task_status.RevenueAttributionAllocationTaskStatus",
            "",
        )
    if data.get("Catalog") is not None:
        import capo_partnercentral_revenue_measurement.types.catalog_name

        out["catalog"] = (
            capo_partnercentral_revenue_measurement.types.catalog_name.deserialize_cbor(
                data["Catalog"]
            )
        )
    else:
        import typing

        out["catalog"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName", ""
        )
    if data.get("RevenueAttributionArn") is not None:
        out["revenue_attribution_arn"] = data["RevenueAttributionArn"]
    else:
        out["revenue_attribution_arn"] = ""
    if data.get("StartedAt") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["started_at"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["StartedAt"]
            )
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("TotalRevenueAttributionAllocationRecords") is not None:
        out["total_revenue_attribution_allocation_records"] = data[
            "TotalRevenueAttributionAllocationRecords"
        ]
    else:
        out["total_revenue_attribution_allocation_records"] = 0
    return out
