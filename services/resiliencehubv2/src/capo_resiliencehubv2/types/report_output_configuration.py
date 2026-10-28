"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ReportOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError
from capo_resiliencehubv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.s3_report_output_configuration


class ReportOutputConfigurationS3Member(TypedDict, closed=True):
    s3: "capo_resiliencehubv2.types.s3_report_output_configuration.S3ReportOutputConfiguration"


ReportOutputConfiguration: TypeAlias = (
    ReportOutputConfigurationS3Member | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ReportOutputConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ReportOutputConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_resiliencehubv2.types.s3_report_output_configuration

        return {
            "s3": capo_resiliencehubv2.types.s3_report_output_configuration.serialize_json(
                value["s3"]
            )
        }
    else:
        raise SerializationError("ReportOutputConfiguration: no variant present")


def deserialize_json(data: dict) -> ReportOutputConfiguration:
    if data.get("s3") is not None:
        import capo_resiliencehubv2.types.s3_report_output_configuration

        return {
            "s3": capo_resiliencehubv2.types.s3_report_output_configuration.deserialize_json(
                data["s3"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ReportOutputConfiguration: no recognized variant key"
        )
