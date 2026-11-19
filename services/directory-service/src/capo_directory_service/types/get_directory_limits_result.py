"""Generated from Smithy shape ``com.amazonaws.directoryservice#GetDirectoryLimitsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_limits


class GetDirectoryLimitsResult(TypedDict, closed=True):
    directory_limits: NotRequired[
        "capo_directory_service.types.directory_limits.DirectoryLimits"
    ]
    """<p>A <a>DirectoryLimits</a> object that contains the directory limits for the current Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDirectoryLimitsResult) -> dict:
    out: dict = {}
    if "directory_limits" in value:
        import capo_directory_service.types.directory_limits

        out["DirectoryLimits"] = (
            capo_directory_service.types.directory_limits.serialize_aws_json_1_1(
                value["directory_limits"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDirectoryLimitsResult:
    out: GetDirectoryLimitsResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryLimits") is not None:
        import capo_directory_service.types.directory_limits

        out["directory_limits"] = (
            capo_directory_service.types.directory_limits.deserialize_aws_json_1_1(
                data["DirectoryLimits"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDirectoryLimitsResult) -> dict:
    out: dict = {}
    if "directory_limits" in value:
        import capo_directory_service.types.directory_limits

        out["DirectoryLimits"] = (
            capo_directory_service.types.directory_limits.serialize_cbor(
                value["directory_limits"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetDirectoryLimitsResult:
    out: GetDirectoryLimitsResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryLimits") is not None:
        import capo_directory_service.types.directory_limits

        out["directory_limits"] = (
            capo_directory_service.types.directory_limits.deserialize_cbor(
                data["DirectoryLimits"]
            )
        )
    return out
