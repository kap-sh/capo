"""Generated from Smithy shape ``com.amazonaws.ssm#GcpProject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.gcp_project_display_name
    import capo_ssm.types.gcp_project_id


class GcpProject(TypedDict, closed=True):
    project_id: "capo_ssm.types.gcp_project_id.GcpProjectId"
    """<p>The ID of the GCP project.</p>"""
    project_display_name: NotRequired[
        "capo_ssm.types.gcp_project_display_name.GcpProjectDisplayName"
    ]
    """<p>The display name of the GCP project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GcpProject) -> dict:
    out: dict = {}
    out["ProjectId"] = value["project_id"]
    if "project_display_name" in value:
        out["ProjectDisplayName"] = value["project_display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GcpProject:
    out: GcpProject = {}  # type: ignore[typeddict-item]
    if data.get("ProjectId") is not None:
        out["project_id"] = data["ProjectId"]
    else:
        out["project_id"] = ""
    if data.get("ProjectDisplayName") is not None:
        out["project_display_name"] = data["ProjectDisplayName"]
    return out
