"""Generated from Smithy shape ``com.amazonaws.devicefarm#InstallToRemoteAccessSessionResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.upload


class InstallToRemoteAccessSessionResult(TypedDict, closed=True):
    app_upload: NotRequired["capo_device_farm.types.upload.Upload"]
    """<p>An app to upload or that has been uploaded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstallToRemoteAccessSessionResult) -> dict:
    out: dict = {}
    if "app_upload" in value:
        import capo_device_farm.types.upload

        out["appUpload"] = capo_device_farm.types.upload.serialize_aws_json_1_1(
            value["app_upload"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstallToRemoteAccessSessionResult:
    out: InstallToRemoteAccessSessionResult = {}  # type: ignore[typeddict-item]
    if data.get("appUpload") is not None:
        import capo_device_farm.types.upload

        out["app_upload"] = capo_device_farm.types.upload.deserialize_aws_json_1_1(
            data["appUpload"]
        )
    return out


def redact_sensitive(value: InstallToRemoteAccessSessionResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_upload" in value:
        import capo_device_farm.types.upload

        out["app_upload"] = capo_device_farm.types.upload.redact_sensitive(
            value["app_upload"]
        )
    return out
