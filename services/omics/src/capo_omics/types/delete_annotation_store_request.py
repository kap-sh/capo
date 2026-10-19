"""Generated from Smithy shape ``com.amazonaws.omics#DeleteAnnotationStoreRequest``."""

from typing_extensions import NotRequired, TypedDict


class DeleteAnnotationStoreRequest(TypedDict, closed=True):
    name: "str"
    """<p>The store's name.</p>"""
    force: NotRequired["bool"]
    """<p>Whether to force deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAnnotationStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAnnotationStoreRequest:
    out: DeleteAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
    return out
