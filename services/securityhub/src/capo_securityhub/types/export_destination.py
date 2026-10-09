"""Generated from Smithy shape ``com.amazonaws.securityhub#ExportDestination``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityhub.types.s3_export_destination


class _ExportDestination_S3(TypedDict, closed=True):
    S3: "capo_securityhub.types.s3_export_destination.S3ExportDestination"


ExportDestination: TypeAlias = _ExportDestination_S3


# --- restJson1 ser/de ---
def serialize_json(value: ExportDestination) -> dict:
    if "S3" in value:
        import capo_securityhub.types.s3_export_destination

        return {
            "S3": capo_securityhub.types.s3_export_destination.serialize_json(
                value["S3"]
            )
        }
    else:
        raise SerializationError("ExportDestination: no variant present")


def deserialize_json(data: dict) -> ExportDestination:
    if data.get("S3") is not None:
        import capo_securityhub.types.s3_export_destination

        return {
            "S3": capo_securityhub.types.s3_export_destination.deserialize_json(
                data["S3"]
            )
        }
    else:
        raise DeserializationError("ExportDestination: no recognized variant key")
