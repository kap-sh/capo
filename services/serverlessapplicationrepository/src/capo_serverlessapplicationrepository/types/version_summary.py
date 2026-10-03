"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#VersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__string


class VersionSummary(TypedDict, closed=True):
    application_id: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The application Amazon Resource Name (ARN).</p>"""
    creation_time: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The date and time this resource was created.</p>"""
    semantic_version: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The semantic version of the application:</p><p> <a href="https://semver.org/">https://semver.org/</a> </p>"""
    source_code_url: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionSummary) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "semantic_version" in value:
        out["semanticVersion"] = value["semantic_version"]
    if "source_code_url" in value:
        out["sourceCodeUrl"] = value["source_code_url"]
    return out


def deserialize_json(data: dict) -> VersionSummary:
    out: VersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    if data.get("creationTime") is not None:
        out["creation_time"] = data["creationTime"]
    if data.get("semanticVersion") is not None:
        out["semantic_version"] = data["semanticVersion"]
    if data.get("sourceCodeUrl") is not None:
        out["source_code_url"] = data["sourceCodeUrl"]
    return out
