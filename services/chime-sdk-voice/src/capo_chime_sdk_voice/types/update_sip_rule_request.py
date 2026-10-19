"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateSipRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.nullable_boolean
    import capo_chime_sdk_voice.types.sip_rule_name
    import capo_chime_sdk_voice.types.sip_rule_target_application_list


class UpdateSipRuleRequest(TypedDict, closed=True):
    sip_rule_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The SIP rule ID.</p>"""
    name: "capo_chime_sdk_voice.types.sip_rule_name.SipRuleName"
    """<p>The new name for the specified SIP rule.</p>"""
    disabled: NotRequired["capo_chime_sdk_voice.types.nullable_boolean.NullableBoolean"]
    """<p>The new value that indicates whether the rule is disabled.</p>"""
    target_applications: NotRequired[
        "capo_chime_sdk_voice.types.sip_rule_target_application_list.SipRuleTargetApplicationList"
    ]
    """<p>The new list of target applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSipRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    if "target_applications" in value:
        import capo_chime_sdk_voice.types.sip_rule_target_application_list

        out["TargetApplications"] = (
            capo_chime_sdk_voice.types.sip_rule_target_application_list.serialize_json(
                value["target_applications"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSipRuleRequest:
    out: UpdateSipRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Disabled") is not None:
        out["disabled"] = data["Disabled"]
    if data.get("TargetApplications") is not None:
        import capo_chime_sdk_voice.types.sip_rule_target_application_list

        out["target_applications"] = (
            capo_chime_sdk_voice.types.sip_rule_target_application_list.deserialize_json(
                data["TargetApplications"]
            )
        )
    return out
