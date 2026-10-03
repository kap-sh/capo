"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#CreateCloudFormationChangeSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__string


class CreateCloudFormationChangeSetResponse(TypedDict, closed=True):
    application_id: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The application Amazon Resource Name (ARN).</p>"""
    change_set_id: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the change set.</p><p>Length constraints: Minimum length of 1.</p><p>Pattern: ARN:[-a-zA-Z0-9:/]*</p>"""
    semantic_version: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The semantic version of the application:</p><p> <a href="https://semver.org/">https://semver.org/</a> </p>"""
    stack_id: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The unique ID of the stack.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCloudFormationChangeSetResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "change_set_id" in value:
        out["changeSetId"] = value["change_set_id"]
    if "semantic_version" in value:
        out["semanticVersion"] = value["semantic_version"]
    if "stack_id" in value:
        out["stackId"] = value["stack_id"]
    return out


def deserialize_json(data: dict) -> CreateCloudFormationChangeSetResponse:
    out: CreateCloudFormationChangeSetResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    if data.get("changeSetId") is not None:
        out["change_set_id"] = data["changeSetId"]
    if data.get("semanticVersion") is not None:
        out["semantic_version"] = data["semanticVersion"]
    if data.get("stackId") is not None:
        out["stack_id"] = data["stackId"]
    return out
