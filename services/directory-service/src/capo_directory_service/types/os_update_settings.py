"""Generated from Smithy shape ``com.amazonaws.directoryservice#OSUpdateSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.os_version


class OSUpdateSettings(TypedDict, closed=True):
    os_version: NotRequired["capo_directory_service.types.os_version.OSVersion"]
    """<p>OS version that the directory needs to be updated to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OSUpdateSettings) -> dict:
    out: dict = {}
    if "os_version" in value:
        import capo_directory_service.types.os_version

        out["OSVersion"] = (
            capo_directory_service.types.os_version.serialize_aws_json_1_1(
                value["os_version"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OSUpdateSettings:
    out: OSUpdateSettings = {}  # type: ignore[typeddict-item]
    if data.get("OSVersion") is not None:
        import capo_directory_service.types.os_version

        out["os_version"] = (
            capo_directory_service.types.os_version.deserialize_aws_json_1_1(
                data["OSVersion"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OSUpdateSettings) -> dict:
    out: dict = {}
    if "os_version" in value:
        import capo_directory_service.types.os_version

        out["OSVersion"] = capo_directory_service.types.os_version.serialize_cbor(
            value["os_version"]
        )
    return out


def deserialize_cbor(data: dict) -> OSUpdateSettings:
    out: OSUpdateSettings = {}  # type: ignore[typeddict-item]
    if data.get("OSVersion") is not None:
        import capo_directory_service.types.os_version

        out["os_version"] = capo_directory_service.types.os_version.deserialize_cbor(
            data["OSVersion"]
        )
    return out
