"""Generated from Smithy shape ``com.amazonaws.securityhub#ExportDestination``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.s3_export_destination


class ExportDestinationS3Member(TypedDict, closed=True):
    S3: "capo_securityhub.types.s3_export_destination.S3ExportDestination"


ExportDestination: TypeAlias = ExportDestinationS3Member | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ExportDestination) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ExportDestination: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "S3" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ExportDestination: no recognized variant key")
