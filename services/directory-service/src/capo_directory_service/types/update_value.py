"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.os_update_settings


class UpdateValue(TypedDict, closed=True):
    os_update_settings: NotRequired[
        "capo_directory_service.types.os_update_settings.OSUpdateSettings"
    ]
    """<p> The OS update related settings. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateValue) -> dict:
    out: dict = {}
    if "os_update_settings" in value:
        import capo_directory_service.types.os_update_settings

        out["OSUpdateSettings"] = (
            capo_directory_service.types.os_update_settings.serialize_aws_json_1_1(
                value["os_update_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateValue:
    out: UpdateValue = {}  # type: ignore[typeddict-item]
    if data.get("OSUpdateSettings") is not None:
        import capo_directory_service.types.os_update_settings

        out["os_update_settings"] = (
            capo_directory_service.types.os_update_settings.deserialize_aws_json_1_1(
                data["OSUpdateSettings"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateValue) -> dict:
    out: dict = {}
    if "os_update_settings" in value:
        import capo_directory_service.types.os_update_settings

        out["OSUpdateSettings"] = (
            capo_directory_service.types.os_update_settings.serialize_cbor(
                value["os_update_settings"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateValue:
    out: UpdateValue = {}  # type: ignore[typeddict-item]
    if data.get("OSUpdateSettings") is not None:
        import capo_directory_service.types.os_update_settings

        out["os_update_settings"] = (
            capo_directory_service.types.os_update_settings.deserialize_cbor(
                data["OSUpdateSettings"]
            )
        )
    return out
