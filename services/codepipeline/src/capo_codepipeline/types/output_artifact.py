"""Generated from Smithy shape ``com.amazonaws.codepipeline#OutputArtifact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.artifact_name
    import capo_codepipeline.types.file_path_list


class OutputArtifact(TypedDict, closed=True):
    name: "capo_codepipeline.types.artifact_name.ArtifactName"
    """<p>The name of the output of an artifact, such as "My App".</p> <p>The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.</p> <p>Output artifact names must be unique within a pipeline.</p>"""
    files: NotRequired["capo_codepipeline.types.file_path_list.FilePathList"]
    """<p>The files that you want to associate with the output artifact that will be exported from the compute action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputArtifact) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "files" in value:
        import capo_codepipeline.types.file_path_list

        out["files"] = capo_codepipeline.types.file_path_list.serialize_aws_json_1_1(
            value["files"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputArtifact:
    out: OutputArtifact = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("OutputArtifact.name required")
    if data.get("files") is not None:
        import capo_codepipeline.types.file_path_list

        out["files"] = capo_codepipeline.types.file_path_list.deserialize_aws_json_1_1(
            data["files"]
        )
    return out
