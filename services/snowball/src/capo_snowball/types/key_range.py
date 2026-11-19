"""Generated from Smithy shape ``com.amazonaws.snowball#KeyRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.string


class KeyRange(TypedDict, closed=True):
    begin_marker: NotRequired["capo_snowball.types.string.String"]
    """<p>The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.</p>"""
    end_marker: NotRequired["capo_snowball.types.string.String"]
    """<p>The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyRange) -> dict:
    out: dict = {}
    if "begin_marker" in value:
        out["BeginMarker"] = value["begin_marker"]
    if "end_marker" in value:
        out["EndMarker"] = value["end_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KeyRange:
    out: KeyRange = {}  # type: ignore[typeddict-item]
    if data.get("BeginMarker") is not None:
        out["begin_marker"] = data["BeginMarker"]
    if data.get("EndMarker") is not None:
        out["end_marker"] = data["EndMarker"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: KeyRange) -> dict:
    out: dict = {}
    if "begin_marker" in value:
        out["BeginMarker"] = value["begin_marker"]
    if "end_marker" in value:
        out["EndMarker"] = value["end_marker"]
    return out


def deserialize_cbor(data: dict) -> KeyRange:
    out: KeyRange = {}  # type: ignore[typeddict-item]
    if data.get("BeginMarker") is not None:
        out["begin_marker"] = data["BeginMarker"]
    if data.get("EndMarker") is not None:
        out["end_marker"] = data["EndMarker"]
    return out
