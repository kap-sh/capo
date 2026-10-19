"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.arn
    import capo_databrew.types.project_name
    import capo_databrew.types.sample


class UpdateProjectRequest(TypedDict, closed=True):
    sample: NotRequired["capo_databrew.types.sample.Sample"]
    role_arn: "capo_databrew.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to be assumed for this request.</p>"""
    name: "capo_databrew.types.project_name.ProjectName"
    """<p>The name of the project to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProjectRequest) -> dict:
    out: dict = {}
    if "sample" in value:
        import capo_databrew.types.sample

        out["Sample"] = capo_databrew.types.sample.serialize_json(value["sample"])
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateProjectRequest:
    out: UpdateProjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("Sample") is not None:
        import capo_databrew.types.sample

        out["sample"] = capo_databrew.types.sample.deserialize_json(data["Sample"])
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    return out
