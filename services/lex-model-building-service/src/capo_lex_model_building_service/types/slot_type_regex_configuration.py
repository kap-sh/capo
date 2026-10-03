"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotTypeRegexConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.regex_pattern


class SlotTypeRegexConfiguration(TypedDict, closed=True):
    pattern: "capo_lex_model_building_service.types.regex_pattern.RegexPattern"
    r"""<p>A regular expression used to validate the value of a slot. </p> <p>Use a standard regular expression. Amazon Lex supports the following characters in the regular expression:</p> <ul> <li> <p>A-Z, a-z</p> </li> <li> <p>0-9</p> </li> <li> <p>Unicode characters ("\ u<Unicode>")</p> </li> </ul> <p>Represent Unicode characters with four digits, for example "\u0041" or "\u005A".</p> <p>The following regular expression operators are not supported:</p> <ul> <li> <p>Infinite repeaters: *, +, or {x,} with no upper bound.</p> </li> <li> <p>Wild card (.)</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeRegexConfiguration) -> dict:
    out: dict = {}
    out["pattern"] = value["pattern"]
    return out


def deserialize_json(data: dict) -> SlotTypeRegexConfiguration:
    out: SlotTypeRegexConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("pattern") is not None:
        out["pattern"] = data["pattern"]
    else:
        raise DeserializationError("SlotTypeRegexConfiguration.pattern required")
    return out
