"""Generated from Smithy shape ``com.amazonaws.rum#BatchDeleteRumMetricDefinitionsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rum.types.metric_definition_id


class BatchDeleteRumMetricDefinitionsError(TypedDict, closed=True):
    metric_definition_id: "capo_rum.types.metric_definition_id.MetricDefinitionId"
    """<p>The ID of the metric definition that caused this error.</p>"""
    error_code: "str"
    """<p>The error code.</p>"""
    error_message: "str"
    """<p>The error message for this metric definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteRumMetricDefinitionsError) -> dict:
    out: dict = {}
    out["MetricDefinitionId"] = value["metric_definition_id"]
    out["ErrorCode"] = value["error_code"]
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchDeleteRumMetricDefinitionsError:
    out: BatchDeleteRumMetricDefinitionsError = {}  # type: ignore[typeddict-item]
    if data.get("MetricDefinitionId") is not None:
        out["metric_definition_id"] = data["MetricDefinitionId"]
    else:
        out["metric_definition_id"] = ""
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        out["error_code"] = ""
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    else:
        out["error_message"] = ""
    return out
