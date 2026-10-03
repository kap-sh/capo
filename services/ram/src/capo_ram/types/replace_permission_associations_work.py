"""Generated from Smithy shape ``com.amazonaws.ram#ReplacePermissionAssociationsWork``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.date_time
    import capo_ram.types.replace_permission_associations_work_status
    import capo_ram.types.string


class ReplacePermissionAssociationsWork(TypedDict, closed=True):
    id: NotRequired["capo_ram.types.string.String"]
    """<p>The unique identifier for the background task associated with one <a>ReplacePermissionAssociations</a> request.</p>"""
    from_permission_arn: NotRequired["capo_ram.types.string.String"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the managed permission that this background task is replacing.</p>"""
    from_permission_version: NotRequired["capo_ram.types.string.String"]
    """<p>The version of the managed permission that this background task is replacing.</p>"""
    to_permission_arn: NotRequired["capo_ram.types.string.String"]
    """<p>The ARN of the managed permission that this background task is associating with the resource shares in place of the managed permission and version specified in <code>fromPermissionArn</code> and <code>fromPermissionVersion</code>.</p>"""
    to_permission_version: NotRequired["capo_ram.types.string.String"]
    """<p>The version of the managed permission that this background task is associating with the resource shares. This is always the version that is currently the default for this managed permission.</p>"""
    status: NotRequired[
        "capo_ram.types.replace_permission_associations_work_status.ReplacePermissionAssociationsWorkStatus"
    ]
    """<p>Specifies the current status of the background tasks for the specified ID. The output is one of the following strings:</p> <ul> <li> <p> <code>IN_PROGRESS</code> </p> </li> <li> <p> <code>COMPLETED</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> </ul>"""
    status_message: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies the reason for a <code>FAILED</code> status. This field is present only when there <code>status</code> is <code>FAILED</code>.</p>"""
    creation_time: NotRequired["capo_ram.types.date_time.DateTime"]
    """<p>The date and time when this asynchronous background task was created.</p>"""
    last_updated_time: NotRequired["capo_ram.types.date_time.DateTime"]
    """<p>The date and time when the status of this background task was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplacePermissionAssociationsWork) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "from_permission_arn" in value:
        out["fromPermissionArn"] = value["from_permission_arn"]
    if "from_permission_version" in value:
        out["fromPermissionVersion"] = value["from_permission_version"]
    if "to_permission_arn" in value:
        out["toPermissionArn"] = value["to_permission_arn"]
    if "to_permission_version" in value:
        out["toPermissionVersion"] = value["to_permission_version"]
    if "status" in value:
        import capo_ram.types.replace_permission_associations_work_status

        out["status"] = (
            capo_ram.types.replace_permission_associations_work_status.serialize_json(
                value["status"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "creation_time" in value:
        import capo_ram.types.date_time

        out["creationTime"] = capo_ram.types.date_time.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_ram.types.date_time

        out["lastUpdatedTime"] = capo_ram.types.date_time.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> ReplacePermissionAssociationsWork:
    out: ReplacePermissionAssociationsWork = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("fromPermissionArn") is not None:
        out["from_permission_arn"] = data["fromPermissionArn"]
    if data.get("fromPermissionVersion") is not None:
        out["from_permission_version"] = data["fromPermissionVersion"]
    if data.get("toPermissionArn") is not None:
        out["to_permission_arn"] = data["toPermissionArn"]
    if data.get("toPermissionVersion") is not None:
        out["to_permission_version"] = data["toPermissionVersion"]
    if data.get("status") is not None:
        import capo_ram.types.replace_permission_associations_work_status

        out["status"] = (
            capo_ram.types.replace_permission_associations_work_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("creationTime") is not None:
        import capo_ram.types.date_time

        out["creation_time"] = capo_ram.types.date_time.deserialize_json(
            data["creationTime"]
        )
    if data.get("lastUpdatedTime") is not None:
        import capo_ram.types.date_time

        out["last_updated_time"] = capo_ram.types.date_time.deserialize_json(
            data["lastUpdatedTime"]
        )
    return out
