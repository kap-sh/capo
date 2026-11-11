"""Generated from Smithy shape ``com.amazonaws.ram#PermissionTemplateParameterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.permission_template_parameter_value_list
    import capo_ram.types.string


class PermissionTemplateParameterInput(TypedDict, closed=True):
    name: NotRequired["capo_ram.types.string.String"]
    """<p>The name of the template parameter to assign a value to. This must match a parameter name declared in the permission template.</p>"""
    values: NotRequired[
        "capo_ram.types.permission_template_parameter_value_list.PermissionTemplateParameterValueList"
    ]
    """<p>The values to assign to the template parameter. For <code>STRING</code> type parameters, provide a single value. For <code>STRING_LIST</code> type parameters, provide one or more values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionTemplateParameterInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "values" in value:
        import capo_ram.types.permission_template_parameter_value_list

        out["values"] = (
            capo_ram.types.permission_template_parameter_value_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> PermissionTemplateParameterInput:
    out: PermissionTemplateParameterInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("values") is not None:
        import capo_ram.types.permission_template_parameter_value_list

        out["values"] = (
            capo_ram.types.permission_template_parameter_value_list.deserialize_json(
                data["values"]
            )
        )
    return out
