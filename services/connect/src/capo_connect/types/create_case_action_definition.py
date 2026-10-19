"""Generated from Smithy shape ``com.amazonaws.connect#CreateCaseActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.field_values
    import capo_connect.types.template_id


class CreateCaseActionDefinition(TypedDict, closed=True):
    fields: "capo_connect.types.field_values.FieldValues"
    """<p>An array of objects with <code>Field ID</code> and <code>Value</code> data.</p>"""
    template_id: "capo_connect.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseActionDefinition) -> dict:
    out: dict = {}
    import capo_connect.types.field_values

    out["Fields"] = capo_connect.types.field_values.serialize_json(value["fields"])
    out["TemplateId"] = value["template_id"]
    return out


def deserialize_json(data: dict) -> CreateCaseActionDefinition:
    out: CreateCaseActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Fields") is not None:
        import capo_connect.types.field_values

        out["fields"] = capo_connect.types.field_values.deserialize_json(data["Fields"])
    else:
        out["fields"] = []
    if data.get("TemplateId") is not None:
        out["template_id"] = data["TemplateId"]
    else:
        out["template_id"] = ""
    return out
