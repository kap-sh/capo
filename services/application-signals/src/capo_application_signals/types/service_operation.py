"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.metric_references
    import capo_application_signals.types.operation_name


class ServiceOperation(TypedDict, closed=True):
    name: "capo_application_signals.types.operation_name.OperationName"
    """<p>The name of the operation, discovered by Application Signals.</p>"""
    metric_references: (
        "capo_application_signals.types.metric_references.MetricReferences"
    )
    """<p>An array of structures that each contain information about one metric associated with this service operation that was discovered by Application Signals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceOperation) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_application_signals.types.metric_references

    out["MetricReferences"] = (
        capo_application_signals.types.metric_references.serialize_json(
            value["metric_references"]
        )
    )
    return out


def deserialize_json(data: dict) -> ServiceOperation:
    out: ServiceOperation = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("MetricReferences") is not None:
        import capo_application_signals.types.metric_references

        out["metric_references"] = (
            capo_application_signals.types.metric_references.deserialize_json(
                data["MetricReferences"]
            )
        )
    else:
        out["metric_references"] = []
    return out
