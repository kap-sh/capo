"""Generated from Smithy shape ``com.amazonaws.codebuild#GetReportGroupTrendOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.report_group_trend_raw_data_list
    import capo_codebuild.types.report_group_trend_stats


class GetReportGroupTrendOutput(TypedDict, closed=True):
    stats: NotRequired[
        "capo_codebuild.types.report_group_trend_stats.ReportGroupTrendStats"
    ]
    """<p>Contains the accumulated trend data.</p>"""
    raw_data: NotRequired[
        "capo_codebuild.types.report_group_trend_raw_data_list.ReportGroupTrendRawDataList"
    ]
    """<p>An array that contains the raw data for each report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReportGroupTrendOutput) -> dict:
    out: dict = {}
    if "stats" in value:
        import capo_codebuild.types.report_group_trend_stats

        out["stats"] = (
            capo_codebuild.types.report_group_trend_stats.serialize_aws_json_1_1(
                value["stats"]
            )
        )
    if "raw_data" in value:
        import capo_codebuild.types.report_group_trend_raw_data_list

        out["rawData"] = (
            capo_codebuild.types.report_group_trend_raw_data_list.serialize_aws_json_1_1(
                value["raw_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReportGroupTrendOutput:
    out: GetReportGroupTrendOutput = {}  # type: ignore[typeddict-item]
    if data.get("stats") is not None:
        import capo_codebuild.types.report_group_trend_stats

        out["stats"] = (
            capo_codebuild.types.report_group_trend_stats.deserialize_aws_json_1_1(
                data["stats"]
            )
        )
    if data.get("rawData") is not None:
        import capo_codebuild.types.report_group_trend_raw_data_list

        out["raw_data"] = (
            capo_codebuild.types.report_group_trend_raw_data_list.deserialize_aws_json_1_1(
                data["rawData"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetReportGroupTrendOutput) -> dict:
    out: dict = {}
    if "stats" in value:
        import capo_codebuild.types.report_group_trend_stats

        out["stats"] = capo_codebuild.types.report_group_trend_stats.serialize_cbor(
            value["stats"]
        )
    if "raw_data" in value:
        import capo_codebuild.types.report_group_trend_raw_data_list

        out["rawData"] = (
            capo_codebuild.types.report_group_trend_raw_data_list.serialize_cbor(
                value["raw_data"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetReportGroupTrendOutput:
    out: GetReportGroupTrendOutput = {}  # type: ignore[typeddict-item]
    if data.get("stats") is not None:
        import capo_codebuild.types.report_group_trend_stats

        out["stats"] = capo_codebuild.types.report_group_trend_stats.deserialize_cbor(
            data["stats"]
        )
    if data.get("rawData") is not None:
        import capo_codebuild.types.report_group_trend_raw_data_list

        out["raw_data"] = (
            capo_codebuild.types.report_group_trend_raw_data_list.deserialize_cbor(
                data["rawData"]
            )
        )
    return out
