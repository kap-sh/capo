"""Generated from Smithy shape ``com.amazonaws.medialive#MulticastSourceUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class MulticastSourceUpdateRequest(TypedDict, closed=True):
    source_ip: NotRequired["capo_medialive.types.__string.__string"]
    """This represents the ip address of the device sending the multicast stream."""
    url: NotRequired["capo_medialive.types.__string.__string"]
    """This represents the customer's source URL where multicast stream is pulled from."""
    secondary_source_ip: NotRequired["capo_medialive.types.__string.__string"]
    """This represents the ip address of the device sending the secondary multicast stream."""
    secondary_url: NotRequired["capo_medialive.types.__string.__string"]
    """This represents the customer's secondary source URL where the redundant multicast stream (SMPTE 2022-7) is pulled from."""


# --- restJson1 ser/de ---
def serialize_json(value: MulticastSourceUpdateRequest) -> dict:
    out: dict = {}
    if "source_ip" in value:
        out["sourceIp"] = value["source_ip"]
    if "url" in value:
        out["url"] = value["url"]
    if "secondary_source_ip" in value:
        out["secondarySourceIp"] = value["secondary_source_ip"]
    if "secondary_url" in value:
        out["secondaryUrl"] = value["secondary_url"]
    return out


def deserialize_json(data: dict) -> MulticastSourceUpdateRequest:
    out: MulticastSourceUpdateRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceIp") is not None:
        out["source_ip"] = data["sourceIp"]
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("secondarySourceIp") is not None:
        out["secondary_source_ip"] = data["secondarySourceIp"]
    if data.get("secondaryUrl") is not None:
        out["secondary_url"] = data["secondaryUrl"]
    return out
