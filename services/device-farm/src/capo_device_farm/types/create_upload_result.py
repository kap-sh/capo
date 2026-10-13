"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateUploadResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.upload


class CreateUploadResult(TypedDict, closed=True):
    upload: NotRequired["capo_device_farm.types.upload.Upload"]
    """<p>The newly created upload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUploadResult) -> dict:
    out: dict = {}
    if "upload" in value:
        import capo_device_farm.types.upload

        out["upload"] = capo_device_farm.types.upload.serialize_aws_json_1_1(
            value["upload"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUploadResult:
    out: CreateUploadResult = {}  # type: ignore[typeddict-item]
    if data.get("upload") is not None:
        import capo_device_farm.types.upload

        out["upload"] = capo_device_farm.types.upload.deserialize_aws_json_1_1(
            data["upload"]
        )
    return out


def redact_sensitive(value: CreateUploadResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "upload" in value:
        import capo_device_farm.types.upload

        out["upload"] = capo_device_farm.types.upload.redact_sensitive(value["upload"])
    return out
