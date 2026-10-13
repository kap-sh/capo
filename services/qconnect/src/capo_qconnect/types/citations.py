"""Generated from Smithy shape ``com.amazonaws.qconnect#Citations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.citation

Citations: TypeAlias = list["capo_qconnect.types.citation.Citation"]


# --- restJson1 ser/de ---
def serialize_json(value: Citations) -> list:
    import capo_qconnect.types.citation

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.citation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Citations:
    import capo_qconnect.types.citation

    out: Citations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.citation.deserialize_json(item))
    return out


def redact_sensitive(value: Citations) -> list[Any]:
    import capo_qconnect.types.citation

    return [capo_qconnect.types.citation.redact_sensitive(item) for item in value]
