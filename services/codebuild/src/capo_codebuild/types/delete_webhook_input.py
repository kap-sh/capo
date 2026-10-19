"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteWebhookInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.project_name


class DeleteWebhookInput(TypedDict, closed=True):
    project_name: "capo_codebuild.types.project_name.ProjectName"
    """<p>The name of the CodeBuild project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWebhookInput) -> dict:
    out: dict = {}
    out["projectName"] = value["project_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWebhookInput:
    out: DeleteWebhookInput = {}  # type: ignore[typeddict-item]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        out["project_name"] = ""
    return out
