"""Generated from Smithy shape ``com.amazonaws.securityagent#SelfManagedInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.certificate_chain
    import capo_securityagent.types.resource_configuration_id


class SelfManagedInput(TypedDict, closed=True):
    resource_configuration_id: (
        "capo_securityagent.types.resource_configuration_id.ResourceConfigurationId"
    )
    """<p>The identifier or ARN of the resource configuration.</p>"""
    certificate: NotRequired[
        "capo_securityagent.types.certificate_chain.CertificateChain"
    ]
    """<p>The certificate for the private connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedInput) -> dict:
    out: dict = {}
    out["resourceConfigurationId"] = value["resource_configuration_id"]
    if "certificate" in value:
        out["certificate"] = value["certificate"]
    return out


def deserialize_json(data: dict) -> SelfManagedInput:
    out: SelfManagedInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceConfigurationId") is not None:
        out["resource_configuration_id"] = data["resourceConfigurationId"]
    else:
        out["resource_configuration_id"] = ""
    if data.get("certificate") is not None:
        out["certificate"] = data["certificate"]
    return out


def redact_sensitive(value: SelfManagedInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "certificate" in value:
        out["certificate"] = "*** Sensitive Data Redacted ***"
    return out
