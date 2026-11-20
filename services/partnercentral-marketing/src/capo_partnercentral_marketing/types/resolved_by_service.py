"""Generated from Smithy shape ``aws.iam#ResolvedByService``."""

from typing_extensions import TypedDict


class ResolvedByService(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResolvedByService) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> ResolvedByService:
    out: ResolvedByService = {}  # type: ignore[typeddict-item]
    return out
