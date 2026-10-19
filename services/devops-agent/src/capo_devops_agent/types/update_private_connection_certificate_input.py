"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdatePrivateConnectionCertificateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.certificate_string
    import capo_devops_agent.types.private_connection_name


class UpdatePrivateConnectionCertificateInput(TypedDict, closed=True):
    name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
    """<p>The name of the Private Connection.</p>"""
    certificate: "capo_devops_agent.types.certificate_string.CertificateString"
    """<p>The new certificate for the Private Connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePrivateConnectionCertificateInput) -> dict:
    out: dict = {}
    out["certificate"] = value["certificate"]
    return out


def deserialize_json(data: dict) -> UpdatePrivateConnectionCertificateInput:
    out: UpdatePrivateConnectionCertificateInput = {}  # type: ignore[typeddict-item]
    if data.get("certificate") is not None:
        out["certificate"] = data["certificate"]
    else:
        out["certificate"] = ""
    return out
