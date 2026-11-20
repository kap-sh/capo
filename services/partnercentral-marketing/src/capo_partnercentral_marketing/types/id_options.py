"""Generated from Smithy shape ``aws.iam#IdOptions``."""

from typing_extensions import NotRequired, TypedDict


class IdOptions(TypedDict, closed=True):
    friendly_name: NotRequired["bool"]
    """Indicates whether the resource bound with the identifier allows friendly name ID."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdOptions) -> dict:
    out: dict = {}
    if "friendly_name" in value:
        out["friendlyName"] = value["friendly_name"]
    return out


def deserialize_cbor(data: dict) -> IdOptions:
    out: IdOptions = {}  # type: ignore[typeddict-item]
    if data.get("friendlyName") is not None:
        out["friendly_name"] = data["friendlyName"]
    return out
