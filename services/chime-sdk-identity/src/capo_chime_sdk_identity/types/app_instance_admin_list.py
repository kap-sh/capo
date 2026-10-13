"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceAdminList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_admin_summary

AppInstanceAdminList: TypeAlias = list[
    "capo_chime_sdk_identity.types.app_instance_admin_summary.AppInstanceAdminSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceAdminList) -> list:
    import capo_chime_sdk_identity.types.app_instance_admin_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_identity.types.app_instance_admin_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AppInstanceAdminList:
    import capo_chime_sdk_identity.types.app_instance_admin_summary

    out: AppInstanceAdminList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_identity.types.app_instance_admin_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AppInstanceAdminList) -> list[Any]:
    import capo_chime_sdk_identity.types.app_instance_admin_summary

    return [
        capo_chime_sdk_identity.types.app_instance_admin_summary.redact_sensitive(item)
        for item in value
    ]
