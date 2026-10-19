"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_id


class DomainUnitSummary(TypedDict, closed=True):
    name: "str"
    """<p>The name of the domain unit summary.</p>"""
    id: "capo_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the domain unit summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DomainUnitSummary:
    out: DomainUnitSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
