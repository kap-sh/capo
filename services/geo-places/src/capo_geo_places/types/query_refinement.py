"""Generated from Smithy shape ``com.amazonaws.geoplaces#QueryRefinement``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string


class QueryRefinement(TypedDict, closed=True):
    refined_term: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The term that will be suggested to the user.</p>"""
    original_term: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The sub-string of the original query that is replaced by this query term.</p>"""
    start_index: "int"
    """<p>Start index of the parsed component.</p>"""
    end_index: "int"
    """<p>End index of the parsed query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryRefinement) -> dict:
    out: dict = {}
    out["RefinedTerm"] = value["refined_term"]
    out["OriginalTerm"] = value["original_term"]
    out["StartIndex"] = value["start_index"]
    out["EndIndex"] = value["end_index"]
    return out


def deserialize_json(data: dict) -> QueryRefinement:
    out: QueryRefinement = {}  # type: ignore[typeddict-item]
    if data.get("RefinedTerm") is not None:
        out["refined_term"] = data["RefinedTerm"]
    else:
        out["refined_term"] = ""
    if data.get("OriginalTerm") is not None:
        out["original_term"] = data["OriginalTerm"]
    else:
        out["original_term"] = ""
    if data.get("StartIndex") is not None:
        out["start_index"] = data["StartIndex"]
    else:
        out["start_index"] = 0
    if data.get("EndIndex") is not None:
        out["end_index"] = data["EndIndex"]
    else:
        out["end_index"] = 0
    return out


def redact_sensitive(value: QueryRefinement) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "refined_term" in value:
        out["refined_term"] = "*** Sensitive Data Redacted ***"
    if "original_term" in value:
        out["original_term"] = "*** Sensitive Data Redacted ***"
    return out
