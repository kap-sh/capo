"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#TagResourceResponse``."""

from typing_extensions import TypedDict


class TagResourceResponse(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagResourceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> TagResourceResponse:
    out: TagResourceResponse = {}  # type: ignore[typeddict-item]
    return out
