"""Generated from Smithy shape ``com.amazonaws.codebuild#UpdateProjectOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.project


class UpdateProjectOutput(TypedDict, closed=True):
    project: NotRequired["capo_codebuild.types.project.Project"]
    """<p>Information about the build project that was changed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProjectOutput) -> dict:
    out: dict = {}
    if "project" in value:
        import capo_codebuild.types.project

        out["project"] = capo_codebuild.types.project.serialize_aws_json_1_1(
            value["project"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProjectOutput:
    out: UpdateProjectOutput = {}  # type: ignore[typeddict-item]
    if data.get("project") is not None:
        import capo_codebuild.types.project

        out["project"] = capo_codebuild.types.project.deserialize_aws_json_1_1(
            data["project"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateProjectOutput) -> dict:
    out: dict = {}
    if "project" in value:
        import capo_codebuild.types.project

        out["project"] = capo_codebuild.types.project.serialize_cbor(value["project"])
    return out


def deserialize_cbor(data: dict) -> UpdateProjectOutput:
    out: UpdateProjectOutput = {}  # type: ignore[typeddict-item]
    if data.get("project") is not None:
        import capo_codebuild.types.project

        out["project"] = capo_codebuild.types.project.deserialize_cbor(data["project"])
    return out
