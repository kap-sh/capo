"""Generated from Smithy shape ``com.amazonaws.codebuild#DebugSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.wrapper_boolean


class DebugSession(TypedDict, closed=True):
    session_enabled: NotRequired["capo_codebuild.types.wrapper_boolean.WrapperBoolean"]
    """<p>Specifies if session debugging is enabled for this build.</p>"""
    session_target: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>Contains the identifier of the Session Manager session used for the build. To work with the paused build, you open this session to examine, control, and resume the build.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DebugSession) -> dict:
    out: dict = {}
    if "session_enabled" in value:
        out["sessionEnabled"] = value["session_enabled"]
    if "session_target" in value:
        out["sessionTarget"] = value["session_target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DebugSession:
    out: DebugSession = {}  # type: ignore[typeddict-item]
    if data.get("sessionEnabled") is not None:
        out["session_enabled"] = data["sessionEnabled"]
    if data.get("sessionTarget") is not None:
        out["session_target"] = data["sessionTarget"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DebugSession) -> dict:
    out: dict = {}
    if "session_enabled" in value:
        out["sessionEnabled"] = value["session_enabled"]
    if "session_target" in value:
        out["sessionTarget"] = value["session_target"]
    return out


def deserialize_cbor(data: dict) -> DebugSession:
    out: DebugSession = {}  # type: ignore[typeddict-item]
    if data.get("sessionEnabled") is not None:
        out["session_enabled"] = data["sessionEnabled"]
    if data.get("sessionTarget") is not None:
        out["session_target"] = data["sessionTarget"]
    return out
