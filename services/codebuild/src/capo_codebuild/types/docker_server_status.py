"""Generated from Smithy shape ``com.amazonaws.codebuild#DockerServerStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.string


class DockerServerStatus(TypedDict, closed=True):
    status: NotRequired["capo_codebuild.types.string.String"]
    """<p>The status of the docker server.</p>"""
    message: NotRequired["capo_codebuild.types.string.String"]
    """<p>A message associated with the status of a docker server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DockerServerStatus) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DockerServerStatus:
    out: DockerServerStatus = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DockerServerStatus) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> DockerServerStatus:
    out: DockerServerStatus = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
