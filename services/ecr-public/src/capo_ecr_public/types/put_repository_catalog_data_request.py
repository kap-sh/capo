"""Generated from Smithy shape ``com.amazonaws.ecrpublic#PutRepositoryCatalogDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr_public.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr_public.types.registry_id
    import capo_ecr_public.types.repository_catalog_data_input
    import capo_ecr_public.types.repository_name


class PutRepositoryCatalogDataRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr_public.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID that's associated with the public registry the repository is in. If you do not specify a registry, the default public registry is assumed.</p>"""
    repository_name: "capo_ecr_public.types.repository_name.RepositoryName"
    """<p>The name of the repository to create or update the catalog data for.</p>"""
    catalog_data: (
        "capo_ecr_public.types.repository_catalog_data_input.RepositoryCatalogDataInput"
    )
    """<p>An object containing the catalog data for a repository. This data is publicly visible in the Amazon ECR Public Gallery.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRepositoryCatalogDataRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    import capo_ecr_public.types.repository_catalog_data_input

    out["catalogData"] = (
        capo_ecr_public.types.repository_catalog_data_input.serialize_aws_json_1_1(
            value["catalog_data"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRepositoryCatalogDataRequest:
    out: PutRepositoryCatalogDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("catalogData") is not None:
        import capo_ecr_public.types.repository_catalog_data_input

        out["catalog_data"] = (
            capo_ecr_public.types.repository_catalog_data_input.deserialize_aws_json_1_1(
                data["catalogData"]
            )
        )
    else:
        raise DeserializationError(
            "PutRepositoryCatalogDataRequest.catalog_data required"
        )
    return out
