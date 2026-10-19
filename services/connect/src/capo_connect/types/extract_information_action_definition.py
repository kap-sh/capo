"""Generated from Smithy shape ``com.amazonaws.connect#ExtractInformationActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.rules_extraction_definition_identifier_list


class ExtractInformationActionDefinition(TypedDict, closed=True):
    rules_extraction_definitions: "capo_connect.types.rules_extraction_definition_identifier_list.RulesExtractionDefinitionIdentifierList"
    """<p>The list of extraction definition identifiers that specify what data to extract.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractInformationActionDefinition) -> dict:
    out: dict = {}
    import capo_connect.types.rules_extraction_definition_identifier_list

    out["RulesExtractionDefinitions"] = (
        capo_connect.types.rules_extraction_definition_identifier_list.serialize_json(
            value["rules_extraction_definitions"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExtractInformationActionDefinition:
    out: ExtractInformationActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("RulesExtractionDefinitions") is not None:
        import capo_connect.types.rules_extraction_definition_identifier_list

        out["rules_extraction_definitions"] = (
            capo_connect.types.rules_extraction_definition_identifier_list.deserialize_json(
                data["RulesExtractionDefinitions"]
            )
        )
    else:
        out["rules_extraction_definitions"] = []
    return out
