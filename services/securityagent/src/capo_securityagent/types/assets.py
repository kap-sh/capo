"""Generated from Smithy shape ``com.amazonaws.securityagent#Assets``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.actor_list
    import capo_securityagent.types.document_list
    import capo_securityagent.types.endpoint_list
    import capo_securityagent.types.integrated_repository_list
    import capo_securityagent.types.source_code_repository_list
    import capo_securityagent.types.trusted_ca_certificate_list


class Assets(TypedDict, closed=True):
    endpoints: NotRequired["capo_securityagent.types.endpoint_list.EndpointList"]
    """<p>The list of endpoints to test during the pentest.</p>"""
    actors: NotRequired["capo_securityagent.types.actor_list.ActorList"]
    """<p>The list of actors used during penetration testing.</p>"""
    documents: NotRequired["capo_securityagent.types.document_list.DocumentList"]
    """<p>The list of documents that provide context for the pentest.</p>"""
    source_code: NotRequired[
        "capo_securityagent.types.source_code_repository_list.SourceCodeRepositoryList"
    ]
    """<p>The list of source code repositories to analyze during the pentest.</p>"""
    integrated_repositories: NotRequired[
        "capo_securityagent.types.integrated_repository_list.IntegratedRepositoryList"
    ]
    """<p>The list of integrated repositories associated with the pentest.</p>"""
    trusted_ca_certificates: NotRequired[
        "capo_securityagent.types.trusted_ca_certificate_list.TrustedCaCertificateList"
    ]
    """<p>The trust anchors used to validate target endpoint TLS certificates. Provide these for endpoints served by a private or internal certificate authority (CA), an intermediate CA, or a self-signed certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Assets) -> dict:
    out: dict = {}
    if "endpoints" in value:
        import capo_securityagent.types.endpoint_list

        out["endpoints"] = capo_securityagent.types.endpoint_list.serialize_json(
            value["endpoints"]
        )
    if "actors" in value:
        import capo_securityagent.types.actor_list

        out["actors"] = capo_securityagent.types.actor_list.serialize_json(
            value["actors"]
        )
    if "documents" in value:
        import capo_securityagent.types.document_list

        out["documents"] = capo_securityagent.types.document_list.serialize_json(
            value["documents"]
        )
    if "source_code" in value:
        import capo_securityagent.types.source_code_repository_list

        out["sourceCode"] = (
            capo_securityagent.types.source_code_repository_list.serialize_json(
                value["source_code"]
            )
        )
    if "integrated_repositories" in value:
        import capo_securityagent.types.integrated_repository_list

        out["integratedRepositories"] = (
            capo_securityagent.types.integrated_repository_list.serialize_json(
                value["integrated_repositories"]
            )
        )
    if "trusted_ca_certificates" in value:
        import capo_securityagent.types.trusted_ca_certificate_list

        out["trustedCaCertificates"] = (
            capo_securityagent.types.trusted_ca_certificate_list.serialize_json(
                value["trusted_ca_certificates"]
            )
        )
    return out


def deserialize_json(data: dict) -> Assets:
    out: Assets = {}  # type: ignore[typeddict-item]
    if data.get("endpoints") is not None:
        import capo_securityagent.types.endpoint_list

        out["endpoints"] = capo_securityagent.types.endpoint_list.deserialize_json(
            data["endpoints"]
        )
    if data.get("actors") is not None:
        import capo_securityagent.types.actor_list

        out["actors"] = capo_securityagent.types.actor_list.deserialize_json(
            data["actors"]
        )
    if data.get("documents") is not None:
        import capo_securityagent.types.document_list

        out["documents"] = capo_securityagent.types.document_list.deserialize_json(
            data["documents"]
        )
    if data.get("sourceCode") is not None:
        import capo_securityagent.types.source_code_repository_list

        out["source_code"] = (
            capo_securityagent.types.source_code_repository_list.deserialize_json(
                data["sourceCode"]
            )
        )
    if data.get("integratedRepositories") is not None:
        import capo_securityagent.types.integrated_repository_list

        out["integrated_repositories"] = (
            capo_securityagent.types.integrated_repository_list.deserialize_json(
                data["integratedRepositories"]
            )
        )
    if data.get("trustedCaCertificates") is not None:
        import capo_securityagent.types.trusted_ca_certificate_list

        out["trusted_ca_certificates"] = (
            capo_securityagent.types.trusted_ca_certificate_list.deserialize_json(
                data["trustedCaCertificates"]
            )
        )
    return out


def redact_sensitive(value: Assets) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "actors" in value:
        import capo_securityagent.types.actor_list

        out["actors"] = capo_securityagent.types.actor_list.redact_sensitive(
            value["actors"]
        )
    if "trusted_ca_certificates" in value:
        import capo_securityagent.types.trusted_ca_certificate_list

        out["trusted_ca_certificates"] = (
            capo_securityagent.types.trusted_ca_certificate_list.redact_sensitive(
                value["trusted_ca_certificates"]
            )
        )
    return out
