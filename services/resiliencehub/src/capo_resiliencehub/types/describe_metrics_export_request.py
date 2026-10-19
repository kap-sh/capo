"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeMetricsExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.string255


class DescribeMetricsExportRequest(TypedDict, closed=True):
    metrics_export_id: "capo_resiliencehub.types.string255.String255"
    """<p>Identifier of the metrics export task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMetricsExportRequest) -> dict:
    out: dict = {}
    out["metricsExportId"] = value["metrics_export_id"]
    return out


def deserialize_json(data: dict) -> DescribeMetricsExportRequest:
    out: DescribeMetricsExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("metricsExportId") is not None:
        out["metrics_export_id"] = data["metricsExportId"]
    else:
        out["metrics_export_id"] = ""
    return out
