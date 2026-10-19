"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateFieldRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.field_attributes
    import capo_connectcases.types.field_description
    import capo_connectcases.types.field_name
    import capo_connectcases.types.field_type


class CreateFieldRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    name: "capo_connectcases.types.field_name.FieldName"
    """<p>The name of the field.</p>"""
    type: "capo_connectcases.types.field_type.FieldType"
    """<p>Defines the data type, some system constraints, and default display of the field.</p>"""
    description: NotRequired[
        "capo_connectcases.types.field_description.FieldDescription"
    ]
    """<p>The description of the field.</p>"""
    attributes: NotRequired["capo_connectcases.types.field_attributes.FieldAttributes"]
    """<p>Union of field attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFieldRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    if "description" in value:
        out["description"] = value["description"]
    if "attributes" in value:
        import capo_connectcases.types.field_attributes

        out["attributes"] = capo_connectcases.types.field_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> CreateFieldRequest:
    out: CreateFieldRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("attributes") is not None:
        import capo_connectcases.types.field_attributes

        out["attributes"] = capo_connectcases.types.field_attributes.deserialize_json(
            data["attributes"]
        )
    return out
