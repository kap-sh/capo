"""Generated from Smithy shape ``com.amazonaws.codebuild#ListCuratedEnvironmentImagesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.environment_platforms


class ListCuratedEnvironmentImagesOutput(TypedDict, closed=True):
    platforms: NotRequired[
        "capo_codebuild.types.environment_platforms.EnvironmentPlatforms"
    ]
    """<p>Information about supported platforms for Docker images that are managed by CodeBuild.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCuratedEnvironmentImagesOutput) -> dict:
    out: dict = {}
    if "platforms" in value:
        import capo_codebuild.types.environment_platforms

        out["platforms"] = (
            capo_codebuild.types.environment_platforms.serialize_aws_json_1_1(
                value["platforms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCuratedEnvironmentImagesOutput:
    out: ListCuratedEnvironmentImagesOutput = {}  # type: ignore[typeddict-item]
    if data.get("platforms") is not None:
        import capo_codebuild.types.environment_platforms

        out["platforms"] = (
            capo_codebuild.types.environment_platforms.deserialize_aws_json_1_1(
                data["platforms"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListCuratedEnvironmentImagesOutput) -> dict:
    out: dict = {}
    if "platforms" in value:
        import capo_codebuild.types.environment_platforms

        out["platforms"] = capo_codebuild.types.environment_platforms.serialize_cbor(
            value["platforms"]
        )
    return out


def deserialize_cbor(data: dict) -> ListCuratedEnvironmentImagesOutput:
    out: ListCuratedEnvironmentImagesOutput = {}  # type: ignore[typeddict-item]
    if data.get("platforms") is not None:
        import capo_codebuild.types.environment_platforms

        out["platforms"] = capo_codebuild.types.environment_platforms.deserialize_cbor(
            data["platforms"]
        )
    return out
