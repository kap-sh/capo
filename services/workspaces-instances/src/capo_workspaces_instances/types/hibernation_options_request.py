"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#HibernationOptionsRequest``."""

from typing_extensions import NotRequired, TypedDict


class HibernationOptionsRequest(TypedDict, closed=True):
    configured: NotRequired["bool"]
    """<p>Enables or disables instance hibernation capability.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HibernationOptionsRequest) -> dict:
    out: dict = {}
    if "configured" in value:
        out["Configured"] = value["configured"]
    return out


def deserialize_aws_json_1_0(data: dict) -> HibernationOptionsRequest:
    out: HibernationOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Configured") is not None:
        out["configured"] = data["Configured"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HibernationOptionsRequest) -> dict:
    out: dict = {}
    if "configured" in value:
        out["Configured"] = value["configured"]
    return out


def deserialize_cbor(data: dict) -> HibernationOptionsRequest:
    out: HibernationOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Configured") is not None:
        out["configured"] = data["Configured"]
    return out
