"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetBuildsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.build_ids
    import capo_codebuild.types.builds


class BatchGetBuildsOutput(TypedDict, closed=True):
    builds: NotRequired["capo_codebuild.types.builds.Builds"]
    """<p>Information about the requested builds.</p>"""
    builds_not_found: NotRequired["capo_codebuild.types.build_ids.BuildIds"]
    """<p>The IDs of builds for which information could not be found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetBuildsOutput) -> dict:
    out: dict = {}
    if "builds" in value:
        import capo_codebuild.types.builds

        out["builds"] = capo_codebuild.types.builds.serialize_aws_json_1_1(
            value["builds"]
        )
    if "builds_not_found" in value:
        import capo_codebuild.types.build_ids

        out["buildsNotFound"] = capo_codebuild.types.build_ids.serialize_aws_json_1_1(
            value["builds_not_found"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetBuildsOutput:
    out: BatchGetBuildsOutput = {}  # type: ignore[typeddict-item]
    if data.get("builds") is not None:
        import capo_codebuild.types.builds

        out["builds"] = capo_codebuild.types.builds.deserialize_aws_json_1_1(
            data["builds"]
        )
    if data.get("buildsNotFound") is not None:
        import capo_codebuild.types.build_ids

        out["builds_not_found"] = (
            capo_codebuild.types.build_ids.deserialize_aws_json_1_1(
                data["buildsNotFound"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetBuildsOutput) -> dict:
    out: dict = {}
    if "builds" in value:
        import capo_codebuild.types.builds

        out["builds"] = capo_codebuild.types.builds.serialize_cbor(value["builds"])
    if "builds_not_found" in value:
        import capo_codebuild.types.build_ids

        out["buildsNotFound"] = capo_codebuild.types.build_ids.serialize_cbor(
            value["builds_not_found"]
        )
    return out


def deserialize_cbor(data: dict) -> BatchGetBuildsOutput:
    out: BatchGetBuildsOutput = {}  # type: ignore[typeddict-item]
    if data.get("builds") is not None:
        import capo_codebuild.types.builds

        out["builds"] = capo_codebuild.types.builds.deserialize_cbor(data["builds"])
    if data.get("buildsNotFound") is not None:
        import capo_codebuild.types.build_ids

        out["builds_not_found"] = capo_codebuild.types.build_ids.deserialize_cbor(
            data["buildsNotFound"]
        )
    return out
