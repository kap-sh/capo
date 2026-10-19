"""Generated from Smithy shape ``com.amazonaws.databrew#CreateProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.arn
    import capo_databrew.types.dataset_name
    import capo_databrew.types.project_name
    import capo_databrew.types.recipe_name
    import capo_databrew.types.sample
    import capo_databrew.types.tag_map


class CreateProjectRequest(TypedDict, closed=True):
    dataset_name: "capo_databrew.types.dataset_name.DatasetName"
    """<p>The name of an existing dataset to associate this project with.</p>"""
    name: "capo_databrew.types.project_name.ProjectName"
    """<p>A unique name for the new project. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>"""
    recipe_name: "capo_databrew.types.recipe_name.RecipeName"
    """<p>The name of an existing recipe to associate with the project.</p>"""
    sample: NotRequired["capo_databrew.types.sample.Sample"]
    role_arn: "capo_databrew.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role to be assumed for this request.</p>"""
    tags: NotRequired["capo_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags to apply to this project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectRequest) -> dict:
    out: dict = {}
    out["DatasetName"] = value["dataset_name"]
    out["Name"] = value["name"]
    out["RecipeName"] = value["recipe_name"]
    if "sample" in value:
        import capo_databrew.types.sample

        out["Sample"] = capo_databrew.types.sample.serialize_json(value["sample"])
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_databrew.types.tag_map

        out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateProjectRequest:
    out: CreateProjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    else:
        out["dataset_name"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RecipeName") is not None:
        out["recipe_name"] = data["RecipeName"]
    else:
        out["recipe_name"] = ""
    if data.get("Sample") is not None:
        import capo_databrew.types.sample

        out["sample"] = capo_databrew.types.sample.deserialize_json(data["Sample"])
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("Tags") is not None:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    return out
