"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#CodeReviewType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeguru_reviewer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.analysis_types
    import capo_codeguru_reviewer.types.repository_analysis


class CodeReviewType(TypedDict, closed=True):
    repository_analysis: (
        "capo_codeguru_reviewer.types.repository_analysis.RepositoryAnalysis"
    )
    """<p>A code review that analyzes all code under a specified branch in an associated repository. The associated repository is specified using its ARN in <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReview">CreateCodeReview</a>.</p>"""
    analysis_types: NotRequired[
        "capo_codeguru_reviewer.types.analysis_types.AnalysisTypes"
    ]
    """<p>They types of analysis performed during a repository analysis or a pull request review. You can specify either <code>Security</code>, <code>CodeQuality</code>, or both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewType) -> dict:
    out: dict = {}
    import capo_codeguru_reviewer.types.repository_analysis

    out["RepositoryAnalysis"] = (
        capo_codeguru_reviewer.types.repository_analysis.serialize_json(
            value["repository_analysis"]
        )
    )
    if "analysis_types" in value:
        import capo_codeguru_reviewer.types.analysis_types

        out["AnalysisTypes"] = (
            capo_codeguru_reviewer.types.analysis_types.serialize_json(
                value["analysis_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodeReviewType:
    out: CodeReviewType = {}  # type: ignore[typeddict-item]
    if data.get("RepositoryAnalysis") is not None:
        import capo_codeguru_reviewer.types.repository_analysis

        out["repository_analysis"] = (
            capo_codeguru_reviewer.types.repository_analysis.deserialize_json(
                data["RepositoryAnalysis"]
            )
        )
    else:
        raise DeserializationError("CodeReviewType.repository_analysis required")
    if data.get("AnalysisTypes") is not None:
        import capo_codeguru_reviewer.types.analysis_types

        out["analysis_types"] = (
            capo_codeguru_reviewer.types.analysis_types.deserialize_json(
                data["AnalysisTypes"]
            )
        )
    return out
