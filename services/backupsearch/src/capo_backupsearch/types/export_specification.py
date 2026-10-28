"""Generated from Smithy shape ``com.amazonaws.backupsearch#ExportSpecification``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_backupsearch.errors import DeserializationError, SerializationError
from capo_backupsearch.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_backupsearch.types.s3_export_specification


class ExportSpecificationS3ExportSpecificationMember(TypedDict, closed=True):
    s3ExportSpecification: (
        "capo_backupsearch.types.s3_export_specification.S3ExportSpecification"
    )


ExportSpecification: TypeAlias = (
    ExportSpecificationS3ExportSpecificationMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ExportSpecification) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ExportSpecification: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3ExportSpecification" in value:
        import capo_backupsearch.types.s3_export_specification

        return {
            "s3ExportSpecification": capo_backupsearch.types.s3_export_specification.serialize_json(
                value["s3ExportSpecification"]
            )
        }
    else:
        raise SerializationError("ExportSpecification: no variant present")


def deserialize_json(data: dict) -> ExportSpecification:
    if data.get("s3ExportSpecification") is not None:
        import capo_backupsearch.types.s3_export_specification

        return {
            "s3ExportSpecification": capo_backupsearch.types.s3_export_specification.deserialize_json(
                data["s3ExportSpecification"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ExportSpecification: no recognized variant key")
