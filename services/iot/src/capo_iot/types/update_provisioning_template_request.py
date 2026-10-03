"""Generated from Smithy shape ``com.amazonaws.iot#UpdateProvisioningTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.enabled2
    import capo_iot.types.provisioning_hook
    import capo_iot.types.remove_hook
    import capo_iot.types.role_arn
    import capo_iot.types.template_description
    import capo_iot.types.template_name
    import capo_iot.types.template_version_id


class UpdateProvisioningTemplateRequest(TypedDict, closed=True):
    template_name: "capo_iot.types.template_name.TemplateName"
    """<p>The name of the provisioning template.</p>"""
    description: NotRequired["capo_iot.types.template_description.TemplateDescription"]
    """<p>The description of the provisioning template.</p>"""
    enabled: NotRequired["capo_iot.types.enabled2.Enabled2"]
    """<p>True to enable the provisioning template, otherwise false.</p>"""
    default_version_id: NotRequired[
        "capo_iot.types.template_version_id.TemplateVersionId"
    ]
    """<p>The ID of the default provisioning template version.</p>"""
    provisioning_role_arn: NotRequired["capo_iot.types.role_arn.RoleArn"]
    """<p>The ARN of the role associated with the provisioning template. This IoT role grants permission to provision a device.</p>"""
    pre_provisioning_hook: NotRequired[
        "capo_iot.types.provisioning_hook.ProvisioningHook"
    ]
    """<p>Updates the pre-provisioning hook template. Only supports template of type <code>FLEET_PROVISIONING</code>. For more information about provisioning template types, see <a href="https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningTemplate.html#iot-CreateProvisioningTemplate-request-type">type</a>.</p>"""
    remove_pre_provisioning_hook: NotRequired["capo_iot.types.remove_hook.RemoveHook"]
    """<p>Removes pre-provisioning hook template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProvisioningTemplateRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "default_version_id" in value:
        out["defaultVersionId"] = value["default_version_id"]
    if "provisioning_role_arn" in value:
        out["provisioningRoleArn"] = value["provisioning_role_arn"]
    if "pre_provisioning_hook" in value:
        import capo_iot.types.provisioning_hook

        out["preProvisioningHook"] = capo_iot.types.provisioning_hook.serialize_json(
            value["pre_provisioning_hook"]
        )
    if "remove_pre_provisioning_hook" in value:
        out["removePreProvisioningHook"] = value["remove_pre_provisioning_hook"]
    return out


def deserialize_json(data: dict) -> UpdateProvisioningTemplateRequest:
    out: UpdateProvisioningTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("defaultVersionId") is not None:
        out["default_version_id"] = data["defaultVersionId"]
    if data.get("provisioningRoleArn") is not None:
        out["provisioning_role_arn"] = data["provisioningRoleArn"]
    if data.get("preProvisioningHook") is not None:
        import capo_iot.types.provisioning_hook

        out["pre_provisioning_hook"] = (
            capo_iot.types.provisioning_hook.deserialize_json(
                data["preProvisioningHook"]
            )
        )
    if data.get("removePreProvisioningHook") is not None:
        out["remove_pre_provisioning_hook"] = data["removePreProvisioningHook"]
    return out
