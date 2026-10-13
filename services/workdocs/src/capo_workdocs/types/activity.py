"""Generated from Smithy shape ``com.amazonaws.workdocs#Activity``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.activity_type
    import capo_workdocs.types.boolean_type
    import capo_workdocs.types.comment_metadata
    import capo_workdocs.types.id_type
    import capo_workdocs.types.participants
    import capo_workdocs.types.resource_metadata
    import capo_workdocs.types.timestamp_type
    import capo_workdocs.types.user_metadata


class Activity(TypedDict, closed=True):
    type: NotRequired["capo_workdocs.types.activity_type.ActivityType"]
    """<p>The activity type.</p>"""
    time_stamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The timestamp when the action was performed.</p>"""
    is_indirect_activity: "capo_workdocs.types.boolean_type.BooleanType"
    """<p>Indicates whether an activity is indirect or direct. An indirect activity results from a direct activity performed on a parent resource. For example, sharing a parent folder (the direct activity) shares all of the subfolders and documents within the parent folder (the indirect activity).</p>"""
    organization_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the organization.</p>"""
    initiator: NotRequired["capo_workdocs.types.user_metadata.UserMetadata"]
    """<p>The user who performed the action.</p>"""
    participants: NotRequired["capo_workdocs.types.participants.Participants"]
    """<p>The list of users or groups impacted by this action. This is an optional field and is filled for the following sharing activities: DOCUMENT_SHARED, DOCUMENT_SHARED, DOCUMENT_UNSHARED, FOLDER_SHARED, FOLDER_UNSHARED.</p>"""
    resource_metadata: NotRequired[
        "capo_workdocs.types.resource_metadata.ResourceMetadata"
    ]
    """<p>The metadata of the resource involved in the user action.</p>"""
    original_parent: NotRequired[
        "capo_workdocs.types.resource_metadata.ResourceMetadata"
    ]
    """<p>The original parent of the resource. This is an optional field and is filled for move activities.</p>"""
    comment_metadata: NotRequired[
        "capo_workdocs.types.comment_metadata.CommentMetadata"
    ]
    """<p>Metadata of the commenting activity. This is an optional field and is filled for commenting activities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Activity) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_workdocs.types.activity_type

        out["Type"] = capo_workdocs.types.activity_type.serialize_json(value["type"])
    if "time_stamp" in value:
        import capo_workdocs.types.timestamp_type

        out["TimeStamp"] = capo_workdocs.types.timestamp_type.serialize_json(
            value["time_stamp"]
        )
    out["IsIndirectActivity"] = value.get("is_indirect_activity", False)
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    if "initiator" in value:
        import capo_workdocs.types.user_metadata

        out["Initiator"] = capo_workdocs.types.user_metadata.serialize_json(
            value["initiator"]
        )
    if "participants" in value:
        import capo_workdocs.types.participants

        out["Participants"] = capo_workdocs.types.participants.serialize_json(
            value["participants"]
        )
    if "resource_metadata" in value:
        import capo_workdocs.types.resource_metadata

        out["ResourceMetadata"] = capo_workdocs.types.resource_metadata.serialize_json(
            value["resource_metadata"]
        )
    if "original_parent" in value:
        import capo_workdocs.types.resource_metadata

        out["OriginalParent"] = capo_workdocs.types.resource_metadata.serialize_json(
            value["original_parent"]
        )
    if "comment_metadata" in value:
        import capo_workdocs.types.comment_metadata

        out["CommentMetadata"] = capo_workdocs.types.comment_metadata.serialize_json(
            value["comment_metadata"]
        )
    return out


def deserialize_json(data: dict) -> Activity:
    out: Activity = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_workdocs.types.activity_type

        out["type"] = capo_workdocs.types.activity_type.deserialize_json(data["Type"])
    if data.get("TimeStamp") is not None:
        import capo_workdocs.types.timestamp_type

        out["time_stamp"] = capo_workdocs.types.timestamp_type.deserialize_json(
            data["TimeStamp"]
        )
    if data.get("IsIndirectActivity") is not None:
        out["is_indirect_activity"] = data["IsIndirectActivity"]
    else:
        out["is_indirect_activity"] = False
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    if data.get("Initiator") is not None:
        import capo_workdocs.types.user_metadata

        out["initiator"] = capo_workdocs.types.user_metadata.deserialize_json(
            data["Initiator"]
        )
    if data.get("Participants") is not None:
        import capo_workdocs.types.participants

        out["participants"] = capo_workdocs.types.participants.deserialize_json(
            data["Participants"]
        )
    if data.get("ResourceMetadata") is not None:
        import capo_workdocs.types.resource_metadata

        out["resource_metadata"] = (
            capo_workdocs.types.resource_metadata.deserialize_json(
                data["ResourceMetadata"]
            )
        )
    if data.get("OriginalParent") is not None:
        import capo_workdocs.types.resource_metadata

        out["original_parent"] = capo_workdocs.types.resource_metadata.deserialize_json(
            data["OriginalParent"]
        )
    if data.get("CommentMetadata") is not None:
        import capo_workdocs.types.comment_metadata

        out["comment_metadata"] = capo_workdocs.types.comment_metadata.deserialize_json(
            data["CommentMetadata"]
        )
    return out


def redact_sensitive(value: Activity) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "initiator" in value:
        import capo_workdocs.types.user_metadata

        out["initiator"] = capo_workdocs.types.user_metadata.redact_sensitive(
            value["initiator"]
        )
    if "participants" in value:
        import capo_workdocs.types.participants

        out["participants"] = capo_workdocs.types.participants.redact_sensitive(
            value["participants"]
        )
    if "resource_metadata" in value:
        import capo_workdocs.types.resource_metadata

        out["resource_metadata"] = (
            capo_workdocs.types.resource_metadata.redact_sensitive(
                value["resource_metadata"]
            )
        )
    if "original_parent" in value:
        import capo_workdocs.types.resource_metadata

        out["original_parent"] = capo_workdocs.types.resource_metadata.redact_sensitive(
            value["original_parent"]
        )
    if "comment_metadata" in value:
        import capo_workdocs.types.comment_metadata

        out["comment_metadata"] = capo_workdocs.types.comment_metadata.redact_sensitive(
            value["comment_metadata"]
        )
    return out
