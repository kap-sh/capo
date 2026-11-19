"""Generated from Smithy shape ``com.amazonaws.codebuild#CodeCoverageReportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_negative_int
    import capo_codebuild.types.percentage


class CodeCoverageReportSummary(TypedDict, closed=True):
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeCoverageReportSummary) -> dict:
    out: dict = {}
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeCoverageReportSummary:
    out: CodeCoverageReportSummary = {}  # type: ignore[typeddict-item]
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
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CodeCoverageReportSummary) -> dict:
    out: dict = {}
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
    return out


def deserialize_cbor(data: dict) -> CodeCoverageReportSummary:
    out: CodeCoverageReportSummary = {}  # type: ignore[typeddict-item]
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
    return out
