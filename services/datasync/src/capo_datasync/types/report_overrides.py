"""Generated from Smithy shape ``com.amazonaws.datasync#ReportOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.report_override


class ReportOverrides(TypedDict, closed=True):
    transferred: NotRequired["capo_datasync.types.report_override.ReportOverride"]
    """<p>Specifies the level of reporting for the files, objects, and directories that DataSync attempted to transfer.</p>"""
    verified: NotRequired["capo_datasync.types.report_override.ReportOverride"]
    """<p>Specifies the level of reporting for the files, objects, and directories that DataSync attempted to verify at the end of your transfer.</p>"""
    deleted: NotRequired["capo_datasync.types.report_override.ReportOverride"]
    """<p>Specifies the level of reporting for the files, objects, and directories that DataSync attempted to delete in your destination location. This only applies if you <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html">configure your task</a> to delete data in the destination that isn't in the source.</p>"""
    skipped: NotRequired["capo_datasync.types.report_override.ReportOverride"]
    """<p>Specifies the level of reporting for the files, objects, and directories that DataSync attempted to skip during your transfer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportOverrides) -> dict:
    out: dict = {}
    if "transferred" in value:
        import capo_datasync.types.report_override

        out["Transferred"] = capo_datasync.types.report_override.serialize_aws_json_1_1(
            value["transferred"]
        )
    if "verified" in value:
        import capo_datasync.types.report_override

        out["Verified"] = capo_datasync.types.report_override.serialize_aws_json_1_1(
            value["verified"]
        )
    if "deleted" in value:
        import capo_datasync.types.report_override

        out["Deleted"] = capo_datasync.types.report_override.serialize_aws_json_1_1(
            value["deleted"]
        )
    if "skipped" in value:
        import capo_datasync.types.report_override

        out["Skipped"] = capo_datasync.types.report_override.serialize_aws_json_1_1(
            value["skipped"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportOverrides:
    out: ReportOverrides = {}  # type: ignore[typeddict-item]
    if data.get("Transferred") is not None:
        import capo_datasync.types.report_override

        out["transferred"] = (
            capo_datasync.types.report_override.deserialize_aws_json_1_1(
                data["Transferred"]
            )
        )
    if data.get("Verified") is not None:
        import capo_datasync.types.report_override

        out["verified"] = capo_datasync.types.report_override.deserialize_aws_json_1_1(
            data["Verified"]
        )
    if data.get("Deleted") is not None:
        import capo_datasync.types.report_override

        out["deleted"] = capo_datasync.types.report_override.deserialize_aws_json_1_1(
            data["Deleted"]
        )
    if data.get("Skipped") is not None:
        import capo_datasync.types.report_override

        out["skipped"] = capo_datasync.types.report_override.deserialize_aws_json_1_1(
            data["Skipped"]
        )
    return out
