"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AuditFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.attributes
    import capo_application_signals.types.auditor_results
    import capo_application_signals.types.dependency_graph
    import capo_application_signals.types.metric_graph


class AuditFinding(TypedDict, closed=True):
    key_attributes: "capo_application_signals.types.attributes.Attributes"
    """<p>The key attributes that identify the service or entity this audit finding relates to. This is a string-to-string map that includes fields like Type, Name, and Environment.</p>"""
    auditor_results: NotRequired[
        "capo_application_signals.types.auditor_results.AuditorResults"
    ]
    """<p>An array of auditor results that contain the specific findings, descriptions, and severity levels identified by different auditing algorithms.</p>"""
    operation: NotRequired["str"]
    """<p>The name of the operation associated with this audit finding, if the finding is specific to a particular service operation.</p>"""
    metric_graph: NotRequired["capo_application_signals.types.metric_graph.MetricGraph"]
    """<p>A structure containing metric data queries and time range information that provides context for the audit finding through relevant performance metrics.</p>"""
    dependency_graph: NotRequired[
        "capo_application_signals.types.dependency_graph.DependencyGraph"
    ]
    """<p>A structure containing nodes and edges that represent the dependency relationships relevant to this audit finding, helping to understand the context and potential impact.</p>"""
    type: NotRequired["str"]
    """<p>The type of audit finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditFinding) -> dict:
    out: dict = {}
    import capo_application_signals.types.attributes

    out["KeyAttributes"] = capo_application_signals.types.attributes.serialize_json(
        value["key_attributes"]
    )
    if "auditor_results" in value:
        import capo_application_signals.types.auditor_results

        out["AuditorResults"] = (
            capo_application_signals.types.auditor_results.serialize_json(
                value["auditor_results"]
            )
        )
    if "operation" in value:
        out["Operation"] = value["operation"]
    if "metric_graph" in value:
        import capo_application_signals.types.metric_graph

        out["MetricGraph"] = capo_application_signals.types.metric_graph.serialize_json(
            value["metric_graph"]
        )
    if "dependency_graph" in value:
        import capo_application_signals.types.dependency_graph

        out["DependencyGraph"] = (
            capo_application_signals.types.dependency_graph.serialize_json(
                value["dependency_graph"]
            )
        )
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AuditFinding:
    out: AuditFinding = {}  # type: ignore[typeddict-item]
    if data.get("KeyAttributes") is not None:
        import capo_application_signals.types.attributes

        out["key_attributes"] = (
            capo_application_signals.types.attributes.deserialize_json(
                data["KeyAttributes"]
            )
        )
    else:
        out["key_attributes"] = {}
    if data.get("AuditorResults") is not None:
        import capo_application_signals.types.auditor_results

        out["auditor_results"] = (
            capo_application_signals.types.auditor_results.deserialize_json(
                data["AuditorResults"]
            )
        )
    if data.get("Operation") is not None:
        out["operation"] = data["Operation"]
    if data.get("MetricGraph") is not None:
        import capo_application_signals.types.metric_graph

        out["metric_graph"] = (
            capo_application_signals.types.metric_graph.deserialize_json(
                data["MetricGraph"]
            )
        )
    if data.get("DependencyGraph") is not None:
        import capo_application_signals.types.dependency_graph

        out["dependency_graph"] = (
            capo_application_signals.types.dependency_graph.deserialize_json(
                data["DependencyGraph"]
            )
        )
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
