"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateRepositoryDescriptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.repository_description
    import capo_codecommit.types.repository_name


class UpdateRepositoryDescriptionInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository to set or change the comment or description for.</p>"""
    repository_description: NotRequired[
        "capo_codecommit.types.repository_description.RepositoryDescription"
    ]
    """<p>The new comment or description for the specified repository. Repository descriptions are limited to 1,000 characters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRepositoryDescriptionInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "repository_description" in value:
        out["repositoryDescription"] = value["repository_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRepositoryDescriptionInput:
    out: UpdateRepositoryDescriptionInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("repositoryDescription") is not None:
        out["repository_description"] = data["repositoryDescription"]
    return out
