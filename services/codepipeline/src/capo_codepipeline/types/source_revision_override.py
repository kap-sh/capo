"""Generated from Smithy shape ``com.amazonaws.codepipeline#SourceRevisionOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_name
    import capo_codepipeline.types.revision
    import capo_codepipeline.types.source_revision_type


class SourceRevisionOverride(TypedDict, closed=True):
    action_name: "capo_codepipeline.types.action_name.ActionName"
    """<p>The name of the action where the override will be applied.</p>"""
    revision_type: "capo_codepipeline.types.source_revision_type.SourceRevisionType"
    """<p>The type of source revision, based on the source provider. For example, the revision type for the CodeCommit action provider is the commit ID.</p>"""
    revision_value: "capo_codepipeline.types.revision.Revision"
    """<p>The source revision, or version of your source artifact, with the changes that you want to run in the pipeline execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceRevisionOverride) -> dict:
    out: dict = {}
    out["actionName"] = value["action_name"]
    import capo_codepipeline.types.source_revision_type

    out["revisionType"] = (
        capo_codepipeline.types.source_revision_type.serialize_aws_json_1_1(
            value["revision_type"]
        )
    )
    out["revisionValue"] = value["revision_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceRevisionOverride:
    out: SourceRevisionOverride = {}  # type: ignore[typeddict-item]
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    else:
        out["action_name"] = ""
    if data.get("revisionType") is not None:
        import capo_codepipeline.types.source_revision_type

        out["revision_type"] = (
            capo_codepipeline.types.source_revision_type.deserialize_aws_json_1_1(
                data["revisionType"]
            )
        )
    else:
        import typing

        out["revision_type"] = typing.cast(
            "capo_codepipeline.types.source_revision_type.SourceRevisionType", ""
        )
    if data.get("revisionValue") is not None:
        out["revision_value"] = data["revisionValue"]
    else:
        out["revision_value"] = ""
    return out
