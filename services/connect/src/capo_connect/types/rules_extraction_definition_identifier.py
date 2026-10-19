"""Generated from Smithy shape ``com.amazonaws.connect#RulesExtractionDefinitionIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.rules_extraction_definition_id


class RulesExtractionDefinitionIdentifier(TypedDict, closed=True):
    identifier: (
        "capo_connect.types.rules_extraction_definition_id.RulesExtractionDefinitionId"
    )
    """<p>The identifier of the extraction definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RulesExtractionDefinitionIdentifier) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> RulesExtractionDefinitionIdentifier:
    out: RulesExtractionDefinitionIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
