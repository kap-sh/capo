"""Generated from Smithy shape ``com.amazonaws.devopsagent#SelfManagedInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.certificate_string
    import capo_devops_agent.types.resource_configuration_arn


class SelfManagedInput(TypedDict, closed=True):
    resource_configuration_id: (
        "capo_devops_agent.types.resource_configuration_arn.ResourceConfigurationArn"
    )
    """<p>The ID or ARN of the resource configuration.</p>"""
    certificate: NotRequired[
        "capo_devops_agent.types.certificate_string.CertificateString"
    ]
    """<p>Certificate for the Private Connection.</p>"""


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
