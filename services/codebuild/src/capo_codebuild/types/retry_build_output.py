"""Generated from Smithy shape ``com.amazonaws.codebuild#RetryBuildOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.build


class RetryBuildOutput(TypedDict, closed=True):
    build: NotRequired["capo_codebuild.types.build.Build"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryBuildOutput) -> dict:
    out: dict = {}
    if "build" in value:
        import capo_codebuild.types.build

        out["build"] = capo_codebuild.types.build.serialize_aws_json_1_1(value["build"])
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryBuildOutput:
    out: RetryBuildOutput = {}  # type: ignore[typeddict-item]
    if data.get("build") is not None:
        import capo_codebuild.types.build

        out["build"] = capo_codebuild.types.build.deserialize_aws_json_1_1(
            data["build"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RetryBuildOutput) -> dict:
    out: dict = {}
    if "build" in value:
        import capo_codebuild.types.build

        out["build"] = capo_codebuild.types.build.serialize_cbor(value["build"])
    return out


def deserialize_cbor(data: dict) -> RetryBuildOutput:
    out: RetryBuildOutput = {}  # type: ignore[typeddict-item]
    if data.get("build") is not None:
        import capo_codebuild.types.build

        out["build"] = capo_codebuild.types.build.deserialize_cbor(data["build"])
    return out
