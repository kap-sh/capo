"""Generated from Smithy shape ``com.amazonaws.ram#PermissionTemplateParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.permission_template_parameter_type
    import capo_ram.types.permission_template_parameter_value_list
    import capo_ram.types.string


class PermissionTemplateParameter(TypedDict, closed=True):
    name: NotRequired["capo_ram.types.string.String"]
    """<p>The name of the template parameter.</p>"""
    type: NotRequired[
        "capo_ram.types.permission_template_parameter_type.PermissionTemplateParameterType"
    ]
    """<p>The type of the template parameter. This can be one of the following values:</p> <ul> <li> <p> <code>STRING</code> – A single string value.</p> </li> <li> <p> <code>STRING_LIST</code> – One or more string values.</p> </li> </ul>"""
    description: NotRequired["capo_ram.types.string.String"]
    """<p>A description of the template parameter.</p>"""
    values: NotRequired[
        "capo_ram.types.permission_template_parameter_value_list.PermissionTemplateParameterValueList"
    ]
    """<p>The values assigned to this template parameter in the context of a permission association. This field is present only when the parameter has been assigned values (for example, in the response from <a>ListPermissionAssociations</a> or <a>ListResourceSharePermissions</a>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionTemplateParameter) -> dict:
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
    if "values" in value:
        import capo_ram.types.permission_template_parameter_value_list

        out["values"] = (
            capo_ram.types.permission_template_parameter_value_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> PermissionTemplateParameter:
    out: PermissionTemplateParameter = {}  # type: ignore[typeddict-item]
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
    if data.get("values") is not None:
        import capo_ram.types.permission_template_parameter_value_list

        out["values"] = (
            capo_ram.types.permission_template_parameter_value_list.deserialize_json(
                data["values"]
            )
        )
    return out
