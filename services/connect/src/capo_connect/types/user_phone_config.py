"""Generated from Smithy shape ``com.amazonaws.connect#UserPhoneConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.after_contact_work_time_limit
    import capo_connect.types.auto_accept
    import capo_connect.types.persistent_connection
    import capo_connect.types.phone_type
    import capo_connect.types.sensitive_phone_number


class UserPhoneConfig(TypedDict, closed=True):
    phone_type: "capo_connect.types.phone_type.PhoneType"
    """<p>The phone type.</p>"""
    auto_accept: "capo_connect.types.auto_accept.AutoAccept"
    """<p>The Auto accept setting.</p>"""
    after_contact_work_time_limit: (
        "capo_connect.types.after_contact_work_time_limit.AfterContactWorkTimeLimit"
    )
    """<p>The After Call Work (ACW) timeout setting, in seconds. This parameter has a minimum value of 0 and a maximum value of 2,000,000 seconds (24 days). Enter 0 if you don't want to allocate a specific amount of ACW time. It essentially means an indefinite amount of time. When the conversation ends, ACW starts; the agent must choose Close contact to end ACW. </p> <note> <p>When returned by a <code>SearchUsers</code> call, <code>AfterContactWorkTimeLimit</code> is returned in milliseconds. </p> </note>"""
    desk_phone_number: NotRequired[
        "capo_connect.types.sensitive_phone_number.SensitivePhoneNumber"
    ]
    """<p>The phone number for the user's desk phone.</p>"""
    persistent_connection: NotRequired[
        "capo_connect.types.persistent_connection.PersistentConnection"
    ]
    """<p>The persistent connection setting for the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserPhoneConfig) -> dict:
    out: dict = {}
    import capo_connect.types.phone_type

    out["PhoneType"] = capo_connect.types.phone_type.serialize_json(
        value.get("phone_type", "SOFT_PHONE")
    )
    out["AutoAccept"] = value.get("auto_accept", False)
    out["AfterContactWorkTimeLimit"] = value.get("after_contact_work_time_limit", 0)
    if "desk_phone_number" in value:
        out["DeskPhoneNumber"] = value["desk_phone_number"]
    if "persistent_connection" in value:
        out["PersistentConnection"] = value["persistent_connection"]
    return out


def deserialize_json(data: dict) -> UserPhoneConfig:
    out: UserPhoneConfig = {}  # type: ignore[typeddict-item]
    if data.get("PhoneType") is not None:
        import capo_connect.types.phone_type

        out["phone_type"] = capo_connect.types.phone_type.deserialize_json(
            data["PhoneType"]
        )
    else:
        out["phone_type"] = "SOFT_PHONE"
    if data.get("AutoAccept") is not None:
        out["auto_accept"] = data["AutoAccept"]
    else:
        out["auto_accept"] = False
    if data.get("AfterContactWorkTimeLimit") is not None:
        out["after_contact_work_time_limit"] = data["AfterContactWorkTimeLimit"]
    else:
        out["after_contact_work_time_limit"] = 0
    if data.get("DeskPhoneNumber") is not None:
        out["desk_phone_number"] = data["DeskPhoneNumber"]
    if data.get("PersistentConnection") is not None:
        out["persistent_connection"] = data["PersistentConnection"]
    return out


def redact_sensitive(value: UserPhoneConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "desk_phone_number" in value:
        out["desk_phone_number"] = "*** Sensitive Data Redacted ***"
    return out
