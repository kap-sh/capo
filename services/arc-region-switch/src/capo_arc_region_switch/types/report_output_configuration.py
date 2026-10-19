"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ReportOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_arc_region_switch.errors import DeserializationError, SerializationError
from capo_arc_region_switch.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_arc_region_switch.types.s3_report_output_configuration


class _ReportOutputConfiguration_s3Configuration(TypedDict, closed=True):
    s3Configuration: "capo_arc_region_switch.types.s3_report_output_configuration.S3ReportOutputConfiguration"


ReportOutputConfiguration: TypeAlias = (
    _ReportOutputConfiguration_s3Configuration | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReportOutputConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ReportOutputConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "s3Configuration" in value:
        import capo_arc_region_switch.types.s3_report_output_configuration

        return {
            "s3Configuration": capo_arc_region_switch.types.s3_report_output_configuration.serialize_aws_json_1_0(
                value["s3Configuration"]
            )
        }
    else:
        raise SerializationError("ReportOutputConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ReportOutputConfiguration:
    if data.get("s3Configuration") is not None:
        import capo_arc_region_switch.types.s3_report_output_configuration

        return {
            "s3Configuration": capo_arc_region_switch.types.s3_report_output_configuration.deserialize_aws_json_1_0(
                data["s3Configuration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "ReportOutputConfiguration: no recognized variant key"
        )
