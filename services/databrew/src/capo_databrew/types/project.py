"""Generated from Smithy shape ``com.amazonaws.databrew#Project``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.account_id
    import capo_databrew.types.arn
    import capo_databrew.types.created_by
    import capo_databrew.types.dataset_name
    import capo_databrew.types.date
    import capo_databrew.types.last_modified_by
    import capo_databrew.types.opened_by
    import capo_databrew.types.project_name
    import capo_databrew.types.recipe_name
    import capo_databrew.types.sample
    import capo_databrew.types.tag_map


class Project(TypedDict, closed=True):
    account_id: NotRequired["capo_databrew.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account that owns the project.</p>"""
    create_date: NotRequired["capo_databrew.types.date.Date"]
    """<p>The date and time that the project was created.</p>"""
    created_by: NotRequired["capo_databrew.types.created_by.CreatedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who crated the project.</p>"""
    dataset_name: NotRequired["capo_databrew.types.dataset_name.DatasetName"]
    """<p>The dataset that the project is to act upon.</p>"""
    last_modified_date: NotRequired["capo_databrew.types.date.Date"]
    """<p>The last modification date and time for the project.</p>"""
    last_modified_by: NotRequired["capo_databrew.types.last_modified_by.LastModifiedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who last modified the project.</p>"""
    name: "capo_databrew.types.project_name.ProjectName"
    """<p>The unique name of a project.</p>"""
    recipe_name: "capo_databrew.types.recipe_name.RecipeName"
    """<p>The name of a recipe that will be developed during a project session.</p>"""
    resource_arn: NotRequired["capo_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the project.</p>"""
    sample: NotRequired["capo_databrew.types.sample.Sample"]
    """<p>The sample size and sampling type to apply to the data. If this parameter isn't specified, then the sample consists of the first 500 rows from the dataset.</p>"""
    tags: NotRequired["capo_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags that have been applied to the project.</p>"""
    role_arn: NotRequired["capo_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the role that will be assumed for this project.</p>"""
    opened_by: NotRequired["capo_databrew.types.opened_by.OpenedBy"]
    """<p>The Amazon Resource Name (ARN) of the user that opened the project for use.</p>"""
    open_date: NotRequired["capo_databrew.types.date.Date"]
    """<p>The date and time when the project was opened.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Project) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "create_date" in value:
        import capo_databrew.types.date

        out["CreateDate"] = capo_databrew.types.date.serialize_json(
            value["create_date"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "last_modified_date" in value:
        import capo_databrew.types.date

        out["LastModifiedDate"] = capo_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    out["Name"] = value["name"]
    out["RecipeName"] = value["recipe_name"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "sample" in value:
        import capo_databrew.types.sample

        out["Sample"] = capo_databrew.types.sample.serialize_json(value["sample"])
    if "tags" in value:
        import capo_databrew.types.tag_map

        out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "opened_by" in value:
        out["OpenedBy"] = value["opened_by"]
    if "open_date" in value:
        import capo_databrew.types.date

        out["OpenDate"] = capo_databrew.types.date.serialize_json(value["open_date"])
    return out


def deserialize_json(data: dict) -> Project:
    out: Project = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("CreateDate") is not None:
        import capo_databrew.types.date

        out["create_date"] = capo_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    if data.get("LastModifiedDate") is not None:
        import capo_databrew.types.date

        out["last_modified_date"] = capo_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if data.get("LastModifiedBy") is not None:
        out["last_modified_by"] = data["LastModifiedBy"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RecipeName") is not None:
        out["recipe_name"] = data["RecipeName"]
    else:
        out["recipe_name"] = ""
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("Sample") is not None:
        import capo_databrew.types.sample

        out["sample"] = capo_databrew.types.sample.deserialize_json(data["Sample"])
    if data.get("Tags") is not None:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("OpenedBy") is not None:
        out["opened_by"] = data["OpenedBy"]
    if data.get("OpenDate") is not None:
        import capo_databrew.types.date

        out["open_date"] = capo_databrew.types.date.deserialize_json(data["OpenDate"])
    return out
