"""Generated from Smithy shape ``com.amazonaws.geoplaces#ParsedQueryComponent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string


class ParsedQueryComponent(TypedDict, closed=True):
    start_index: NotRequired["int"]
    """<p>Start index of the parsed query component.</p>"""
    end_index: NotRequired["int"]
    """<p>End index of the parsed query component.</p>"""
    value: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Value of the parsed query component.</p>"""
    query_component: NotRequired[
        "capo_geo_places.types.sensitive_string.SensitiveString"
    ]
    """<p>The address component that the parsed query component corresponds to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParsedQueryComponent) -> dict:
    out: dict = {}
    if "start_index" in value:
        out["StartIndex"] = value["start_index"]
    if "end_index" in value:
        out["EndIndex"] = value["end_index"]
    if "value" in value:
        out["Value"] = value["value"]
    if "query_component" in value:
        out["QueryComponent"] = value["query_component"]
    return out


def deserialize_json(data: dict) -> ParsedQueryComponent:
    out: ParsedQueryComponent = {}  # type: ignore[typeddict-item]
    if data.get("StartIndex") is not None:
        out["start_index"] = data["StartIndex"]
    if data.get("EndIndex") is not None:
        out["end_index"] = data["EndIndex"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("QueryComponent") is not None:
        out["query_component"] = data["QueryComponent"]
    return out


def redact_sensitive(value: ParsedQueryComponent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    if "query_component" in value:
        out["query_component"] = "*** Sensitive Data Redacted ***"
    return out
