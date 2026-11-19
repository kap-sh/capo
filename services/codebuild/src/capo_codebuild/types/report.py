"""Generated from Smithy shape ``com.amazonaws.codebuild#Report``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.code_coverage_report_summary
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.report_export_config
    import capo_codebuild.types.report_status_type
    import capo_codebuild.types.report_type
    import capo_codebuild.types.string
    import capo_codebuild.types.test_report_summary
    import capo_codebuild.types.timestamp
    import capo_codebuild.types.wrapper_boolean


class Report(TypedDict, closed=True):
    arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The ARN of the report run. </p>"""
    type: NotRequired["capo_codebuild.types.report_type.ReportType"]
    """<p>The type of the report that was run.</p> <dl> <dt>CODE_COVERAGE</dt> <dd> <p>A code coverage report.</p> </dd> <dt>TEST</dt> <dd> <p>A test report.</p> </dd> </dl>"""
    name: NotRequired["capo_codebuild.types.string.String"]
    """<p> The name of the report that was run. </p>"""
    report_group_arn: NotRequired[
        "capo_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ARN of the report group associated with this report. </p>"""
    execution_id: NotRequired["capo_codebuild.types.string.String"]
    """<p> The ARN of the build run that generated this report. </p>"""
    status: NotRequired["capo_codebuild.types.report_status_type.ReportStatusType"]
    """<p> The status of this report. </p>"""
    created: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p> The date and time this report run occurred. </p>"""
    expired: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p> The date and time a report expires. A report expires 30 days after it is created. An expired report is not available to view in CodeBuild. </p>"""
    export_config: NotRequired[
        "capo_codebuild.types.report_export_config.ReportExportConfig"
    ]
    """<p> Information about where the raw data used to generate this report was exported. </p>"""
    truncated: NotRequired["capo_codebuild.types.wrapper_boolean.WrapperBoolean"]
    """<p> A boolean that specifies if this report run is truncated. The list of test cases is truncated after the maximum number of test cases is reached. </p>"""
    test_summary: NotRequired[
        "capo_codebuild.types.test_report_summary.TestReportSummary"
    ]
    """<p> A <code>TestReportSummary</code> object that contains information about this test report. </p>"""
    code_coverage_summary: NotRequired[
        "capo_codebuild.types.code_coverage_report_summary.CodeCoverageReportSummary"
    ]
    """<p>A <code>CodeCoverageReportSummary</code> object that contains a code coverage summary for this report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Report) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        import capo_codebuild.types.report_type

        out["type"] = capo_codebuild.types.report_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "report_group_arn" in value:
        out["reportGroupArn"] = value["report_group_arn"]
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    if "status" in value:
        import capo_codebuild.types.report_status_type

        out["status"] = capo_codebuild.types.report_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    if "created" in value:
        import capo_codebuild.types.timestamp

        out["created"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "expired" in value:
        import capo_codebuild.types.timestamp

        out["expired"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["expired"]
        )
    if "export_config" in value:
        import capo_codebuild.types.report_export_config

        out["exportConfig"] = (
            capo_codebuild.types.report_export_config.serialize_aws_json_1_1(
                value["export_config"]
            )
        )
    if "truncated" in value:
        out["truncated"] = value["truncated"]
    if "test_summary" in value:
        import capo_codebuild.types.test_report_summary

        out["testSummary"] = (
            capo_codebuild.types.test_report_summary.serialize_aws_json_1_1(
                value["test_summary"]
            )
        )
    if "code_coverage_summary" in value:
        import capo_codebuild.types.code_coverage_report_summary

        out["codeCoverageSummary"] = (
            capo_codebuild.types.code_coverage_report_summary.serialize_aws_json_1_1(
                value["code_coverage_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Report:
    out: Report = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("type") is not None:
        import capo_codebuild.types.report_type

        out["type"] = capo_codebuild.types.report_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("reportGroupArn") is not None:
        out["report_group_arn"] = data["reportGroupArn"]
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    if data.get("status") is not None:
        import capo_codebuild.types.report_status_type

        out["status"] = (
            capo_codebuild.types.report_status_type.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("created") is not None:
        import capo_codebuild.types.timestamp

        out["created"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    if data.get("expired") is not None:
        import capo_codebuild.types.timestamp

        out["expired"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["expired"]
        )
    if data.get("exportConfig") is not None:
        import capo_codebuild.types.report_export_config

        out["export_config"] = (
            capo_codebuild.types.report_export_config.deserialize_aws_json_1_1(
                data["exportConfig"]
            )
        )
    if data.get("truncated") is not None:
        out["truncated"] = data["truncated"]
    if data.get("testSummary") is not None:
        import capo_codebuild.types.test_report_summary

        out["test_summary"] = (
            capo_codebuild.types.test_report_summary.deserialize_aws_json_1_1(
                data["testSummary"]
            )
        )
    if data.get("codeCoverageSummary") is not None:
        import capo_codebuild.types.code_coverage_report_summary

        out["code_coverage_summary"] = (
            capo_codebuild.types.code_coverage_report_summary.deserialize_aws_json_1_1(
                data["codeCoverageSummary"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Report) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        import capo_codebuild.types.report_type

        out["type"] = capo_codebuild.types.report_type.serialize_cbor(value["type"])
    if "name" in value:
        out["name"] = value["name"]
    if "report_group_arn" in value:
        out["reportGroupArn"] = value["report_group_arn"]
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    if "status" in value:
        import capo_codebuild.types.report_status_type

        out["status"] = capo_codebuild.types.report_status_type.serialize_cbor(
            value["status"]
        )
    if "created" in value:
        import capo_codebuild.types.timestamp

        out["created"] = capo_codebuild.types.timestamp.serialize_cbor(value["created"])
    if "expired" in value:
        import capo_codebuild.types.timestamp

        out["expired"] = capo_codebuild.types.timestamp.serialize_cbor(value["expired"])
    if "export_config" in value:
        import capo_codebuild.types.report_export_config

        out["exportConfig"] = capo_codebuild.types.report_export_config.serialize_cbor(
            value["export_config"]
        )
    if "truncated" in value:
        out["truncated"] = value["truncated"]
    if "test_summary" in value:
        import capo_codebuild.types.test_report_summary

        out["testSummary"] = capo_codebuild.types.test_report_summary.serialize_cbor(
            value["test_summary"]
        )
    if "code_coverage_summary" in value:
        import capo_codebuild.types.code_coverage_report_summary

        out["codeCoverageSummary"] = (
            capo_codebuild.types.code_coverage_report_summary.serialize_cbor(
                value["code_coverage_summary"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Report:
    out: Report = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("type") is not None:
        import capo_codebuild.types.report_type

        out["type"] = capo_codebuild.types.report_type.deserialize_cbor(data["type"])
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("reportGroupArn") is not None:
        out["report_group_arn"] = data["reportGroupArn"]
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    if data.get("status") is not None:
        import capo_codebuild.types.report_status_type

        out["status"] = capo_codebuild.types.report_status_type.deserialize_cbor(
            data["status"]
        )
    if data.get("created") is not None:
        import capo_codebuild.types.timestamp

        out["created"] = capo_codebuild.types.timestamp.deserialize_cbor(
            data["created"]
        )
    if data.get("expired") is not None:
        import capo_codebuild.types.timestamp

        out["expired"] = capo_codebuild.types.timestamp.deserialize_cbor(
            data["expired"]
        )
    if data.get("exportConfig") is not None:
        import capo_codebuild.types.report_export_config

        out["export_config"] = (
            capo_codebuild.types.report_export_config.deserialize_cbor(
                data["exportConfig"]
            )
        )
    if data.get("truncated") is not None:
        out["truncated"] = data["truncated"]
    if data.get("testSummary") is not None:
        import capo_codebuild.types.test_report_summary

        out["test_summary"] = capo_codebuild.types.test_report_summary.deserialize_cbor(
            data["testSummary"]
        )
    if data.get("codeCoverageSummary") is not None:
        import capo_codebuild.types.code_coverage_report_summary

        out["code_coverage_summary"] = (
            capo_codebuild.types.code_coverage_report_summary.deserialize_cbor(
                data["codeCoverageSummary"]
            )
        )
    return out
