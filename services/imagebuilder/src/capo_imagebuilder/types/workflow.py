"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Workflow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.version_number
    import capo_imagebuilder.types.workflow_build_version_arn
    import capo_imagebuilder.types.workflow_data
    import capo_imagebuilder.types.workflow_parameter_detail_list
    import capo_imagebuilder.types.workflow_state
    import capo_imagebuilder.types.workflow_type


class Workflow(TypedDict, closed=True):
    arn: NotRequired[
        "capo_imagebuilder.types.workflow_build_version_arn.WorkflowBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the workflow resource.</p>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the workflow resource.</p>"""
    version: NotRequired["capo_imagebuilder.types.version_number.VersionNumber"]
    """<p>The workflow resource version. Workflow resources are immutable. To make a change, you can clone a workflow or create a new version.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the workflow.</p>"""
    change_description: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.</p>"""
    type: NotRequired["capo_imagebuilder.types.workflow_type.WorkflowType"]
    """<p>The image creation stage that the workflow applies to.</p>"""
    state: NotRequired["capo_imagebuilder.types.workflow_state.WorkflowState"]
    """<p>Describes the current status of the workflow and the reason for that status.</p>"""
    owner: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the workflow resource.</p>"""
    data: NotRequired["capo_imagebuilder.types.workflow_data.WorkflowData"]
    """<p>Contains the YAML document content for the workflow.</p>"""
    kms_key_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The KMS key identifier used to encrypt the workflow resource. This can be either the Key ARN or the Alias ARN. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    date_created: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The timestamp when Image Builder created the workflow resource.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags that apply to the workflow resource.</p>"""
    parameters: NotRequired[
        "capo_imagebuilder.types.workflow_parameter_detail_list.WorkflowParameterDetailList"
    ]
    """<p>An array of input parameters that the image workflow uses to control actions or configure settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Workflow) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "description" in value:
        out["description"] = value["description"]
    if "change_description" in value:
        out["changeDescription"] = value["change_description"]
    if "type" in value:
        import capo_imagebuilder.types.workflow_type

        out["type"] = capo_imagebuilder.types.workflow_type.serialize_json(
            value["type"]
        )
    if "state" in value:
        import capo_imagebuilder.types.workflow_state

        out["state"] = capo_imagebuilder.types.workflow_state.serialize_json(
            value["state"]
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "data" in value:
        out["data"] = value["data"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "parameters" in value:
        import capo_imagebuilder.types.workflow_parameter_detail_list

        out["parameters"] = (
            capo_imagebuilder.types.workflow_parameter_detail_list.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> Workflow:
    out: Workflow = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("changeDescription") is not None:
        out["change_description"] = data["changeDescription"]
    if data.get("type") is not None:
        import capo_imagebuilder.types.workflow_type

        out["type"] = capo_imagebuilder.types.workflow_type.deserialize_json(
            data["type"]
        )
    if data.get("state") is not None:
        import capo_imagebuilder.types.workflow_state

        out["state"] = capo_imagebuilder.types.workflow_state.deserialize_json(
            data["state"]
        )
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    if data.get("data") is not None:
        out["data"] = data["data"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("dateCreated") is not None:
        out["date_created"] = data["dateCreated"]
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("parameters") is not None:
        import capo_imagebuilder.types.workflow_parameter_detail_list

        out["parameters"] = (
            capo_imagebuilder.types.workflow_parameter_detail_list.deserialize_json(
                data["parameters"]
            )
        )
    return out
