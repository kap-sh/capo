"""Generated from Smithy shape ``com.amazonaws.elementalinference#QuestionSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.question_set_arn
    import capo_elementalinference.types.question_set_id
    import capo_elementalinference.types.question_set_version
    import capo_elementalinference.types.resource_name


class QuestionSetSummary(TypedDict, closed=True):
    arn: "capo_elementalinference.types.question_set_arn.QuestionSetArn"
    """<p>The ARN of the question set.</p>"""
    id: "capo_elementalinference.types.question_set_id.QuestionSetId"
    """<p>The ID of the question set.</p>"""
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the question set.</p>"""
    latest_version: NotRequired[
        "capo_elementalinference.types.question_set_version.QuestionSetVersion"
    ]
    """<p>The number of the highest version that you have published for this question set, even if you have since deleted that version. Elemental Inference doesn't return this property if you haven't published a version. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuestionSetSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "latest_version" in value:
        out["latestVersion"] = value["latest_version"]
    return out


def deserialize_json(data: dict) -> QuestionSetSummary:
    out: QuestionSetSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("latestVersion") is not None:
        out["latest_version"] = data["latestVersion"]
    return out
