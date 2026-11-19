"""Generated from Smithy shape ``com.amazonaws.datasync#ReportDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.report_destination_s3


class ReportDestination(TypedDict, closed=True):
    s3: NotRequired["capo_datasync.types.report_destination_s3.ReportDestinationS3"]
    """<p>Specifies the Amazon S3 bucket where DataSync uploads your task report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportDestination) -> dict:
    out: dict = {}
    if "s3" in value:
        import capo_datasync.types.report_destination_s3

        out["S3"] = capo_datasync.types.report_destination_s3.serialize_aws_json_1_1(
            value["s3"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportDestination:
    out: ReportDestination = {}  # type: ignore[typeddict-item]
    if data.get("S3") is not None:
        import capo_datasync.types.report_destination_s3

        out["s3"] = capo_datasync.types.report_destination_s3.deserialize_aws_json_1_1(
            data["S3"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportDestination) -> dict:
    out: dict = {}
    if "s3" in value:
        import capo_datasync.types.report_destination_s3

        out["S3"] = capo_datasync.types.report_destination_s3.serialize_cbor(
            value["s3"]
        )
    return out


def deserialize_cbor(data: dict) -> ReportDestination:
    out: ReportDestination = {}  # type: ignore[typeddict-item]
    if data.get("S3") is not None:
        import capo_datasync.types.report_destination_s3

        out["s3"] = capo_datasync.types.report_destination_s3.deserialize_cbor(
            data["S3"]
        )
    return out
