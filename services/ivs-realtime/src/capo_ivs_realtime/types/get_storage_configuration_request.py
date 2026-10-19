"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetStorageConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.storage_configuration_arn


class GetStorageConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.storage_configuration_arn.StorageConfigurationArn"
    """<p>ARN of the storage configuration to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStorageConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetStorageConfigurationRequest:
    out: GetStorageConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
