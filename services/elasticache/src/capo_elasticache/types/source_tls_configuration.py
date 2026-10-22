"""Generated from Smithy shape ``com.amazonaws.elasticache#SourceTlsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string
    import capo_elasticache.types.tls_mode


class SourceTlsConfiguration(TypedDict, closed=True):
    source_tls_mode: NotRequired["capo_elasticache.types.tls_mode.TlsMode"]
    """<p>The TLS mode to use when connecting to the source. Valid values are <code>none</code> and <code>verify-ca</code>.</p>"""
    source_tls_certificate: NotRequired["capo_elasticache.types.string.String"]
    """<p>The TLS certificate used to verify the identity of the source during migration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SourceTlsConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_tls_mode" in value:
        import capo_elasticache.types.tls_mode

        capo_elasticache.types.tls_mode.serialize_query(
            value["source_tls_mode"], pairs, f"{key_prefix}SourceTlsMode"
        )
    if "source_tls_certificate" in value:
        pairs.append(
            (f"{key_prefix}SourceTlsCertificate", str(value["source_tls_certificate"]))
        )


def deserialize_query(el: Element) -> SourceTlsConfiguration:
    out: SourceTlsConfiguration = {}  # type: ignore[typeddict-item]
    child_source_tls_mode = el.find("SourceTlsMode")
    if child_source_tls_mode is not None:
        import capo_elasticache.types.tls_mode

        out["source_tls_mode"] = capo_elasticache.types.tls_mode.deserialize_query(
            child_source_tls_mode
        )
    child_source_tls_certificate = el.find("SourceTlsCertificate")
    if child_source_tls_certificate is not None:
        out["source_tls_certificate"] = str(child_source_tls_certificate.text or "")
    return out
