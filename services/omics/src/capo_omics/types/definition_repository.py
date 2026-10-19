"""Generated from Smithy shape ``com.amazonaws.omics#DefinitionRepository``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.connection_arn
    import capo_omics.types.exclude_file_pattern_list
    import capo_omics.types.full_repository_id
    import capo_omics.types.source_reference


class DefinitionRepository(TypedDict, closed=True):
    connection_arn: "capo_omics.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of the connection to the source code repository.</p>"""
    full_repository_id: "capo_omics.types.full_repository_id.FullRepositoryId"
    """<p>The full repository identifier, including the repository owner and name. For example, 'repository-owner/repository-name'.</p>"""
    source_reference: NotRequired["capo_omics.types.source_reference.SourceReference"]
    """<p>The source reference for the repository, such as a branch name, tag, or commit ID.</p>"""
    exclude_file_patterns: NotRequired[
        "capo_omics.types.exclude_file_pattern_list.ExcludeFilePatternList"
    ]
    """<p>A list of file patterns to exclude when retrieving the workflow definition from the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefinitionRepository) -> dict:
    out: dict = {}
    out["connectionArn"] = value["connection_arn"]
    out["fullRepositoryId"] = value["full_repository_id"]
    if "source_reference" in value:
        import capo_omics.types.source_reference

        out["sourceReference"] = capo_omics.types.source_reference.serialize_json(
            value["source_reference"]
        )
    if "exclude_file_patterns" in value:
        import capo_omics.types.exclude_file_pattern_list

        out["excludeFilePatterns"] = (
            capo_omics.types.exclude_file_pattern_list.serialize_json(
                value["exclude_file_patterns"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefinitionRepository:
    out: DefinitionRepository = {}  # type: ignore[typeddict-item]
    if data.get("connectionArn") is not None:
        out["connection_arn"] = data["connectionArn"]
    else:
        out["connection_arn"] = ""
    if data.get("fullRepositoryId") is not None:
        out["full_repository_id"] = data["fullRepositoryId"]
    else:
        out["full_repository_id"] = ""
    if data.get("sourceReference") is not None:
        import capo_omics.types.source_reference

        out["source_reference"] = capo_omics.types.source_reference.deserialize_json(
            data["sourceReference"]
        )
    if data.get("excludeFilePatterns") is not None:
        import capo_omics.types.exclude_file_pattern_list

        out["exclude_file_patterns"] = (
            capo_omics.types.exclude_file_pattern_list.deserialize_json(
                data["excludeFilePatterns"]
            )
        )
    return out
