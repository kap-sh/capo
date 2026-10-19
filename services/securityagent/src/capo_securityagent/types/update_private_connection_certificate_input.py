"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdatePrivateConnectionCertificateInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.certificate_chain
    import capo_securityagent.types.private_connection_name


class UpdatePrivateConnectionCertificateInput(TypedDict, closed=True):
    private_connection_name: (
        "capo_securityagent.types.private_connection_name.PrivateConnectionName"
    )
    """<p>The name of the private connection to update.</p>"""
    certificate: "capo_securityagent.types.certificate_chain.CertificateChain"
    """<p>The PEM-encoded certificate chain for the private connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePrivateConnectionCertificateInput) -> dict:
    out: dict = {}
    out["privateConnectionName"] = value["private_connection_name"]
    out["certificate"] = value["certificate"]
    return out


def deserialize_json(data: dict) -> UpdatePrivateConnectionCertificateInput:
    out: UpdatePrivateConnectionCertificateInput = {}  # type: ignore[typeddict-item]
    if data.get("privateConnectionName") is not None:
        out["private_connection_name"] = data["privateConnectionName"]
    else:
        out["private_connection_name"] = ""
    if data.get("certificate") is not None:
        out["certificate"] = data["certificate"]
    else:
        out["certificate"] = ""
    return out


def redact_sensitive(value: UpdatePrivateConnectionCertificateInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "certificate" in value:
        out["certificate"] = "*** Sensitive Data Redacted ***"
    return out
