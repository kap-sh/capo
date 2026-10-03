"""Generated from Smithy shape ``com.amazonaws.iot#CreateProvisioningTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.enabled2
    import capo_iot.types.provisioning_hook
    import capo_iot.types.role_arn
    import capo_iot.types.tag_list
    import capo_iot.types.template_body
    import capo_iot.types.template_description
    import capo_iot.types.template_name
    import capo_iot.types.template_type


class CreateProvisioningTemplateRequest(TypedDict, closed=True):
    template_name: "capo_iot.types.template_name.TemplateName"
    """<p>The name of the provisioning template.</p>"""
    description: NotRequired["capo_iot.types.template_description.TemplateDescription"]
    """<p>The description of the provisioning template.</p>"""
    template_body: "capo_iot.types.template_body.TemplateBody"
    """<p>The JSON formatted contents of the provisioning template.</p>"""
    enabled: NotRequired["capo_iot.types.enabled2.Enabled2"]
    """<p>True to enable the provisioning template, otherwise false.</p>"""
    provisioning_role_arn: "capo_iot.types.role_arn.RoleArn"
    """<p>The role ARN for the role associated with the provisioning template. This IoT role grants permission to provision a device.</p>"""
    pre_provisioning_hook: NotRequired[
        "capo_iot.types.provisioning_hook.ProvisioningHook"
    ]
    """<p>Creates a pre-provisioning hook template. Only supports template of type <code>FLEET_PROVISIONING</code>. For more information about provisioning template types, see <a href="https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningTemplate.html#iot-CreateProvisioningTemplate-request-type">type</a>.</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the provisioning template.</p> <note> <p>For URI Request parameters use format: ...key1=value1&key2=value2...</p> <p>For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."</p> <p>For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."</p> </note>"""
    type: NotRequired["capo_iot.types.template_type.TemplateType"]
    """<p>The type you define in a provisioning template. You can create a template with only one type. You can't change the template type after its creation. The default value is <code>FLEET_PROVISIONING</code>. For more information about provisioning template, see: <a href="https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html">Provisioning template</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisioningTemplateRequest) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["templateBody"] = value["template_body"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    out["provisioningRoleArn"] = value["provisioning_role_arn"]
    if "pre_provisioning_hook" in value:
        import capo_iot.types.provisioning_hook

        out["preProvisioningHook"] = capo_iot.types.provisioning_hook.serialize_json(
            value["pre_provisioning_hook"]
        )
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    if "type" in value:
        import capo_iot.types.template_type

        out["type"] = capo_iot.types.template_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> CreateProvisioningTemplateRequest:
    out: CreateProvisioningTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "CreateProvisioningTemplateRequest.template_name required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("templateBody") is not None:
        out["template_body"] = data["templateBody"]
    else:
        raise DeserializationError(
            "CreateProvisioningTemplateRequest.template_body required"
        )
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("provisioningRoleArn") is not None:
        out["provisioning_role_arn"] = data["provisioningRoleArn"]
    else:
        raise DeserializationError(
            "CreateProvisioningTemplateRequest.provisioning_role_arn required"
        )
    if data.get("preProvisioningHook") is not None:
        import capo_iot.types.provisioning_hook

        out["pre_provisioning_hook"] = (
            capo_iot.types.provisioning_hook.deserialize_json(
                data["preProvisioningHook"]
            )
        )
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    if data.get("type") is not None:
        import capo_iot.types.template_type

        out["type"] = capo_iot.types.template_type.deserialize_json(data["type"])
    return out
