"""Generated from Smithy shape ``com.amazonaws.securityagent#GitLabRepositoryMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.access_type
    import capo_securityagent.types.git_lab_namespace
    import capo_securityagent.types.provider_resource_id
    import capo_securityagent.types.provider_resource_name


class GitLabRepositoryMetadata(TypedDict, closed=True):
    name: "capo_securityagent.types.provider_resource_name.ProviderResourceName"
    provider_resource_id: (
        "capo_securityagent.types.provider_resource_id.ProviderResourceId"
    )
    namespace: "capo_securityagent.types.git_lab_namespace.GitLabNamespace"
    """<p>The namespace (group or user path) that owns the project.</p>"""
    access_type: NotRequired["capo_securityagent.types.access_type.AccessType"]


# --- restJson1 ser/de ---
def serialize_json(value: GitLabRepositoryMetadata) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["providerResourceId"] = value["provider_resource_id"]
    out["namespace"] = value["namespace"]
    if "access_type" in value:
        import capo_securityagent.types.access_type

        out["accessType"] = capo_securityagent.types.access_type.serialize_json(
            value["access_type"]
        )
    return out


def deserialize_json(data: dict) -> GitLabRepositoryMetadata:
    out: GitLabRepositoryMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("providerResourceId") is not None:
        out["provider_resource_id"] = data["providerResourceId"]
    else:
        out["provider_resource_id"] = ""
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        out["namespace"] = ""
    if data.get("accessType") is not None:
        import capo_securityagent.types.access_type

        out["access_type"] = capo_securityagent.types.access_type.deserialize_json(
            data["accessType"]
        )
    return out
