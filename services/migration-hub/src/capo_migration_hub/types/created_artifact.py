"""Generated from Smithy shape ``com.amazonaws.migrationhub#CreatedArtifact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.created_artifact_description
    import capo_migration_hub.types.created_artifact_name


class CreatedArtifact(TypedDict, closed=True):
    name: "capo_migration_hub.types.created_artifact_name.CreatedArtifactName"
    """<p>An ARN that uniquely identifies the result of a migration task.</p>"""
    description: NotRequired[
        "capo_migration_hub.types.created_artifact_description.CreatedArtifactDescription"
    ]
    """<p>A description that can be free-form text to record additional detail about the artifact for clarity or for later reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatedArtifact) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatedArtifact:
    out: CreatedArtifact = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
