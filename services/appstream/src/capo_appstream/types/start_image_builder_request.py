"""Generated from Smithy shape ``com.amazonaws.appstream#StartImageBuilderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.appstream_agent_version
    import capo_appstream.types.string


class StartImageBuilderRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the image builder.</p>"""
    appstream_agent_version: NotRequired[
        "capo_appstream.types.appstream_agent_version.AppstreamAgentVersion"
    ]
    """<p>The version of the WorkSpaces Applications agent to use for this image builder. To use the latest version of the WorkSpaces Applications agent, specify [LATEST]. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImageBuilderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "appstream_agent_version" in value:
        out["AppstreamAgentVersion"] = value["appstream_agent_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImageBuilderRequest:
    out: StartImageBuilderRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AppstreamAgentVersion") is not None:
        out["appstream_agent_version"] = data["AppstreamAgentVersion"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartImageBuilderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "appstream_agent_version" in value:
        out["AppstreamAgentVersion"] = value["appstream_agent_version"]
    return out


def deserialize_cbor(data: dict) -> StartImageBuilderRequest:
    out: StartImageBuilderRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AppstreamAgentVersion") is not None:
        out["appstream_agent_version"] = data["AppstreamAgentVersion"]
    return out
