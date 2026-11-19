"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyAccountResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.message


class ModifyAccountResult(TypedDict, closed=True):
    message: NotRequired["capo_workspaces.types.message.Message"]
    """<p>The text message to describe the status of BYOL modification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyAccountResult) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyAccountResult:
    out: ModifyAccountResult = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModifyAccountResult) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> ModifyAccountResult:
    out: ModifyAccountResult = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
