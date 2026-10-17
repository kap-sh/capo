"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Metadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.log_metadata_list
    import capo_cloudwatchomni.types.metric_metadata_list
    import capo_cloudwatchomni.types.node_semantics
    import capo_cloudwatchomni.types.trace_metadata_list


class Metadata(TypedDict, closed=True):
    metrics: NotRequired[
        "capo_cloudwatchomni.types.metric_metadata_list.MetricMetadataList"
    ]
    """The metrics observed on the element."""
    semantics: NotRequired["capo_cloudwatchomni.types.node_semantics.NodeSemantics"]
    """Semantic description of the node. Absent on an edge, because semantics describe a service rather than a relationship."""
    logs: NotRequired["capo_cloudwatchomni.types.log_metadata_list.LogMetadataList"]
    """Per-signal LOGS query selectors: a LIST of blocks the console ORs, each an AND of exact store column -> raw values. Node-level (edges carry only traces). Populated when the request sets includeMetadata; derived labels (logSourceType) are added by the service projection, not stored here."""
    traces: NotRequired[
        "capo_cloudwatchomni.types.trace_metadata_list.TraceMetadataList"
    ]
    """Per-signal TRACES query selectors (same block shape as logs). Present on both node and edge metadata. serviceName is derived at the service projection, not stored here."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Metadata) -> dict:
    out: dict = {}
    if "metrics" in value:
        import capo_cloudwatchomni.types.metric_metadata_list

        out["metrics"] = capo_cloudwatchomni.types.metric_metadata_list.serialize_cbor(
            value["metrics"]
        )
    if "semantics" in value:
        import capo_cloudwatchomni.types.node_semantics

        out["semantics"] = capo_cloudwatchomni.types.node_semantics.serialize_cbor(
            value["semantics"]
        )
    if "logs" in value:
        import capo_cloudwatchomni.types.log_metadata_list

        out["logs"] = capo_cloudwatchomni.types.log_metadata_list.serialize_cbor(
            value["logs"]
        )
    if "traces" in value:
        import capo_cloudwatchomni.types.trace_metadata_list

        out["traces"] = capo_cloudwatchomni.types.trace_metadata_list.serialize_cbor(
            value["traces"]
        )
    return out


def deserialize_cbor(data: dict) -> Metadata:
    out: Metadata = {}  # type: ignore[typeddict-item]
    if data.get("metrics") is not None:
        import capo_cloudwatchomni.types.metric_metadata_list

        out["metrics"] = (
            capo_cloudwatchomni.types.metric_metadata_list.deserialize_cbor(
                data["metrics"]
            )
        )
    if data.get("semantics") is not None:
        import capo_cloudwatchomni.types.node_semantics

        out["semantics"] = capo_cloudwatchomni.types.node_semantics.deserialize_cbor(
            data["semantics"]
        )
    if data.get("logs") is not None:
        import capo_cloudwatchomni.types.log_metadata_list

        out["logs"] = capo_cloudwatchomni.types.log_metadata_list.deserialize_cbor(
            data["logs"]
        )
    if data.get("traces") is not None:
        import capo_cloudwatchomni.types.trace_metadata_list

        out["traces"] = capo_cloudwatchomni.types.trace_metadata_list.deserialize_cbor(
            data["traces"]
        )
    return out
