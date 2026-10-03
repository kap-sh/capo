"""Generated from Smithy shape ``com.amazonaws.securityir#CaseMetadataEntry``."""

from typing_extensions import TypedDict

from capo_security_ir.errors import DeserializationError


class CaseMetadataEntry(TypedDict, closed=True):
    key: "str"
    """<p>The identifier for the metadata field. This key uniquely identifies the type of metadata being stored, such as "severity", "category", or "assignee".</p>"""
    value: "str"
    """<p>The value associated with the metadata key. This contains the actual data for the metadata field identified by the key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseMetadataEntry) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CaseMetadataEntry:
    out: CaseMetadataEntry = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("CaseMetadataEntry.key required")
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError("CaseMetadataEntry.value required")
    return out
