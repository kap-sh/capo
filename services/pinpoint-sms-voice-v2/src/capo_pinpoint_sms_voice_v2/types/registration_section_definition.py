"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationSectionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_section_display_hints
    import capo_pinpoint_sms_voice_v2.types.section_path


class RegistrationSectionDefinition(TypedDict, closed=True):
    section_path: "capo_pinpoint_sms_voice_v2.types.section_path.SectionPath"
    """<p>The path to the section of the registration.</p>"""
    display_hints: "capo_pinpoint_sms_voice_v2.types.registration_section_display_hints.RegistrationSectionDisplayHints"
    """<p>The path to the section of the registration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationSectionDefinition) -> dict:
    out: dict = {}
    out["SectionPath"] = value["section_path"]
    import capo_pinpoint_sms_voice_v2.types.registration_section_display_hints

    out["DisplayHints"] = (
        capo_pinpoint_sms_voice_v2.types.registration_section_display_hints.serialize_aws_json_1_0(
            value["display_hints"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationSectionDefinition:
    out: RegistrationSectionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("SectionPath") is not None:
        out["section_path"] = data["SectionPath"]
    else:
        out["section_path"] = ""
    if data.get("DisplayHints") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_section_display_hints

        out["display_hints"] = (
            capo_pinpoint_sms_voice_v2.types.registration_section_display_hints.deserialize_aws_json_1_0(
                data["DisplayHints"]
            )
        )
    else:
        raise DeserializationError(
            "RegistrationSectionDefinition.display_hints required"
        )
    return out
