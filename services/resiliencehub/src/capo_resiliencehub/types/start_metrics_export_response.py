"""Generated from Smithy shape ``com.amazonaws.resiliencehub#StartMetricsExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.metrics_export_status_type
    import capo_resiliencehub.types.string255


class StartMetricsExportResponse(TypedDict, closed=True):
    metrics_export_id: "capo_resiliencehub.types.string255.String255"
    """<p>Identifier of the metrics export task.</p>"""
    status: (
        "capo_resiliencehub.types.metrics_export_status_type.MetricsExportStatusType"
    )
    """<p>Indicates the status of the metrics export task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMetricsExportResponse) -> dict:
    out: dict = {}
    out["metricsExportId"] = value["metrics_export_id"]
    import capo_resiliencehub.types.metrics_export_status_type

    out["status"] = capo_resiliencehub.types.metrics_export_status_type.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> StartMetricsExportResponse:
    out: StartMetricsExportResponse = {}  # type: ignore[typeddict-item]
    if data.get("metricsExportId") is not None:
        out["metrics_export_id"] = data["metricsExportId"]
    else:
        out["metrics_export_id"] = ""
    if data.get("status") is not None:
        import capo_resiliencehub.types.metrics_export_status_type

        out["status"] = (
            capo_resiliencehub.types.metrics_export_status_type.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_resiliencehub.types.metrics_export_status_type.MetricsExportStatusType",
            "",
        )
    return out
