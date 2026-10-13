"""Generated from Smithy shape ``com.amazonaws.devicefarm#StopRemoteAccessSessionResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.remote_access_session


class StopRemoteAccessSessionResult(TypedDict, closed=True):
    remote_access_session: NotRequired[
        "capo_device_farm.types.remote_access_session.RemoteAccessSession"
    ]
    """<p>A container that represents the metadata from the service about the remote access session you are stopping.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopRemoteAccessSessionResult) -> dict:
    out: dict = {}
    if "remote_access_session" in value:
        import capo_device_farm.types.remote_access_session

        out["remoteAccessSession"] = (
            capo_device_farm.types.remote_access_session.serialize_aws_json_1_1(
                value["remote_access_session"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopRemoteAccessSessionResult:
    out: StopRemoteAccessSessionResult = {}  # type: ignore[typeddict-item]
    if data.get("remoteAccessSession") is not None:
        import capo_device_farm.types.remote_access_session

        out["remote_access_session"] = (
            capo_device_farm.types.remote_access_session.deserialize_aws_json_1_1(
                data["remoteAccessSession"]
            )
        )
    return out


def redact_sensitive(value: StopRemoteAccessSessionResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "remote_access_session" in value:
        import capo_device_farm.types.remote_access_session

        out["remote_access_session"] = (
            capo_device_farm.types.remote_access_session.redact_sensitive(
                value["remote_access_session"]
            )
        )
    return out
