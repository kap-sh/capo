"""Generated from Smithy shape ``com.amazonaws.codebuild#ListProjectsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.project_names
    import capo_codebuild.types.string


class ListProjectsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call.</p>"""
    projects: NotRequired["capo_codebuild.types.project_names.ProjectNames"]
    """<p>The list of build project names, with each build project name representing a single build project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProjectsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "projects" in value:
        import capo_codebuild.types.project_names

        out["projects"] = capo_codebuild.types.project_names.serialize_aws_json_1_1(
            value["projects"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProjectsOutput:
    out: ListProjectsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("projects") is not None:
        import capo_codebuild.types.project_names

        out["projects"] = capo_codebuild.types.project_names.deserialize_aws_json_1_1(
            data["projects"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListProjectsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "projects" in value:
        import capo_codebuild.types.project_names

        out["projects"] = capo_codebuild.types.project_names.serialize_cbor(
            value["projects"]
        )
    return out


def deserialize_cbor(data: dict) -> ListProjectsOutput:
    out: ListProjectsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("projects") is not None:
        import capo_codebuild.types.project_names

        out["projects"] = capo_codebuild.types.project_names.deserialize_cbor(
            data["projects"]
        )
    return out
