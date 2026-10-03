"""Generated from Smithy shape ``com.amazonaws.personalize#CreateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.dataset_type
    import capo_personalize.types.name
    import capo_personalize.types.tags


class CreateDatasetRequest(TypedDict, closed=True):
    name: "capo_personalize.types.name.Name"
    """<p>The name for the dataset.</p>"""
    schema_arn: "capo_personalize.types.arn.Arn"
    """<p>The ARN of the schema to associate with the dataset. The schema defines the dataset fields.</p>"""
    dataset_group_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset group to add the dataset to.</p>"""
    dataset_type: "capo_personalize.types.dataset_type.DatasetType"
    """<p>The type of dataset.</p> <p>One of the following (case insensitive) values:</p> <ul> <li> <p>Interactions</p> </li> <li> <p>Items</p> </li> <li> <p>Users</p> </li> <li> <p>Actions</p> </li> <li> <p>Action_Interactions</p> </li> </ul>"""
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the dataset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["schemaArn"] = value["schema_arn"]
    out["datasetGroupArn"] = value["dataset_group_arn"]
    out["datasetType"] = value["dataset_type"]
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDatasetRequest.name required")
    if data.get("schemaArn") is not None:
        out["schema_arn"] = data["schemaArn"]
    else:
        raise DeserializationError("CreateDatasetRequest.schema_arn required")
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_group_arn required")
    if data.get("datasetType") is not None:
        out["dataset_type"] = data["datasetType"]
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_type required")
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out
