"""Generated from Smithy shape ``com.amazonaws.rum#BatchDeleteRumMetricDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.batch_delete_rum_metric_definitions_errors
    import capo_rum.types.metric_definition_ids


class BatchDeleteRumMetricDefinitionsResponse(TypedDict, closed=True):
    errors: "capo_rum.types.batch_delete_rum_metric_definitions_errors.BatchDeleteRumMetricDefinitionsErrors"
    """<p>An array of error objects, if the operation caused any errors.</p>"""
    metric_definition_ids: NotRequired[
        "capo_rum.types.metric_definition_ids.MetricDefinitionIds"
    ]
    """<p>The IDs of the metric definitions that were deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteRumMetricDefinitionsResponse) -> dict:
    out: dict = {}
    import capo_rum.types.batch_delete_rum_metric_definitions_errors

    out["Errors"] = (
        capo_rum.types.batch_delete_rum_metric_definitions_errors.serialize_json(
            value["errors"]
        )
    )
    if "metric_definition_ids" in value:
        import capo_rum.types.metric_definition_ids

        out["MetricDefinitionIds"] = (
            capo_rum.types.metric_definition_ids.serialize_json(
                value["metric_definition_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteRumMetricDefinitionsResponse:
    out: BatchDeleteRumMetricDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Errors") is not None:
        import capo_rum.types.batch_delete_rum_metric_definitions_errors

        out["errors"] = (
            capo_rum.types.batch_delete_rum_metric_definitions_errors.deserialize_json(
                data["Errors"]
            )
        )
    else:
        out["errors"] = []
    if data.get("MetricDefinitionIds") is not None:
        import capo_rum.types.metric_definition_ids

        out["metric_definition_ids"] = (
            capo_rum.types.metric_definition_ids.deserialize_json(
                data["MetricDefinitionIds"]
            )
        )
    return out
