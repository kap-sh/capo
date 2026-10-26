"""Generated from Smithy shape ``com.amazonaws.mailmanager#ExportDestinationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.s3_export_destination_configuration


class _ExportDestinationConfiguration_S3(TypedDict, closed=True):
    S3: "capo_mailmanager.types.s3_export_destination_configuration.S3ExportDestinationConfiguration"


ExportDestinationConfiguration: TypeAlias = (
    _ExportDestinationConfiguration_S3 | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportDestinationConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ExportDestinationConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "S3" in value:
        import capo_mailmanager.types.s3_export_destination_configuration

        return {
            "S3": capo_mailmanager.types.s3_export_destination_configuration.serialize_aws_json_1_0(
                value["S3"]
            )
        }
    else:
        raise SerializationError("ExportDestinationConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ExportDestinationConfiguration:
    if data.get("S3") is not None:
        import capo_mailmanager.types.s3_export_destination_configuration

        return {
            "S3": capo_mailmanager.types.s3_export_destination_configuration.deserialize_aws_json_1_0(
                data["S3"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ExportDestinationConfiguration: no recognized variant key"
        )
