"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteBuildInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.build_id_or_arn


class DeleteBuildInput(TypedDict, closed=True):
    build_id: NotRequired["capo_gamelift.types.build_id_or_arn.BuildIdOrArn"]
    """<p>A unique identifier for the build to delete. You can use either the build ID or ARN value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBuildInput) -> dict:
    out: dict = {}
    if "build_id" in value:
        out["BuildId"] = value["build_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBuildInput:
    out: DeleteBuildInput = {}  # type: ignore[typeddict-item]
    if data.get("BuildId") is not None:
        out["build_id"] = data["BuildId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteBuildInput) -> dict:
    out: dict = {}
    if "build_id" in value:
        out["BuildId"] = value["build_id"]
    return out


def deserialize_cbor(data: dict) -> DeleteBuildInput:
    out: DeleteBuildInput = {}  # type: ignore[typeddict-item]
    if data.get("BuildId") is not None:
        out["build_id"] = data["BuildId"]
    return out
