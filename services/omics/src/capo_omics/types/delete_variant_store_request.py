"""Generated from Smithy shape ``com.amazonaws.omics#DeleteVariantStoreRequest``."""

from typing_extensions import NotRequired, TypedDict


class DeleteVariantStoreRequest(TypedDict, closed=True):
    name: "str"
    """<p>The store's name.</p>"""
    force: NotRequired["bool"]
    """<p>Whether to force deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVariantStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVariantStoreRequest:
    out: DeleteVariantStoreRequest = {}  # type: ignore[typeddict-item]
    return out
