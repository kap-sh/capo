"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AnalysisTypeReportResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.collection_member_string
    import capo_network_firewall.types.domain
    import capo_network_firewall.types.first_accessed
    import capo_network_firewall.types.hits
    import capo_network_firewall.types.last_accessed
    import capo_network_firewall.types.unique_sources


class AnalysisTypeReportResult(TypedDict, closed=True):
    protocol: NotRequired[
        "capo_network_firewall.types.collection_member_string.CollectionMember_String"
    ]
    """<p>The type of traffic captured by the analysis report.</p>"""
    first_accessed: NotRequired[
        "capo_network_firewall.types.first_accessed.FirstAccessed"
    ]
    """<p>The date and time any domain was first accessed (within the last 30 day period).</p>"""
    last_accessed: NotRequired["capo_network_firewall.types.last_accessed.LastAccessed"]
    """<p>The date and time any domain was last accessed (within the last 30 day period).</p>"""
    domain: NotRequired["capo_network_firewall.types.domain.Domain"]
    """<p>The most frequently accessed domains.</p>"""
    hits: NotRequired["capo_network_firewall.types.hits.Hits"]
    """<p>The number of attempts made to access a observed domain.</p>"""
    unique_sources: NotRequired[
        "capo_network_firewall.types.unique_sources.UniqueSources"
    ]
    """<p>The number of unique source IP addresses that connected to a domain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnalysisTypeReportResult) -> dict:
    out: dict = {}
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "first_accessed" in value:
        import capo_network_firewall.types.first_accessed

        out["FirstAccessed"] = (
            capo_network_firewall.types.first_accessed.serialize_aws_json_1_0(
                value["first_accessed"]
            )
        )
    if "last_accessed" in value:
        import capo_network_firewall.types.last_accessed

        out["LastAccessed"] = (
            capo_network_firewall.types.last_accessed.serialize_aws_json_1_0(
                value["last_accessed"]
            )
        )
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "hits" in value:
        import capo_network_firewall.types.hits

        out["Hits"] = capo_network_firewall.types.hits.serialize_aws_json_1_0(
            value["hits"]
        )
    if "unique_sources" in value:
        import capo_network_firewall.types.unique_sources

        out["UniqueSources"] = (
            capo_network_firewall.types.unique_sources.serialize_aws_json_1_0(
                value["unique_sources"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AnalysisTypeReportResult:
    out: AnalysisTypeReportResult = {}  # type: ignore[typeddict-item]
    if data.get("Protocol") is not None:
        out["protocol"] = data["Protocol"]
    if data.get("FirstAccessed") is not None:
        import capo_network_firewall.types.first_accessed

        out["first_accessed"] = (
            capo_network_firewall.types.first_accessed.deserialize_aws_json_1_0(
                data["FirstAccessed"]
            )
        )
    if data.get("LastAccessed") is not None:
        import capo_network_firewall.types.last_accessed

        out["last_accessed"] = (
            capo_network_firewall.types.last_accessed.deserialize_aws_json_1_0(
                data["LastAccessed"]
            )
        )
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("Hits") is not None:
        import capo_network_firewall.types.hits

        out["hits"] = capo_network_firewall.types.hits.deserialize_aws_json_1_0(
            data["Hits"]
        )
    if data.get("UniqueSources") is not None:
        import capo_network_firewall.types.unique_sources

        out["unique_sources"] = (
            capo_network_firewall.types.unique_sources.deserialize_aws_json_1_0(
                data["UniqueSources"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnalysisTypeReportResult) -> dict:
    out: dict = {}
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "first_accessed" in value:
        import capo_network_firewall.types.first_accessed

        out["FirstAccessed"] = (
            capo_network_firewall.types.first_accessed.serialize_cbor(
                value["first_accessed"]
            )
        )
    if "last_accessed" in value:
        import capo_network_firewall.types.last_accessed

        out["LastAccessed"] = capo_network_firewall.types.last_accessed.serialize_cbor(
            value["last_accessed"]
        )
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "hits" in value:
        import capo_network_firewall.types.hits

        out["Hits"] = capo_network_firewall.types.hits.serialize_cbor(value["hits"])
    if "unique_sources" in value:
        import capo_network_firewall.types.unique_sources

        out["UniqueSources"] = (
            capo_network_firewall.types.unique_sources.serialize_cbor(
                value["unique_sources"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AnalysisTypeReportResult:
    out: AnalysisTypeReportResult = {}  # type: ignore[typeddict-item]
    if data.get("Protocol") is not None:
        out["protocol"] = data["Protocol"]
    if data.get("FirstAccessed") is not None:
        import capo_network_firewall.types.first_accessed

        out["first_accessed"] = (
            capo_network_firewall.types.first_accessed.deserialize_cbor(
                data["FirstAccessed"]
            )
        )
    if data.get("LastAccessed") is not None:
        import capo_network_firewall.types.last_accessed

        out["last_accessed"] = (
            capo_network_firewall.types.last_accessed.deserialize_cbor(
                data["LastAccessed"]
            )
        )
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("Hits") is not None:
        import capo_network_firewall.types.hits

        out["hits"] = capo_network_firewall.types.hits.deserialize_cbor(data["Hits"])
    if data.get("UniqueSources") is not None:
        import capo_network_firewall.types.unique_sources

        out["unique_sources"] = (
            capo_network_firewall.types.unique_sources.deserialize_cbor(
                data["UniqueSources"]
            )
        )
    return out
