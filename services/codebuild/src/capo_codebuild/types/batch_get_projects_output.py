"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetProjectsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.project_names
    import capo_codebuild.types.projects


class BatchGetProjectsOutput(TypedDict, closed=True):
    projects: NotRequired["capo_codebuild.types.projects.Projects"]
    """<p>Information about the requested build projects.</p>"""
    projects_not_found: NotRequired["capo_codebuild.types.project_names.ProjectNames"]
    """<p>The names of build projects for which information could not be found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetProjectsOutput) -> dict:
    out: dict = {}
    if "projects" in value:
        import capo_codebuild.types.projects

        out["projects"] = capo_codebuild.types.projects.serialize_aws_json_1_1(
            value["projects"]
        )
    if "projects_not_found" in value:
        import capo_codebuild.types.project_names

        out["projectsNotFound"] = (
            capo_codebuild.types.project_names.serialize_aws_json_1_1(
                value["projects_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetProjectsOutput:
    out: BatchGetProjectsOutput = {}  # type: ignore[typeddict-item]
    if data.get("projects") is not None:
        import capo_codebuild.types.projects

        out["projects"] = capo_codebuild.types.projects.deserialize_aws_json_1_1(
            data["projects"]
        )
    if data.get("projectsNotFound") is not None:
        import capo_codebuild.types.project_names

        out["projects_not_found"] = (
            capo_codebuild.types.project_names.deserialize_aws_json_1_1(
                data["projectsNotFound"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetProjectsOutput) -> dict:
    out: dict = {}
    if "projects" in value:
        import capo_codebuild.types.projects

        out["projects"] = capo_codebuild.types.projects.serialize_cbor(
            value["projects"]
        )
    if "projects_not_found" in value:
        import capo_codebuild.types.project_names

        out["projectsNotFound"] = capo_codebuild.types.project_names.serialize_cbor(
            value["projects_not_found"]
        )
    return out


def deserialize_cbor(data: dict) -> BatchGetProjectsOutput:
    out: BatchGetProjectsOutput = {}  # type: ignore[typeddict-item]
    if data.get("projects") is not None:
        import capo_codebuild.types.projects

        out["projects"] = capo_codebuild.types.projects.deserialize_cbor(
            data["projects"]
        )
    if data.get("projectsNotFound") is not None:
        import capo_codebuild.types.project_names

        out["projects_not_found"] = capo_codebuild.types.project_names.deserialize_cbor(
            data["projectsNotFound"]
        )
    return out
