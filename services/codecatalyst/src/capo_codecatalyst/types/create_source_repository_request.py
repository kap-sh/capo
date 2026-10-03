"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CreateSourceRepositoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.source_repository_description_string
    import capo_codecatalyst.types.source_repository_name_string


class CreateSourceRepositoryRequest(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    name: "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    """<p>The name of the source repository. For more information about name requirements, see <a href="https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-quotas.html">Quotas for source repositories</a>.</p>"""
    description: NotRequired[
        "capo_codecatalyst.types.source_repository_description_string.SourceRepositoryDescriptionString"
    ]
    """<p>The description of the source repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSourceRepositoryRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateSourceRepositoryRequest:
    out: CreateSourceRepositoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
