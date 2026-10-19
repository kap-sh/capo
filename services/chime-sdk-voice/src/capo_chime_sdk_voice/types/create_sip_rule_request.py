"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateSipRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.nullable_boolean
    import capo_chime_sdk_voice.types.sip_rule_name
    import capo_chime_sdk_voice.types.sip_rule_target_application_list
    import capo_chime_sdk_voice.types.sip_rule_trigger_type


class CreateSipRuleRequest(TypedDict, closed=True):
    name: "capo_chime_sdk_voice.types.sip_rule_name.SipRuleName"
    """<p>The name of the SIP rule.</p>"""
    trigger_type: "capo_chime_sdk_voice.types.sip_rule_trigger_type.SipRuleTriggerType"
    """<p>The type of trigger assigned to the SIP rule in <code>TriggerValue</code>, currently <code>RequestUriHostname</code> or <code>ToPhoneNumber</code>.</p>"""
    trigger_value: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>If <code>TriggerType</code> is <code>RequestUriHostname</code>, the value can be the outbound host name of a Voice Connector. If <code>TriggerType</code> is <code>ToPhoneNumber</code>, the value can be a customer-owned phone number in the E164 format. The <code>SipMediaApplication</code> specified in the <code>SipRule</code> is triggered if the request URI in an incoming SIP request matches the <code>RequestUriHostname</code>, or if the <code>To</code> header in the incoming SIP request matches the <code>ToPhoneNumber</code> value.</p>"""
    disabled: NotRequired["capo_chime_sdk_voice.types.nullable_boolean.NullableBoolean"]
    """<p>Disables or enables a SIP rule. You must disable SIP rules before you can delete them.</p>"""
    target_applications: "capo_chime_sdk_voice.types.sip_rule_target_application_list.SipRuleTargetApplicationList"
    """<p>List of SIP media applications, with priority and AWS Region. Only one SIP application per AWS Region can be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSipRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_chime_sdk_voice.types.sip_rule_trigger_type

    out["TriggerType"] = (
        capo_chime_sdk_voice.types.sip_rule_trigger_type.serialize_json(
            value["trigger_type"]
        )
    )
    out["TriggerValue"] = value["trigger_value"]
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    import capo_chime_sdk_voice.types.sip_rule_target_application_list

    out["TargetApplications"] = (
        capo_chime_sdk_voice.types.sip_rule_target_application_list.serialize_json(
            value["target_applications"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateSipRuleRequest:
    out: CreateSipRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("TriggerType") is not None:
        import capo_chime_sdk_voice.types.sip_rule_trigger_type

        out["trigger_type"] = (
            capo_chime_sdk_voice.types.sip_rule_trigger_type.deserialize_json(
                data["TriggerType"]
            )
        )
    else:
        import typing

        out["trigger_type"] = typing.cast(
            "capo_chime_sdk_voice.types.sip_rule_trigger_type.SipRuleTriggerType", ""
        )
    if data.get("TriggerValue") is not None:
        out["trigger_value"] = data["TriggerValue"]
    else:
        out["trigger_value"] = ""
    if data.get("Disabled") is not None:
        out["disabled"] = data["Disabled"]
    if data.get("TargetApplications") is not None:
        import capo_chime_sdk_voice.types.sip_rule_target_application_list

        out["target_applications"] = (
            capo_chime_sdk_voice.types.sip_rule_target_application_list.deserialize_json(
                data["TargetApplications"]
            )
        )
    else:
        out["target_applications"] = []
    return out
