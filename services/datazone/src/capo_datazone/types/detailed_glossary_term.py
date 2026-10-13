"""Generated from Smithy shape ``com.amazonaws.datazone#DetailedGlossaryTerm``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.glossary_term_name
    import capo_datazone.types.short_description


class DetailedGlossaryTerm(TypedDict, closed=True):
    name: NotRequired["capo_datazone.types.glossary_term_name.GlossaryTermName"]
    """<p>The name of a glossary term attached to the inventory asset.</p>"""
    short_description: NotRequired[
        "capo_datazone.types.short_description.ShortDescription"
    ]
    """<p>The shoft description of a glossary term attached to the inventory asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetailedGlossaryTerm) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "short_description" in value:
        out["shortDescription"] = value["short_description"]
    return out


def deserialize_json(data: dict) -> DetailedGlossaryTerm:
    out: DetailedGlossaryTerm = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("shortDescription") is not None:
        out["short_description"] = data["shortDescription"]
    return out


def redact_sensitive(value: DetailedGlossaryTerm) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "short_description" in value:
        out["short_description"] = "*** Sensitive Data Redacted ***"
    return out
