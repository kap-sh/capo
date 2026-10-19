"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateMobileDeviceAccessRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.device_model_list
    import capo_workmail.types.device_operating_system_list
    import capo_workmail.types.device_type_list
    import capo_workmail.types.device_user_agent_list
    import capo_workmail.types.mobile_device_access_rule_description
    import capo_workmail.types.mobile_device_access_rule_effect
    import capo_workmail.types.mobile_device_access_rule_id
    import capo_workmail.types.mobile_device_access_rule_name
    import capo_workmail.types.organization_id


class UpdateMobileDeviceAccessRuleRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization under which the rule will be updated.</p>"""
    mobile_device_access_rule_id: (
        "capo_workmail.types.mobile_device_access_rule_id.MobileDeviceAccessRuleId"
    )
    """<p>The identifier of the rule to be updated.</p>"""
    name: (
        "capo_workmail.types.mobile_device_access_rule_name.MobileDeviceAccessRuleName"
    )
    """<p>The updated rule name.</p>"""
    description: NotRequired[
        "capo_workmail.types.mobile_device_access_rule_description.MobileDeviceAccessRuleDescription"
    ]
    """<p>The updated rule description.</p>"""
    effect: "capo_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect"
    """<p>The effect of the rule when it matches. Allowed values are <code>ALLOW</code> or <code>DENY</code>.</p>"""
    device_types: NotRequired["capo_workmail.types.device_type_list.DeviceTypeList"]
    """<p>Device types that the updated rule will match.</p>"""
    not_device_types: NotRequired["capo_workmail.types.device_type_list.DeviceTypeList"]
    """<p>Device types that the updated rule <b>will not</b> match. All other device types will match.</p>"""
    device_models: NotRequired["capo_workmail.types.device_model_list.DeviceModelList"]
    """<p>Device models that the updated rule will match.</p>"""
    not_device_models: NotRequired[
        "capo_workmail.types.device_model_list.DeviceModelList"
    ]
    """<p>Device models that the updated rule <b>will not</b> match. All other device models will match.</p>"""
    device_operating_systems: NotRequired[
        "capo_workmail.types.device_operating_system_list.DeviceOperatingSystemList"
    ]
    """<p>Device operating systems that the updated rule will match.</p>"""
    not_device_operating_systems: NotRequired[
        "capo_workmail.types.device_operating_system_list.DeviceOperatingSystemList"
    ]
    """<p>Device operating systems that the updated rule <b>will not</b> match. All other device operating systems will match.</p>"""
    device_user_agents: NotRequired[
        "capo_workmail.types.device_user_agent_list.DeviceUserAgentList"
    ]
    """<p>User agents that the updated rule will match.</p>"""
    not_device_user_agents: NotRequired[
        "capo_workmail.types.device_user_agent_list.DeviceUserAgentList"
    ]
    """<p>User agents that the updated rule <b>will not</b> match. All other user agents will match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMobileDeviceAccessRuleRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["MobileDeviceAccessRuleId"] = value["mobile_device_access_rule_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_workmail.types.mobile_device_access_rule_effect

    out["Effect"] = (
        capo_workmail.types.mobile_device_access_rule_effect.serialize_aws_json_1_1(
            value["effect"]
        )
    )
    if "device_types" in value:
        import capo_workmail.types.device_type_list

        out["DeviceTypes"] = (
            capo_workmail.types.device_type_list.serialize_aws_json_1_1(
                value["device_types"]
            )
        )
    if "not_device_types" in value:
        import capo_workmail.types.device_type_list

        out["NotDeviceTypes"] = (
            capo_workmail.types.device_type_list.serialize_aws_json_1_1(
                value["not_device_types"]
            )
        )
    if "device_models" in value:
        import capo_workmail.types.device_model_list

        out["DeviceModels"] = (
            capo_workmail.types.device_model_list.serialize_aws_json_1_1(
                value["device_models"]
            )
        )
    if "not_device_models" in value:
        import capo_workmail.types.device_model_list

        out["NotDeviceModels"] = (
            capo_workmail.types.device_model_list.serialize_aws_json_1_1(
                value["not_device_models"]
            )
        )
    if "device_operating_systems" in value:
        import capo_workmail.types.device_operating_system_list

        out["DeviceOperatingSystems"] = (
            capo_workmail.types.device_operating_system_list.serialize_aws_json_1_1(
                value["device_operating_systems"]
            )
        )
    if "not_device_operating_systems" in value:
        import capo_workmail.types.device_operating_system_list

        out["NotDeviceOperatingSystems"] = (
            capo_workmail.types.device_operating_system_list.serialize_aws_json_1_1(
                value["not_device_operating_systems"]
            )
        )
    if "device_user_agents" in value:
        import capo_workmail.types.device_user_agent_list

        out["DeviceUserAgents"] = (
            capo_workmail.types.device_user_agent_list.serialize_aws_json_1_1(
                value["device_user_agents"]
            )
        )
    if "not_device_user_agents" in value:
        import capo_workmail.types.device_user_agent_list

        out["NotDeviceUserAgents"] = (
            capo_workmail.types.device_user_agent_list.serialize_aws_json_1_1(
                value["not_device_user_agents"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMobileDeviceAccessRuleRequest:
    out: UpdateMobileDeviceAccessRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("MobileDeviceAccessRuleId") is not None:
        out["mobile_device_access_rule_id"] = data["MobileDeviceAccessRuleId"]
    else:
        out["mobile_device_access_rule_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Effect") is not None:
        import capo_workmail.types.mobile_device_access_rule_effect

        out["effect"] = (
            capo_workmail.types.mobile_device_access_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    else:
        import typing

        out["effect"] = typing.cast(
            "capo_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect",
            "",
        )
    if data.get("DeviceTypes") is not None:
        import capo_workmail.types.device_type_list

        out["device_types"] = (
            capo_workmail.types.device_type_list.deserialize_aws_json_1_1(
                data["DeviceTypes"]
            )
        )
    if data.get("NotDeviceTypes") is not None:
        import capo_workmail.types.device_type_list

        out["not_device_types"] = (
            capo_workmail.types.device_type_list.deserialize_aws_json_1_1(
                data["NotDeviceTypes"]
            )
        )
    if data.get("DeviceModels") is not None:
        import capo_workmail.types.device_model_list

        out["device_models"] = (
            capo_workmail.types.device_model_list.deserialize_aws_json_1_1(
                data["DeviceModels"]
            )
        )
    if data.get("NotDeviceModels") is not None:
        import capo_workmail.types.device_model_list

        out["not_device_models"] = (
            capo_workmail.types.device_model_list.deserialize_aws_json_1_1(
                data["NotDeviceModels"]
            )
        )
    if data.get("DeviceOperatingSystems") is not None:
        import capo_workmail.types.device_operating_system_list

        out["device_operating_systems"] = (
            capo_workmail.types.device_operating_system_list.deserialize_aws_json_1_1(
                data["DeviceOperatingSystems"]
            )
        )
    if data.get("NotDeviceOperatingSystems") is not None:
        import capo_workmail.types.device_operating_system_list

        out["not_device_operating_systems"] = (
            capo_workmail.types.device_operating_system_list.deserialize_aws_json_1_1(
                data["NotDeviceOperatingSystems"]
            )
        )
    if data.get("DeviceUserAgents") is not None:
        import capo_workmail.types.device_user_agent_list

        out["device_user_agents"] = (
            capo_workmail.types.device_user_agent_list.deserialize_aws_json_1_1(
                data["DeviceUserAgents"]
            )
        )
    if data.get("NotDeviceUserAgents") is not None:
        import capo_workmail.types.device_user_agent_list

        out["not_device_user_agents"] = (
            capo_workmail.types.device_user_agent_list.deserialize_aws_json_1_1(
                data["NotDeviceUserAgents"]
            )
        )
    return out
