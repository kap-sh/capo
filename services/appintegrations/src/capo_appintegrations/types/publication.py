"""Generated from Smithy shape ``com.amazonaws.appintegrations#Publication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.description
    import capo_appintegrations.types.event_definition_schema
    import capo_appintegrations.types.event_name


class Publication(TypedDict, closed=True):
    event: "capo_appintegrations.types.event_name.EventName"
    """<p>The name of the publication.</p>"""
    schema: "capo_appintegrations.types.event_definition_schema.EventDefinitionSchema"
    """<p>The JSON schema of the publication event.</p>"""
    description: NotRequired["capo_appintegrations.types.description.Description"]
    """<p>The description of the publication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Publication) -> dict:
    out: dict = {}
    out["Event"] = value["event"]
    out["Schema"] = value["schema"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> Publication:
    out: Publication = {}  # type: ignore[typeddict-item]
    if data.get("Event") is not None:
        out["event"] = data["Event"]
    else:
        out["event"] = ""
    if data.get("Schema") is not None:
        out["schema"] = data["Schema"]
    else:
        out["schema"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
