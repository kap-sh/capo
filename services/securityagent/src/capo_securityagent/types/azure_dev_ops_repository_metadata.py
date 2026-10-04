"""Generated from Smithy shape ``com.amazonaws.securityagent#AzureDevOpsRepositoryMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.access_type
    import capo_securityagent.types.azure_dev_ops_organization
    import capo_securityagent.types.provider_resource_id
    import capo_securityagent.types.provider_resource_name


class AzureDevOpsRepositoryMetadata(TypedDict, closed=True):
    name: "capo_securityagent.types.provider_resource_name.ProviderResourceName"
    provider_resource_id: (
        "capo_securityagent.types.provider_resource_id.ProviderResourceId"
    )
    organization: (
        "capo_securityagent.types.azure_dev_ops_organization.AzureDevOpsOrganization"
    )
    """<p>The name of the Azure DevOps organization that owns the repository.</p>"""
    project: NotRequired["str"]
    """<p>The name of the Azure DevOps project that contains the repository.</p>"""
    project_id: NotRequired["str"]
    """<p>The GUID of the Azure DevOps project that contains the repository.</p>"""
    access_type: NotRequired["capo_securityagent.types.access_type.AccessType"]


# --- restJson1 ser/de ---
def serialize_json(value: AzureDevOpsRepositoryMetadata) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["providerResourceId"] = value["provider_resource_id"]
    out["organization"] = value["organization"]
    if "project" in value:
        out["project"] = value["project"]
    if "project_id" in value:
        out["projectId"] = value["project_id"]
    if "access_type" in value:
        import capo_securityagent.types.access_type

        out["accessType"] = capo_securityagent.types.access_type.serialize_json(
            value["access_type"]
        )
    return out


def deserialize_json(data: dict) -> AzureDevOpsRepositoryMetadata:
    out: AzureDevOpsRepositoryMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AzureDevOpsRepositoryMetadata.name required")
    if data.get("providerResourceId") is not None:
        out["provider_resource_id"] = data["providerResourceId"]
    else:
        raise DeserializationError(
            "AzureDevOpsRepositoryMetadata.provider_resource_id required"
        )
    if data.get("organization") is not None:
        out["organization"] = data["organization"]
    else:
        raise DeserializationError(
            "AzureDevOpsRepositoryMetadata.organization required"
        )
    if data.get("project") is not None:
        out["project"] = data["project"]
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    if data.get("accessType") is not None:
        import capo_securityagent.types.access_type

        out["access_type"] = capo_securityagent.types.access_type.deserialize_json(
            data["accessType"]
        )
    return out
