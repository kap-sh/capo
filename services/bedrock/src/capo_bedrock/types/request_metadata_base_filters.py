"""Generated from Smithy shape ``com.amazonaws.bedrock#RequestMetadataBaseFilters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.request_metadata_map


class RequestMetadataBaseFilters(TypedDict, closed=True):
    equals: NotRequired["capo_bedrock.types.request_metadata_map.RequestMetadataMap"]
    """<p>Include results where the key equals the value.</p>"""
    not_equals: NotRequired[
        "capo_bedrock.types.request_metadata_map.RequestMetadataMap"
    ]
    """<p>Include results where the key does not equal the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestMetadataBaseFilters) -> dict:
    out: dict = {}
    if "equals" in value:
        import capo_bedrock.types.request_metadata_map

        out["equals"] = capo_bedrock.types.request_metadata_map.serialize_json(
            value["equals"]
        )
    if "not_equals" in value:
        import capo_bedrock.types.request_metadata_map

        out["notEquals"] = capo_bedrock.types.request_metadata_map.serialize_json(
            value["not_equals"]
        )
    return out


def deserialize_json(data: dict) -> RequestMetadataBaseFilters:
    out: RequestMetadataBaseFilters = {}  # type: ignore[typeddict-item]
    if data.get("equals") is not None:
        import capo_bedrock.types.request_metadata_map

        out["equals"] = capo_bedrock.types.request_metadata_map.deserialize_json(
            data["equals"]
        )
    if data.get("notEquals") is not None:
        import capo_bedrock.types.request_metadata_map

        out["not_equals"] = capo_bedrock.types.request_metadata_map.deserialize_json(
            data["notEquals"]
        )
    return out


def redact_sensitive(value: RequestMetadataBaseFilters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "equals" in value:
        out["equals"] = "*** Sensitive Data Redacted ***"
    if "not_equals" in value:
        out["not_equals"] = "*** Sensitive Data Redacted ***"
    return out
