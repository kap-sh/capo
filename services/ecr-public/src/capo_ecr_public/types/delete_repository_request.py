"""Generated from Smithy shape ``com.amazonaws.ecrpublic#DeleteRepositoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr_public.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr_public.types.force_flag
    import capo_ecr_public.types.registry_id
    import capo_ecr_public.types.repository_name


class DeleteRepositoryRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr_public.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID that's associated with the public registry that contains the repository to delete. If you do not specify a registry, the default public registry is assumed.</p>"""
    repository_name: "capo_ecr_public.types.repository_name.RepositoryName"
    """<p>The name of the repository to delete.</p>"""
    force: NotRequired["capo_ecr_public.types.force_flag.ForceFlag"]
    """<p> The force option can be used to delete a repository that contains images. If the force option is not used, the repository must be empty prior to deletion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRepositoryRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    if "force" in value:
        out["force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRepositoryRequest:
    out: DeleteRepositoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("DeleteRepositoryRequest.repository_name required")
    if data.get("force") is not None:
        out["force"] = data["force"]
    return out
