"""Generated from Smithy shape ``com.amazonaws.securityagent#BitbucketRepositoryMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.access_type
    import capo_securityagent.types.bitbucket_workspace
    import capo_securityagent.types.provider_resource_id
    import capo_securityagent.types.provider_resource_name


class BitbucketRepositoryMetadata(TypedDict, closed=True):
    name: "capo_securityagent.types.provider_resource_name.ProviderResourceName"
    provider_resource_id: (
        "capo_securityagent.types.provider_resource_id.ProviderResourceId"
    )
    workspace: "capo_securityagent.types.bitbucket_workspace.BitbucketWorkspace"
    """<p>The workspace slug that owns the repository.</p>"""
    access_type: NotRequired["capo_securityagent.types.access_type.AccessType"]


# --- restJson1 ser/de ---
def serialize_json(value: BitbucketRepositoryMetadata) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["providerResourceId"] = value["provider_resource_id"]
    out["workspace"] = value["workspace"]
    if "access_type" in value:
        import capo_securityagent.types.access_type

        out["accessType"] = capo_securityagent.types.access_type.serialize_json(
            value["access_type"]
        )
    return out


def deserialize_json(data: dict) -> BitbucketRepositoryMetadata:
    out: BitbucketRepositoryMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("providerResourceId") is not None:
        out["provider_resource_id"] = data["providerResourceId"]
    else:
        out["provider_resource_id"] = ""
    if data.get("workspace") is not None:
        out["workspace"] = data["workspace"]
    else:
        out["workspace"] = ""
    if data.get("accessType") is not None:
        import capo_securityagent.types.access_type

        out["access_type"] = capo_securityagent.types.access_type.deserialize_json(
            data["accessType"]
        )
    return out
