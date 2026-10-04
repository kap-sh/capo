"""Generated from Smithy shape ``com.amazonaws.securityagent#AzureDevOpsRepositoryResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.azure_dev_ops_organization
    import capo_securityagent.types.provider_resource_name


class AzureDevOpsRepositoryResource(TypedDict, closed=True):
    name: "capo_securityagent.types.provider_resource_name.ProviderResourceName"
    organization: (
        "capo_securityagent.types.azure_dev_ops_organization.AzureDevOpsOrganization"
    )
    """<p>The name of the Azure DevOps organization that owns the repository.</p>"""
    project: NotRequired["str"]
    """<p>The name of the Azure DevOps project that contains the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureDevOpsRepositoryResource) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["organization"] = value["organization"]
    if "project" in value:
        out["project"] = value["project"]
    return out


def deserialize_json(data: dict) -> AzureDevOpsRepositoryResource:
    out: AzureDevOpsRepositoryResource = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AzureDevOpsRepositoryResource.name required")
    if data.get("organization") is not None:
        out["organization"] = data["organization"]
    else:
        raise DeserializationError(
            "AzureDevOpsRepositoryResource.organization required"
        )
    if data.get("project") is not None:
        out["project"] = data["project"]
    return out
