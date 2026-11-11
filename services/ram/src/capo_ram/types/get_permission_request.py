"""Generated from Smithy shape ``com.amazonaws.ram#GetPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.integer
    import capo_ram.types.permission_template_parameter_input_list
    import capo_ram.types.string


class GetPermissionRequest(TypedDict, closed=True):
    permission_arn: "capo_ram.types.string.String"
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the permission whose contents you want to retrieve. To find the ARN for a permission, use either the <a>ListPermissions</a> operation or go to the <a href="https://console.aws.amazon.com/ram/home#Permissions:">Permissions library</a> page in the RAM console and then choose the name of the permission. The ARN is displayed on the detail page.</p>"""
    permission_version: NotRequired["capo_ram.types.integer.Integer"]
    """<p>Specifies the version number of the RAM permission to retrieve. If you don't specify this parameter, the operation retrieves the default version.</p> <p>To see the list of available versions, use <a>ListPermissionVersions</a>.</p>"""
    permission_template_parameters: NotRequired[
        "capo_ram.types.permission_template_parameter_input_list.PermissionTemplateParameterInputList"
    ]
    """<p>Specifies the template parameter values to use when rendering the permission's policy template. Each entry supplies a parameter name and its values. When you provide this parameter, the response contains the rendered policy with the specified values in place of the template parameter placeholders.</p> <p>For <code>STRING</code> type parameters, provide a single value. For <code>STRING_LIST</code> type parameters, provide one or more values.</p> <p>You can specify this parameter only for permissions that declare template parameters. You must provide values for all parameters declared in the permission template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPermissionRequest) -> dict:
    out: dict = {}
    out["permissionArn"] = value["permission_arn"]
    if "permission_version" in value:
        out["permissionVersion"] = value["permission_version"]
    if "permission_template_parameters" in value:
        import capo_ram.types.permission_template_parameter_input_list

        out["permissionTemplateParameters"] = (
            capo_ram.types.permission_template_parameter_input_list.serialize_json(
                value["permission_template_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPermissionRequest:
    out: GetPermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("permissionArn") is not None:
        out["permission_arn"] = data["permissionArn"]
    else:
        out["permission_arn"] = ""
    if data.get("permissionVersion") is not None:
        out["permission_version"] = data["permissionVersion"]
    if data.get("permissionTemplateParameters") is not None:
        import capo_ram.types.permission_template_parameter_input_list

        out["permission_template_parameters"] = (
            capo_ram.types.permission_template_parameter_input_list.deserialize_json(
                data["permissionTemplateParameters"]
            )
        )
    return out
