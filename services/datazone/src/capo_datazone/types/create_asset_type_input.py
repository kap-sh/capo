"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAssetTypeInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.forms_input_map
    import capo_datazone.types.project_id
    import capo_datazone.types.type_name


class CreateAssetTypeInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The unique identifier of the Amazon DataZone domain where the custom asset type is being created.</p>"""
    name: "capo_datazone.types.type_name.TypeName"
    """<p>The name of the custom asset type.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The descripton of the custom asset type.</p>"""
    forms_input: "capo_datazone.types.forms_input_map.FormsInputMap"
    """<p>The metadata forms that are to be attached to the custom asset type.</p>"""
    owning_project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the Amazon DataZone project that is to own the custom asset type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetTypeInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_datazone.types.forms_input_map

    out["formsInput"] = capo_datazone.types.forms_input_map.serialize_json(
        value["forms_input"]
    )
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    return out


def deserialize_json(data: dict) -> CreateAssetTypeInput:
    out: CreateAssetTypeInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssetTypeInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("formsInput") is not None:
        import capo_datazone.types.forms_input_map

        out["forms_input"] = capo_datazone.types.forms_input_map.deserialize_json(
            data["formsInput"]
        )
    else:
        raise DeserializationError("CreateAssetTypeInput.forms_input required")
    if data.get("owningProjectIdentifier") is not None:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        raise DeserializationError(
            "CreateAssetTypeInput.owning_project_identifier required"
        )
    return out


def redact_sensitive(value: CreateAssetTypeInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
