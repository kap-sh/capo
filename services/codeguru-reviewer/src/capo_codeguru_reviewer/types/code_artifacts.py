"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#CodeArtifacts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeguru_reviewer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.build_artifacts_object_key
    import capo_codeguru_reviewer.types.source_code_artifacts_object_key


class CodeArtifacts(TypedDict, closed=True):
    source_code_artifacts_object_key: "capo_codeguru_reviewer.types.source_code_artifacts_object_key.SourceCodeArtifactsObjectKey"
    """<p>The S3 object key for a source code .zip file. This is required for all code reviews.</p>"""
    build_artifacts_object_key: NotRequired[
        "capo_codeguru_reviewer.types.build_artifacts_object_key.BuildArtifactsObjectKey"
    ]
    """<p>The S3 object key for a build artifacts .zip file that contains .jar or .class files. This is required for a code review with security analysis. For more information, see <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/working-with-cicd.html">Create code reviews with GitHub Actions</a> in the <i>Amazon CodeGuru Reviewer User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeArtifacts) -> dict:
    out: dict = {}
    out["SourceCodeArtifactsObjectKey"] = value["source_code_artifacts_object_key"]
    if "build_artifacts_object_key" in value:
        out["BuildArtifactsObjectKey"] = value["build_artifacts_object_key"]
    return out


def deserialize_json(data: dict) -> CodeArtifacts:
    out: CodeArtifacts = {}  # type: ignore[typeddict-item]
    if data.get("SourceCodeArtifactsObjectKey") is not None:
        out["source_code_artifacts_object_key"] = data["SourceCodeArtifactsObjectKey"]
    else:
        raise DeserializationError(
            "CodeArtifacts.source_code_artifacts_object_key required"
        )
    if data.get("BuildArtifactsObjectKey") is not None:
        out["build_artifacts_object_key"] = data["BuildArtifactsObjectKey"]
    return out
