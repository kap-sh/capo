"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RepositoryAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.repository_head_source_code_type
    import capo_codeguru_reviewer.types.source_code_type


class RepositoryAnalysis(TypedDict, closed=True):
    repository_head: NotRequired[
        "capo_codeguru_reviewer.types.repository_head_source_code_type.RepositoryHeadSourceCodeType"
    ]
    """<p>A <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType">SourceCodeType</a> that specifies the tip of a branch in an associated repository.</p>"""
    source_code_type: NotRequired[
        "capo_codeguru_reviewer.types.source_code_type.SourceCodeType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryAnalysis) -> dict:
    out: dict = {}
    if "repository_head" in value:
        import capo_codeguru_reviewer.types.repository_head_source_code_type

        out["RepositoryHead"] = (
            capo_codeguru_reviewer.types.repository_head_source_code_type.serialize_json(
                value["repository_head"]
            )
        )
    if "source_code_type" in value:
        import capo_codeguru_reviewer.types.source_code_type

        out["SourceCodeType"] = (
            capo_codeguru_reviewer.types.source_code_type.serialize_json(
                value["source_code_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> RepositoryAnalysis:
    out: RepositoryAnalysis = {}  # type: ignore[typeddict-item]
    if data.get("RepositoryHead") is not None:
        import capo_codeguru_reviewer.types.repository_head_source_code_type

        out["repository_head"] = (
            capo_codeguru_reviewer.types.repository_head_source_code_type.deserialize_json(
                data["RepositoryHead"]
            )
        )
    if data.get("SourceCodeType") is not None:
        import capo_codeguru_reviewer.types.source_code_type

        out["source_code_type"] = (
            capo_codeguru_reviewer.types.source_code_type.deserialize_json(
                data["SourceCodeType"]
            )
        )
    return out
