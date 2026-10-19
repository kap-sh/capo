"""Generated from Smithy shape ``com.amazonaws.ecrpublic#CreateRepositoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.repository_catalog_data_input
    import capo_ecr_public.types.repository_name
    import capo_ecr_public.types.tag_list


class CreateRepositoryRequest(TypedDict, closed=True):
    repository_name: "capo_ecr_public.types.repository_name.RepositoryName"
    """<p>The name to use for the repository. This appears publicly in the Amazon ECR Public Gallery. The repository name can be specified on its own (for example <code>nginx-web-app</code>) or prepended with a namespace to group the repository into a category (for example <code>project-a/nginx-web-app</code>).</p>"""
    catalog_data: NotRequired[
        "capo_ecr_public.types.repository_catalog_data_input.RepositoryCatalogDataInput"
    ]
    """<p>The details about the repository that are publicly visible in the Amazon ECR Public Gallery.</p>"""
    tags: NotRequired["capo_ecr_public.types.tag_list.TagList"]
    """<p>The metadata that you apply to each repository to help categorize and organize your repositories. Each tag consists of a key and an optional value. You define both of them. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRepositoryRequest) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "catalog_data" in value:
        import capo_ecr_public.types.repository_catalog_data_input

        out["catalogData"] = (
            capo_ecr_public.types.repository_catalog_data_input.serialize_aws_json_1_1(
                value["catalog_data"]
            )
        )
    if "tags" in value:
        import capo_ecr_public.types.tag_list

        out["tags"] = capo_ecr_public.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRepositoryRequest:
    out: CreateRepositoryRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("tags") is not None:
        import capo_ecr_public.types.tag_list

        out["tags"] = capo_ecr_public.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
