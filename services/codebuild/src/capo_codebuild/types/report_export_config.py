"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportExportConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.report_export_config_type
    import capo_codebuild.types.s3_report_export_config


class ReportExportConfig(TypedDict, closed=True):
    export_config_type: NotRequired[
        "capo_codebuild.types.report_export_config_type.ReportExportConfigType"
    ]
    """<p> The export configuration type. Valid values are: </p> <ul> <li> <p> <code>S3</code>: The report results are exported to an S3 bucket. </p> </li> <li> <p> <code>NO_EXPORT</code>: The report results are not exported. </p> </li> </ul>"""
    s3_destination: NotRequired[
        "capo_codebuild.types.s3_report_export_config.S3ReportExportConfig"
    ]
    """<p> A <code>S3ReportExportConfig</code> object that contains information about the S3 bucket where the run of a report is exported. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportExportConfig) -> dict:
    out: dict = {}
    if "export_config_type" in value:
        import capo_codebuild.types.report_export_config_type

        out["exportConfigType"] = (
            capo_codebuild.types.report_export_config_type.serialize_aws_json_1_1(
                value["export_config_type"]
            )
        )
    if "s3_destination" in value:
        import capo_codebuild.types.s3_report_export_config

        out["s3Destination"] = (
            capo_codebuild.types.s3_report_export_config.serialize_aws_json_1_1(
                value["s3_destination"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportExportConfig:
    out: ReportExportConfig = {}  # type: ignore[typeddict-item]
    if data.get("exportConfigType") is not None:
        import capo_codebuild.types.report_export_config_type

        out["export_config_type"] = (
            capo_codebuild.types.report_export_config_type.deserialize_aws_json_1_1(
                data["exportConfigType"]
            )
        )
    if data.get("s3Destination") is not None:
        import capo_codebuild.types.s3_report_export_config

        out["s3_destination"] = (
            capo_codebuild.types.s3_report_export_config.deserialize_aws_json_1_1(
                data["s3Destination"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportExportConfig) -> dict:
    out: dict = {}
    if "export_config_type" in value:
        import capo_codebuild.types.report_export_config_type

        out["exportConfigType"] = (
            capo_codebuild.types.report_export_config_type.serialize_cbor(
                value["export_config_type"]
            )
        )
    if "s3_destination" in value:
        import capo_codebuild.types.s3_report_export_config

        out["s3Destination"] = (
            capo_codebuild.types.s3_report_export_config.serialize_cbor(
                value["s3_destination"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ReportExportConfig:
    out: ReportExportConfig = {}  # type: ignore[typeddict-item]
    if data.get("exportConfigType") is not None:
        import capo_codebuild.types.report_export_config_type

        out["export_config_type"] = (
            capo_codebuild.types.report_export_config_type.deserialize_cbor(
                data["exportConfigType"]
            )
        )
    if data.get("s3Destination") is not None:
        import capo_codebuild.types.s3_report_export_config

        out["s3_destination"] = (
            capo_codebuild.types.s3_report_export_config.deserialize_cbor(
                data["s3Destination"]
            )
        )
    return out
