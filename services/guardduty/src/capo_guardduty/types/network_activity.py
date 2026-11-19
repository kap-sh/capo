"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkActivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.dns_context
    import capo_guardduty.types.enrichment
    import capo_guardduty.types.network_anomaly
    import capo_guardduty.types.network_counts
    import capo_guardduty.types.network_ports
    import capo_guardduty.types.network_traffic
    import capo_guardduty.types.string


class NetworkActivity(TypedDict, closed=True):
    protocol: NotRequired["capo_guardduty.types.string.String"]
    """<p>The network protocol of the activity.</p>"""
    direction: NotRequired["capo_guardduty.types.string.String"]
    """<p>The direction of the network connection, such as inbound or outbound.</p>"""
    method: NotRequired["capo_guardduty.types.string.String"]
    """<p>The method that the network activity used.</p>"""
    blocked: NotRequired["capo_guardduty.types.string.String"]
    """<p>Indicates whether the network connection was blocked.</p>"""
    platform: NotRequired["capo_guardduty.types.string.String"]
    """<p>The platform on which the network activity was observed.</p>"""
    ports: NotRequired["capo_guardduty.types.network_ports.NetworkPorts"]
    """<p>The ports that the network activity involved.</p>"""
    traffic: NotRequired["capo_guardduty.types.network_traffic.NetworkTraffic"]
    """<p>The amount of data that the network activity transferred.</p>"""
    anomaly: NotRequired["capo_guardduty.types.network_anomaly.NetworkAnomaly"]
    """<p>Details about how the network activity deviates from normal behavior.</p>"""
    dns: NotRequired["capo_guardduty.types.dns_context.DnsContext"]
    """<p>DNS details about the network activity.</p>"""
    counts: NotRequired["capo_guardduty.types.network_counts.NetworkCounts"]
    """<p>Counts that describe the network activity, such as the number of requests or connection attempts.</p>"""
    enrichment: NotRequired["capo_guardduty.types.enrichment.Enrichment"]
    """<p>Additional context about the network activity, such as geolocation and threat intelligence information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkActivity) -> dict:
    out: dict = {}
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "direction" in value:
        out["direction"] = value["direction"]
    if "method" in value:
        out["method"] = value["method"]
    if "blocked" in value:
        out["blocked"] = value["blocked"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "ports" in value:
        import capo_guardduty.types.network_ports

        out["ports"] = capo_guardduty.types.network_ports.serialize_json(value["ports"])
    if "traffic" in value:
        import capo_guardduty.types.network_traffic

        out["traffic"] = capo_guardduty.types.network_traffic.serialize_json(
            value["traffic"]
        )
    if "anomaly" in value:
        import capo_guardduty.types.network_anomaly

        out["anomaly"] = capo_guardduty.types.network_anomaly.serialize_json(
            value["anomaly"]
        )
    if "dns" in value:
        import capo_guardduty.types.dns_context

        out["dns"] = capo_guardduty.types.dns_context.serialize_json(value["dns"])
    if "counts" in value:
        import capo_guardduty.types.network_counts

        out["counts"] = capo_guardduty.types.network_counts.serialize_json(
            value["counts"]
        )
    if "enrichment" in value:
        import capo_guardduty.types.enrichment

        out["enrichment"] = capo_guardduty.types.enrichment.serialize_json(
            value["enrichment"]
        )
    return out


def deserialize_json(data: dict) -> NetworkActivity:
    out: NetworkActivity = {}  # type: ignore[typeddict-item]
    if data.get("protocol") is not None:
        out["protocol"] = data["protocol"]
    if data.get("direction") is not None:
        out["direction"] = data["direction"]
    if data.get("method") is not None:
        out["method"] = data["method"]
    if data.get("blocked") is not None:
        out["blocked"] = data["blocked"]
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("ports") is not None:
        import capo_guardduty.types.network_ports

        out["ports"] = capo_guardduty.types.network_ports.deserialize_json(
            data["ports"]
        )
    if data.get("traffic") is not None:
        import capo_guardduty.types.network_traffic

        out["traffic"] = capo_guardduty.types.network_traffic.deserialize_json(
            data["traffic"]
        )
    if data.get("anomaly") is not None:
        import capo_guardduty.types.network_anomaly

        out["anomaly"] = capo_guardduty.types.network_anomaly.deserialize_json(
            data["anomaly"]
        )
    if data.get("dns") is not None:
        import capo_guardduty.types.dns_context

        out["dns"] = capo_guardduty.types.dns_context.deserialize_json(data["dns"])
    if data.get("counts") is not None:
        import capo_guardduty.types.network_counts

        out["counts"] = capo_guardduty.types.network_counts.deserialize_json(
            data["counts"]
        )
    if data.get("enrichment") is not None:
        import capo_guardduty.types.enrichment

        out["enrichment"] = capo_guardduty.types.enrichment.deserialize_json(
            data["enrichment"]
        )
    return out
