"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CredentialLockerListDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.credential_locker_summary

CredentialLockerListDefinition: TypeAlias = list[
    "capo_iot_managed_integrations.types.credential_locker_summary.CredentialLockerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CredentialLockerListDefinition) -> list:
    import capo_iot_managed_integrations.types.credential_locker_summary

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.credential_locker_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CredentialLockerListDefinition:
    import capo_iot_managed_integrations.types.credential_locker_summary

    out: CredentialLockerListDefinition = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iot_managed_integrations.types.credential_locker_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: CredentialLockerListDefinition) -> list[Any]:
    import capo_iot_managed_integrations.types.credential_locker_summary

    return [
        capo_iot_managed_integrations.types.credential_locker_summary.redact_sensitive(
            item
        )
        for item in value
    ]
