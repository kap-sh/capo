"""Generated from Smithy shape ``com.amazonaws.qapps#PredictAppDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.app_definition_input
    import capo_qapps.types.description
    import capo_qapps.types.title


class PredictAppDefinition(TypedDict, closed=True):
    title: "capo_qapps.types.title.Title"
    """<p>The title of the generated Q App definition.</p>"""
    description: NotRequired["capo_qapps.types.description.Description"]
    """<p>The description of the generated Q App definition.</p>"""
    app_definition: "capo_qapps.types.app_definition_input.AppDefinitionInput"
    """<p>The definition specifying the cards and flow of the generated Q App.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictAppDefinition) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_qapps.types.app_definition_input

    out["appDefinition"] = capo_qapps.types.app_definition_input.serialize_json(
        value["app_definition"]
    )
    return out


def deserialize_json(data: dict) -> PredictAppDefinition:
    out: PredictAppDefinition = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("appDefinition") is not None:
        import capo_qapps.types.app_definition_input

        out["app_definition"] = capo_qapps.types.app_definition_input.deserialize_json(
            data["appDefinition"]
        )
    else:
        raise DeserializationError("PredictAppDefinition.app_definition required")
    return out
