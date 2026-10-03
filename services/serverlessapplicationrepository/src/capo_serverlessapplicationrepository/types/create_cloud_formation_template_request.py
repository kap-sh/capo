"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#CreateCloudFormationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__string


class CreateCloudFormationTemplateRequest(TypedDict, closed=True):
    application_id: "capo_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    semantic_version: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The semantic version of the application:</p><p> <a href="https://semver.org/">https://semver.org/</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCloudFormationTemplateRequest) -> dict:
    out: dict = {}
    if "semantic_version" in value:
        out["semanticVersion"] = value["semantic_version"]
    return out


def deserialize_json(data: dict) -> CreateCloudFormationTemplateRequest:
    out: CreateCloudFormationTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("semanticVersion") is not None:
        out["semantic_version"] = data["semanticVersion"]
    return out
