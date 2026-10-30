"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#DatumList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.datum

DatumList: TypeAlias = list["capo_sagemakertrainingsessionruntime.types.datum.Datum"]


# --- restJson1 ser/de ---
def serialize_json(value: DatumList) -> list:
    import capo_sagemakertrainingsessionruntime.types.datum

    out: list = []
    for item in value:
        out.append(
            capo_sagemakertrainingsessionruntime.types.datum.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DatumList:
    import capo_sagemakertrainingsessionruntime.types.datum

    out: DatumList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemakertrainingsessionruntime.types.datum.deserialize_json(item)
        )
    return out


def redact_sensitive(value: DatumList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
