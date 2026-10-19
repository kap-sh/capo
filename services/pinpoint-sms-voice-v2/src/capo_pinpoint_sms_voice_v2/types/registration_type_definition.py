"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationTypeDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_type
    import capo_pinpoint_sms_voice_v2.types.registration_type_display_hints
    import capo_pinpoint_sms_voice_v2.types.supported_association_list


class RegistrationTypeDefinition(TypedDict, closed=True):
    registration_type: (
        "capo_pinpoint_sms_voice_v2.types.registration_type.RegistrationType"
    )
    """<p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    supported_associations: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.supported_association_list.SupportedAssociationList"
    ]
    """<p>The supported association behavior for the registration type.</p>"""
    display_hints: "capo_pinpoint_sms_voice_v2.types.registration_type_display_hints.RegistrationTypeDisplayHints"
    """<p>Provides help information on the registration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationTypeDefinition) -> dict:
    out: dict = {}
    out["RegistrationType"] = value["registration_type"]
    if "supported_associations" in value:
        import capo_pinpoint_sms_voice_v2.types.supported_association_list

        out["SupportedAssociations"] = (
            capo_pinpoint_sms_voice_v2.types.supported_association_list.serialize_aws_json_1_0(
                value["supported_associations"]
            )
        )
    import capo_pinpoint_sms_voice_v2.types.registration_type_display_hints

    out["DisplayHints"] = (
        capo_pinpoint_sms_voice_v2.types.registration_type_display_hints.serialize_aws_json_1_0(
            value["display_hints"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationTypeDefinition:
    out: RegistrationTypeDefinition = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationType") is not None:
        out["registration_type"] = data["RegistrationType"]
    else:
        out["registration_type"] = ""
    if data.get("SupportedAssociations") is not None:
        import capo_pinpoint_sms_voice_v2.types.supported_association_list

        out["supported_associations"] = (
            capo_pinpoint_sms_voice_v2.types.supported_association_list.deserialize_aws_json_1_0(
                data["SupportedAssociations"]
            )
        )
    if data.get("DisplayHints") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_type_display_hints

        out["display_hints"] = (
            capo_pinpoint_sms_voice_v2.types.registration_type_display_hints.deserialize_aws_json_1_0(
                data["DisplayHints"]
            )
        )
    else:
        raise DeserializationError("RegistrationTypeDefinition.display_hints required")
    return out
