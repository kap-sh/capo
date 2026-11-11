"""Generated from Smithy shape ``com.amazonaws.ram#PermissionTemplateParameterDeclaration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.permission_template_parameter_type
    import capo_ram.types.string


class PermissionTemplateParameterDeclaration(TypedDict, closed=True):
    name: NotRequired["capo_ram.types.string.String"]
    """<p>The name of the template parameter. This name is used as the placeholder in the policy template using the syntax <code>@{parameterName}</code>.</p>"""
    type: NotRequired[
        "capo_ram.types.permission_template_parameter_type.PermissionTemplateParameterType"
    ]
    """<p>The type of the template parameter. This can be one of the following values:</p> <ul> <li> <p> <code>STRING</code> – A single string value that is substituted directly into the template.</p> </li> <li> <p> <code>STRING_LIST</code> – One or more string values that expand to an array in the rendered policy.</p> </li> </ul>"""
    description: NotRequired["capo_ram.types.string.String"]
    """<p>A description of the template parameter that helps consumers understand what value to provide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionTemplateParameterDeclaration) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_ram.types.permission_template_parameter_type

        out["type"] = capo_ram.types.permission_template_parameter_type.serialize_json(
            value["type"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> PermissionTemplateParameterDeclaration:
    out: PermissionTemplateParameterDeclaration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("type") is not None:
        import capo_ram.types.permission_template_parameter_type

        out["type"] = (
            capo_ram.types.permission_template_parameter_type.deserialize_json(
                data["type"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
