"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CentralizationRuleSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.regions
    import capo_observabilityadmin.types.source_context_graph_configuration
    import capo_observabilityadmin.types.source_filter_string
    import capo_observabilityadmin.types.source_logs_configuration
    import capo_observabilityadmin.types.source_metrics_configuration


class CentralizationRuleSource(TypedDict, closed=True):
    regions: "capo_observabilityadmin.types.regions.Regions"
    """<p>The list of source regions from which telemetry data should be centralized.</p>"""
    scope: NotRequired[
        "capo_observabilityadmin.types.source_filter_string.SourceFilterString"
    ]
    """<p>The organizational scope from which telemetry data should be centralized, specified using organization id, accounts or organizational unit ids.</p>"""
    source_logs_configuration: NotRequired[
        "capo_observabilityadmin.types.source_logs_configuration.SourceLogsConfiguration"
    ]
    """<p>Log specific configuration for centralization source log groups.</p>"""
    source_metrics_configuration: NotRequired[
        "capo_observabilityadmin.types.source_metrics_configuration.SourceMetricsConfiguration"
    ]
    """<p>Metric specific configuration for centralization source metrics.</p>"""
    source_context_graph_configuration: NotRequired[
        "capo_observabilityadmin.types.source_context_graph_configuration.SourceContextGraphConfiguration"
    ]
    """<p>Configuration that enables centralization of the context graph for the selected sources. Including this configuration in a rule's source opts the rule into centralizing the context graph for the selected sources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CentralizationRuleSource) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.regions

    out["Regions"] = capo_observabilityadmin.types.regions.serialize_json(
        value["regions"]
    )
    if "scope" in value:
        out["Scope"] = value["scope"]
    if "source_logs_configuration" in value:
        import capo_observabilityadmin.types.source_logs_configuration

        out["SourceLogsConfiguration"] = (
            capo_observabilityadmin.types.source_logs_configuration.serialize_json(
                value["source_logs_configuration"]
            )
        )
    if "source_metrics_configuration" in value:
        import capo_observabilityadmin.types.source_metrics_configuration

        out["SourceMetricsConfiguration"] = (
            capo_observabilityadmin.types.source_metrics_configuration.serialize_json(
                value["source_metrics_configuration"]
            )
        )
    if "source_context_graph_configuration" in value:
        import capo_observabilityadmin.types.source_context_graph_configuration

        out["SourceContextGraphConfiguration"] = (
            capo_observabilityadmin.types.source_context_graph_configuration.serialize_json(
                value["source_context_graph_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CentralizationRuleSource:
    out: CentralizationRuleSource = {}  # type: ignore[typeddict-item]
    if data.get("Regions") is not None:
        import capo_observabilityadmin.types.regions

        out["regions"] = capo_observabilityadmin.types.regions.deserialize_json(
            data["Regions"]
        )
    else:
        out["regions"] = []
    if data.get("Scope") is not None:
        out["scope"] = data["Scope"]
    if data.get("SourceLogsConfiguration") is not None:
        import capo_observabilityadmin.types.source_logs_configuration

        out["source_logs_configuration"] = (
            capo_observabilityadmin.types.source_logs_configuration.deserialize_json(
                data["SourceLogsConfiguration"]
            )
        )
    if data.get("SourceMetricsConfiguration") is not None:
        import capo_observabilityadmin.types.source_metrics_configuration

        out["source_metrics_configuration"] = (
            capo_observabilityadmin.types.source_metrics_configuration.deserialize_json(
                data["SourceMetricsConfiguration"]
            )
        )
    if data.get("SourceContextGraphConfiguration") is not None:
        import capo_observabilityadmin.types.source_context_graph_configuration

        out["source_context_graph_configuration"] = (
            capo_observabilityadmin.types.source_context_graph_configuration.deserialize_json(
                data["SourceContextGraphConfiguration"]
            )
        )
    return out
