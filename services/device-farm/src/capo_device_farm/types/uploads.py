"""Generated from Smithy shape ``com.amazonaws.devicefarm#Uploads``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.upload

Uploads: TypeAlias = list["capo_device_farm.types.upload.Upload"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Uploads) -> list:
    import capo_device_farm.types.upload

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.upload.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Uploads:
    import capo_device_farm.types.upload

    out: Uploads = []
    for item in data:
        if item is None:
            continue
        out.append(capo_device_farm.types.upload.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Uploads) -> list[Any]:
    import capo_device_farm.types.upload

    return [capo_device_farm.types.upload.redact_sensitive(item) for item in value]
