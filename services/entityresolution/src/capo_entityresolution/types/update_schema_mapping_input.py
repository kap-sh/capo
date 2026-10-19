"""Generated from Smithy shape ``com.amazonaws.entityresolution#UpdateSchemaMappingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.description
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.schema_input_attributes


class UpdateSchemaMappingInput(TypedDict, closed=True):
    schema_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the schema. There can't be multiple <code>SchemaMappings</code> with the same name.</p>"""
    description: NotRequired["capo_entityresolution.types.description.Description"]
    """<p>A description of the schema.</p>"""
    mapped_input_fields: (
        "capo_entityresolution.types.schema_input_attributes.SchemaInputAttributes"
    )
    """<p>A list of <code>MappedInputFields</code>. Each <code>MappedInputField</code> corresponds to a column the source data table, and contains column name plus additional information that Entity Resolution uses for matching.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSchemaMappingInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import capo_entityresolution.types.schema_input_attributes

    out["mappedInputFields"] = (
        capo_entityresolution.types.schema_input_attributes.serialize_json(
            value["mapped_input_fields"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateSchemaMappingInput:
    out: UpdateSchemaMappingInput = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("mappedInputFields") is not None:
        import capo_entityresolution.types.schema_input_attributes

        out["mapped_input_fields"] = (
            capo_entityresolution.types.schema_input_attributes.deserialize_json(
                data["mappedInputFields"]
            )
        )
    else:
        out["mapped_input_fields"] = []
    return out
