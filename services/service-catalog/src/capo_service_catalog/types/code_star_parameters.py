"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CodeStarParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.code_star_connection_arn
    import capo_service_catalog.types.repository
    import capo_service_catalog.types.repository_artifact_path
    import capo_service_catalog.types.repository_branch


class CodeStarParameters(TypedDict, closed=True):
    connection_arn: (
        "capo_service_catalog.types.code_star_connection_arn.CodeStarConnectionArn"
    )
    """<p>The CodeStar ARN, which is the connection between Service Catalog and the external repository.</p>"""
    repository: "capo_service_catalog.types.repository.Repository"
    """<p>The specific repository where the product’s artifact-to-be-synced resides, formatted as "Account/Repo." </p>"""
    branch: "capo_service_catalog.types.repository_branch.RepositoryBranch"
    """<p>The specific branch where the artifact resides. </p>"""
    artifact_path: (
        "capo_service_catalog.types.repository_artifact_path.RepositoryArtifactPath"
    )
    """<p>The absolute path wehre the artifact resides within the repo and branch, formatted as "folder/file.json." </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeStarParameters) -> dict:
    out: dict = {}
    out["ConnectionArn"] = value["connection_arn"]
    out["Repository"] = value["repository"]
    out["Branch"] = value["branch"]
    out["ArtifactPath"] = value["artifact_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeStarParameters:
    out: CodeStarParameters = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        raise DeserializationError("CodeStarParameters.connection_arn required")
    if data.get("Repository") is not None:
        out["repository"] = data["Repository"]
    else:
        raise DeserializationError("CodeStarParameters.repository required")
    if data.get("Branch") is not None:
        out["branch"] = data["Branch"]
    else:
        raise DeserializationError("CodeStarParameters.branch required")
    if data.get("ArtifactPath") is not None:
        out["artifact_path"] = data["ArtifactPath"]
    else:
        raise DeserializationError("CodeStarParameters.artifact_path required")
    return out
