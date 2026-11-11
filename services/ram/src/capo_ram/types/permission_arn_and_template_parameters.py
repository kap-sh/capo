"""Generated from Smithy shape ``com.amazonaws.ram#PermissionArnAndTemplateParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.permission_template_parameter_input_list
    import capo_ram.types.string


class PermissionArnAndTemplateParameters(TypedDict, closed=True):
    permission_arn: NotRequired["capo_ram.types.string.String"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the permission to associate with the resource share.</p>"""
    permission_template_parameters: NotRequired[
        "capo_ram.types.permission_template_parameter_input_list.PermissionTemplateParameterInputList"
    ]
    """<p>The list of template parameter values to assign for this permission. You must provide values for all parameters declared in the permission template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionArnAndTemplateParameters) -> dict:
    out: dict = {}
    if "permission_arn" in value:
        out["permissionArn"] = value["permission_arn"]
    if "permission_template_parameters" in value:
        import capo_ram.types.permission_template_parameter_input_list

        out["permissionTemplateParameters"] = (
            capo_ram.types.permission_template_parameter_input_list.serialize_json(
                value["permission_template_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> PermissionArnAndTemplateParameters:
    out: PermissionArnAndTemplateParameters = {}  # type: ignore[typeddict-item]
    if data.get("permissionArn") is not None:
        out["permission_arn"] = data["permissionArn"]
    if data.get("permissionTemplateParameters") is not None:
        import capo_ram.types.permission_template_parameter_input_list

        out["permission_template_parameters"] = (
            capo_ram.types.permission_template_parameter_input_list.deserialize_json(
                data["permissionTemplateParameters"]
            )
        )
    return out
