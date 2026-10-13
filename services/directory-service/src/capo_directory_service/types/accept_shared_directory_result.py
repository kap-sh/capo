"""Generated from Smithy shape ``com.amazonaws.directoryservice#AcceptSharedDirectoryResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.shared_directory


class AcceptSharedDirectoryResult(TypedDict, closed=True):
    shared_directory: NotRequired[
        "capo_directory_service.types.shared_directory.SharedDirectory"
    ]
    """<p>The shared directory in the directory consumer account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptSharedDirectoryResult) -> dict:
    out: dict = {}
    if "shared_directory" in value:
        import capo_directory_service.types.shared_directory

        out["SharedDirectory"] = (
            capo_directory_service.types.shared_directory.serialize_aws_json_1_1(
                value["shared_directory"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceptSharedDirectoryResult:
    out: AcceptSharedDirectoryResult = {}  # type: ignore[typeddict-item]
    if data.get("SharedDirectory") is not None:
        import capo_directory_service.types.shared_directory

        out["shared_directory"] = (
            capo_directory_service.types.shared_directory.deserialize_aws_json_1_1(
                data["SharedDirectory"]
            )
        )
    return out


def redact_sensitive(value: AcceptSharedDirectoryResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "shared_directory" in value:
        import capo_directory_service.types.shared_directory

        out["shared_directory"] = (
            capo_directory_service.types.shared_directory.redact_sensitive(
                value["shared_directory"]
            )
        )
    return out
