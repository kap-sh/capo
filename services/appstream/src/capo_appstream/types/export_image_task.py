"""Generated from Smithy shape ``com.amazonaws.appstream#ExportImageTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.ami_name
    import capo_appstream.types.arn
    import capo_appstream.types.description
    import capo_appstream.types.error_details_list
    import capo_appstream.types.export_image_task_state
    import capo_appstream.types.photon_ami_id
    import capo_appstream.types.tags
    import capo_appstream.types.timestamp
    import capo_appstream.types.uuid


class ExportImageTask(TypedDict, closed=True):
    task_id: NotRequired["capo_appstream.types.uuid.UUID"]
    """<p>The unique identifier for the export image task. Use this ID to track the task's progress and retrieve its details.</p>"""
    image_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the WorkSpaces Applications image being exported.</p>"""
    ami_name: NotRequired["capo_appstream.types.ami_name.AmiName"]
    """<p>The name of the EC2 AMI that will be created by this export task.</p>"""
    created_date: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The date and time when the export image task was created.</p>"""
    ami_description: NotRequired["capo_appstream.types.description.Description"]
    """<p>The description that will be applied to the exported EC2 AMI.</p>"""
    state: NotRequired[
        "capo_appstream.types.export_image_task_state.ExportImageTaskState"
    ]
    """<p>The current state of the export image task, such as PENDING, RUNNING, COMPLETED, or FAILED.</p>"""
    ami_id: NotRequired["capo_appstream.types.photon_ami_id.PhotonAmiId"]
    """<p>The ID of the EC2 AMI that was created by this export task. This field is only populated when the task completes successfully.</p>"""
    tag_specifications: NotRequired["capo_appstream.types.tags.Tags"]
    """<p>The tags that will be applied to the exported EC2 AMI.</p>"""
    error_details: NotRequired[
        "capo_appstream.types.error_details_list.ErrorDetailsList"
    ]
    """<p>Details about any errors that occurred during the export process. This field is only populated when the task fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportImageTask) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "image_arn" in value:
        out["ImageArn"] = value["image_arn"]
    if "ami_name" in value:
        out["AmiName"] = value["ami_name"]
    if "created_date" in value:
        import capo_appstream.types.timestamp

        out["CreatedDate"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "ami_description" in value:
        out["AmiDescription"] = value["ami_description"]
    if "state" in value:
        import capo_appstream.types.export_image_task_state

        out["State"] = (
            capo_appstream.types.export_image_task_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "ami_id" in value:
        out["AmiId"] = value["ami_id"]
    if "tag_specifications" in value:
        import capo_appstream.types.tags

        out["TagSpecifications"] = capo_appstream.types.tags.serialize_aws_json_1_1(
            value["tag_specifications"]
        )
    if "error_details" in value:
        import capo_appstream.types.error_details_list

        out["ErrorDetails"] = (
            capo_appstream.types.error_details_list.serialize_aws_json_1_1(
                value["error_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportImageTask:
    out: ExportImageTask = {}  # type: ignore[typeddict-item]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    if data.get("ImageArn") is not None:
        out["image_arn"] = data["ImageArn"]
    if data.get("AmiName") is not None:
        out["ami_name"] = data["AmiName"]
    if data.get("CreatedDate") is not None:
        import capo_appstream.types.timestamp

        out["created_date"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if data.get("AmiDescription") is not None:
        out["ami_description"] = data["AmiDescription"]
    if data.get("State") is not None:
        import capo_appstream.types.export_image_task_state

        out["state"] = (
            capo_appstream.types.export_image_task_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if data.get("AmiId") is not None:
        out["ami_id"] = data["AmiId"]
    if data.get("TagSpecifications") is not None:
        import capo_appstream.types.tags

        out["tag_specifications"] = capo_appstream.types.tags.deserialize_aws_json_1_1(
            data["TagSpecifications"]
        )
    if data.get("ErrorDetails") is not None:
        import capo_appstream.types.error_details_list

        out["error_details"] = (
            capo_appstream.types.error_details_list.deserialize_aws_json_1_1(
                data["ErrorDetails"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportImageTask) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "image_arn" in value:
        out["ImageArn"] = value["image_arn"]
    if "ami_name" in value:
        out["AmiName"] = value["ami_name"]
    if "created_date" in value:
        import capo_appstream.types.timestamp

        out["CreatedDate"] = capo_appstream.types.timestamp.serialize_cbor(
            value["created_date"]
        )
    if "ami_description" in value:
        out["AmiDescription"] = value["ami_description"]
    if "state" in value:
        import capo_appstream.types.export_image_task_state

        out["State"] = capo_appstream.types.export_image_task_state.serialize_cbor(
            value["state"]
        )
    if "ami_id" in value:
        out["AmiId"] = value["ami_id"]
    if "tag_specifications" in value:
        import capo_appstream.types.tags

        out["TagSpecifications"] = capo_appstream.types.tags.serialize_cbor(
            value["tag_specifications"]
        )
    if "error_details" in value:
        import capo_appstream.types.error_details_list

        out["ErrorDetails"] = capo_appstream.types.error_details_list.serialize_cbor(
            value["error_details"]
        )
    return out


def deserialize_cbor(data: dict) -> ExportImageTask:
    out: ExportImageTask = {}  # type: ignore[typeddict-item]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    if data.get("ImageArn") is not None:
        out["image_arn"] = data["ImageArn"]
    if data.get("AmiName") is not None:
        out["ami_name"] = data["AmiName"]
    if data.get("CreatedDate") is not None:
        import capo_appstream.types.timestamp

        out["created_date"] = capo_appstream.types.timestamp.deserialize_cbor(
            data["CreatedDate"]
        )
    if data.get("AmiDescription") is not None:
        out["ami_description"] = data["AmiDescription"]
    if data.get("State") is not None:
        import capo_appstream.types.export_image_task_state

        out["state"] = capo_appstream.types.export_image_task_state.deserialize_cbor(
            data["State"]
        )
    if data.get("AmiId") is not None:
        out["ami_id"] = data["AmiId"]
    if data.get("TagSpecifications") is not None:
        import capo_appstream.types.tags

        out["tag_specifications"] = capo_appstream.types.tags.deserialize_cbor(
            data["TagSpecifications"]
        )
    if data.get("ErrorDetails") is not None:
        import capo_appstream.types.error_details_list

        out["error_details"] = capo_appstream.types.error_details_list.deserialize_cbor(
            data["ErrorDetails"]
        )
    return out
