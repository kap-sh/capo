"""Generated from Smithy shape ``com.amazonaws.devicefarm#RemoteAccessSessions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.remote_access_session

RemoteAccessSessions: TypeAlias = list[
    "capo_device_farm.types.remote_access_session.RemoteAccessSession"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoteAccessSessions) -> list:
    import capo_device_farm.types.remote_access_session

    out: list = []
    for item in value:
        out.append(
            capo_device_farm.types.remote_access_session.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RemoteAccessSessions:
    import capo_device_farm.types.remote_access_session

    out: RemoteAccessSessions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_device_farm.types.remote_access_session.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: RemoteAccessSessions) -> list[Any]:
    import capo_device_farm.types.remote_access_session

    return [
        capo_device_farm.types.remote_access_session.redact_sensitive(item)
        for item in value
    ]
