"""Generated from Smithy shape ``com.amazonaws.shield#UpdateEmergencyContactSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.emergency_contact_list


class UpdateEmergencyContactSettingsRequest(TypedDict, closed=True):
    emergency_contact_list: NotRequired[
        "capo_shield.types.emergency_contact_list.EmergencyContactList"
    ]
    """<p>A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.</p> <p>If you have proactive engagement enabled, the contact list must include at least one phone number.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEmergencyContactSettingsRequest) -> dict:
    out: dict = {}
    if "emergency_contact_list" in value:
        import capo_shield.types.emergency_contact_list

        out["EmergencyContactList"] = (
            capo_shield.types.emergency_contact_list.serialize_aws_json_1_1(
                value["emergency_contact_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEmergencyContactSettingsRequest:
    out: UpdateEmergencyContactSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmergencyContactList") is not None:
        import capo_shield.types.emergency_contact_list

        out["emergency_contact_list"] = (
            capo_shield.types.emergency_contact_list.deserialize_aws_json_1_1(
                data["EmergencyContactList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateEmergencyContactSettingsRequest) -> dict:
    out: dict = {}
    if "emergency_contact_list" in value:
        import capo_shield.types.emergency_contact_list

        out["EmergencyContactList"] = (
            capo_shield.types.emergency_contact_list.serialize_cbor(
                value["emergency_contact_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateEmergencyContactSettingsRequest:
    out: UpdateEmergencyContactSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmergencyContactList") is not None:
        import capo_shield.types.emergency_contact_list

        out["emergency_contact_list"] = (
            capo_shield.types.emergency_contact_list.deserialize_cbor(
                data["EmergencyContactList"]
            )
        )
    return out
