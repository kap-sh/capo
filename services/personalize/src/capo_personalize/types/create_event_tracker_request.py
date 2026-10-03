"""Generated from Smithy shape ``com.amazonaws.personalize#CreateEventTrackerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.name
    import capo_personalize.types.tags


class CreateEventTrackerRequest(TypedDict, closed=True):
    name: "capo_personalize.types.name.Name"
    """<p>The name for the event tracker.</p>"""
    dataset_group_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset group that receives the event data.</p>"""
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the event tracker.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEventTrackerRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["datasetGroupArn"] = value["dataset_group_arn"]
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEventTrackerRequest:
    out: CreateEventTrackerRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEventTrackerRequest.name required")
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    else:
        raise DeserializationError(
            "CreateEventTrackerRequest.dataset_group_arn required"
        )
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out
