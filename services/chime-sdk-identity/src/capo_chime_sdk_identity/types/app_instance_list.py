"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_summary

AppInstanceList: TypeAlias = list[
    "capo_chime_sdk_identity.types.app_instance_summary.AppInstanceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceList) -> list:
    import capo_chime_sdk_identity.types.app_instance_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_identity.types.app_instance_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AppInstanceList:
    import capo_chime_sdk_identity.types.app_instance_summary

    out: AppInstanceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_identity.types.app_instance_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AppInstanceList) -> list[Any]:
    import capo_chime_sdk_identity.types.app_instance_summary

    return [
        capo_chime_sdk_identity.types.app_instance_summary.redact_sensitive(item)
        for item in value
    ]
