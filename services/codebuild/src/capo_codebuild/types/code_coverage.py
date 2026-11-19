"""Generated from Smithy shape ``com.amazonaws.codebuild#CodeCoverage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.non_negative_int
    import capo_codebuild.types.percentage
    import capo_codebuild.types.timestamp


class CodeCoverage(TypedDict, closed=True):
    id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the code coverage report.</p>"""
    report_arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the report.</p>"""
    file_path: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The path of the test report file.</p>"""
    line_coverage_percentage: NotRequired["capo_codebuild.types.percentage.Percentage"]
    """<p>The percentage of lines that are covered by your tests.</p>"""
    lines_covered: NotRequired["capo_codebuild.types.non_negative_int.NonNegativeInt"]
    """<p>The number of lines that are covered by your tests.</p>"""
    lines_missed: NotRequired["capo_codebuild.types.non_negative_int.NonNegativeInt"]
    """<p>The number of lines that are not covered by your tests.</p>"""
    branch_coverage_percentage: NotRequired[
        "capo_codebuild.types.percentage.Percentage"
    ]
    """<p>The percentage of branches that are covered by your tests.</p>"""
    branches_covered: NotRequired[
        "capo_codebuild.types.non_negative_int.NonNegativeInt"
    ]
    """<p>The number of conditional branches that are covered by your tests.</p>"""
    branches_missed: NotRequired["capo_codebuild.types.non_negative_int.NonNegativeInt"]
    """<p>The number of conditional branches that are not covered by your tests.</p>"""
    expired: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>The date and time that the tests were run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeCoverage) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "report_arn" in value:
        out["reportARN"] = value["report_arn"]
    if "file_path" in value:
        out["filePath"] = value["file_path"]
    if "line_coverage_percentage" in value:
        out["lineCoveragePercentage"] = (
            "NaN"
            if value["line_coverage_percentage"] != value["line_coverage_percentage"]
            else "Infinity"
            if value["line_coverage_percentage"] == float("inf")
            else "-Infinity"
            if value["line_coverage_percentage"] == float("-inf")
            else value["line_coverage_percentage"]
        )
    if "lines_covered" in value:
        out["linesCovered"] = value["lines_covered"]
    if "lines_missed" in value:
        out["linesMissed"] = value["lines_missed"]
    if "branch_coverage_percentage" in value:
        out["branchCoveragePercentage"] = (
            "NaN"
            if value["branch_coverage_percentage"]
            != value["branch_coverage_percentage"]
            else "Infinity"
            if value["branch_coverage_percentage"] == float("inf")
            else "-Infinity"
            if value["branch_coverage_percentage"] == float("-inf")
            else value["branch_coverage_percentage"]
        )
    if "branches_covered" in value:
        out["branchesCovered"] = value["branches_covered"]
    if "branches_missed" in value:
        out["branchesMissed"] = value["branches_missed"]
    if "expired" in value:
        import capo_codebuild.types.timestamp

        out["expired"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["expired"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeCoverage:
    out: CodeCoverage = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("reportARN") is not None:
        out["report_arn"] = data["reportARN"]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    if data.get("lineCoveragePercentage") is not None:
        out["line_coverage_percentage"] = float(data["lineCoveragePercentage"])
    if data.get("linesCovered") is not None:
        out["lines_covered"] = data["linesCovered"]
    if data.get("linesMissed") is not None:
        out["lines_missed"] = data["linesMissed"]
    if data.get("branchCoveragePercentage") is not None:
        out["branch_coverage_percentage"] = float(data["branchCoveragePercentage"])
    if data.get("branchesCovered") is not None:
        out["branches_covered"] = data["branchesCovered"]
    if data.get("branchesMissed") is not None:
        out["branches_missed"] = data["branchesMissed"]
    if data.get("expired") is not None:
        import capo_codebuild.types.timestamp

        out["expired"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["expired"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CodeCoverage) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "report_arn" in value:
        out["reportARN"] = value["report_arn"]
    if "file_path" in value:
        out["filePath"] = value["file_path"]
    if "line_coverage_percentage" in value:
        out["lineCoveragePercentage"] = value["line_coverage_percentage"]
    if "lines_covered" in value:
        out["linesCovered"] = value["lines_covered"]
    if "lines_missed" in value:
        out["linesMissed"] = value["lines_missed"]
    if "branch_coverage_percentage" in value:
        out["branchCoveragePercentage"] = value["branch_coverage_percentage"]
    if "branches_covered" in value:
        out["branchesCovered"] = value["branches_covered"]
    if "branches_missed" in value:
        out["branchesMissed"] = value["branches_missed"]
    if "expired" in value:
        import capo_codebuild.types.timestamp

        out["expired"] = capo_codebuild.types.timestamp.serialize_cbor(value["expired"])
    return out


def deserialize_cbor(data: dict) -> CodeCoverage:
    out: CodeCoverage = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("reportARN") is not None:
        out["report_arn"] = data["reportARN"]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    if data.get("lineCoveragePercentage") is not None:
        out["line_coverage_percentage"] = float(data["lineCoveragePercentage"])
    if data.get("linesCovered") is not None:
        out["lines_covered"] = data["linesCovered"]
    if data.get("linesMissed") is not None:
        out["lines_missed"] = data["linesMissed"]
    if data.get("branchCoveragePercentage") is not None:
        out["branch_coverage_percentage"] = float(data["branchCoveragePercentage"])
    if data.get("branchesCovered") is not None:
        out["branches_covered"] = data["branchesCovered"]
    if data.get("branchesMissed") is not None:
        out["branches_missed"] = data["branchesMissed"]
    if data.get("expired") is not None:
        import capo_codebuild.types.timestamp

        out["expired"] = capo_codebuild.types.timestamp.deserialize_cbor(
            data["expired"]
        )
    return out
