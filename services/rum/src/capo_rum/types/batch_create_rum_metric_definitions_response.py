"""Generated from Smithy shape ``com.amazonaws.rum#BatchCreateRumMetricDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.batch_create_rum_metric_definitions_errors
    import capo_rum.types.metric_definitions


class BatchCreateRumMetricDefinitionsResponse(TypedDict, closed=True):
    errors: "capo_rum.types.batch_create_rum_metric_definitions_errors.BatchCreateRumMetricDefinitionsErrors"
    """<p>An array of error objects, if the operation caused any errors.</p>"""
    metric_definitions: NotRequired[
        "capo_rum.types.metric_definitions.MetricDefinitions"
    ]
    """<p>An array of structures that define the extended metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRumMetricDefinitionsResponse) -> dict:
    out: dict = {}
    import capo_rum.types.batch_create_rum_metric_definitions_errors

    out["Errors"] = (
        capo_rum.types.batch_create_rum_metric_definitions_errors.serialize_json(
            value["errors"]
        )
    )
    if "metric_definitions" in value:
        import capo_rum.types.metric_definitions

        out["MetricDefinitions"] = capo_rum.types.metric_definitions.serialize_json(
            value["metric_definitions"]
        )
    return out


def deserialize_json(data: dict) -> BatchCreateRumMetricDefinitionsResponse:
    out: BatchCreateRumMetricDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Errors") is not None:
        import capo_rum.types.batch_create_rum_metric_definitions_errors

        out["errors"] = (
            capo_rum.types.batch_create_rum_metric_definitions_errors.deserialize_json(
                data["Errors"]
            )
        )
    else:
        out["errors"] = []
    if data.get("MetricDefinitions") is not None:
        import capo_rum.types.metric_definitions

        out["metric_definitions"] = capo_rum.types.metric_definitions.deserialize_json(
            data["MetricDefinitions"]
        )
    return out
