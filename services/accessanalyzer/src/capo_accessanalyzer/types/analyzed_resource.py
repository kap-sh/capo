"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalyzedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.action_list
    import capo_accessanalyzer.types.finding_status
    import capo_accessanalyzer.types.resource_arn
    import capo_accessanalyzer.types.resource_type
    import capo_accessanalyzer.types.shared_via_list
    import capo_accessanalyzer.types.timestamp


class AnalyzedResource(TypedDict, closed=True):
    resource_arn: "capo_accessanalyzer.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource that was analyzed.</p>"""
    resource_type: "capo_accessanalyzer.types.resource_type.ResourceType"
    """<p>The type of the resource that was analyzed.</p>"""
    created_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was created.</p>"""
    analyzed_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the resource was analyzed.</p>"""
    updated_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was updated.</p>"""
    is_public: "bool"
    """<p>Indicates whether the policy that generated the finding grants public access to the resource.</p>"""
    actions: NotRequired["capo_accessanalyzer.types.action_list.ActionList"]
    """<p>The actions that an external principal is granted permission to use by the policy that generated the finding.</p>"""
    shared_via: NotRequired["capo_accessanalyzer.types.shared_via_list.SharedViaList"]
    """<p>Indicates how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.</p>"""
    status: NotRequired["capo_accessanalyzer.types.finding_status.FindingStatus"]
    """<p>The current status of the finding generated from the analyzed resource.</p>"""
    resource_owner_account: "str"
    """<p>The Amazon Web Services account ID that owns the resource.</p>"""
    error: NotRequired["str"]
    """<p>An error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzedResource) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["resourceType"] = value["resource_type"]
    import capo_accessanalyzer.types.timestamp

    out["createdAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_accessanalyzer.types.timestamp

    out["analyzedAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["analyzed_at"]
    )
    import capo_accessanalyzer.types.timestamp

    out["updatedAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["updated_at"]
    )
    out["isPublic"] = value["is_public"]
    if "actions" in value:
        import capo_accessanalyzer.types.action_list

        out["actions"] = capo_accessanalyzer.types.action_list.serialize_json(
            value["actions"]
        )
    if "shared_via" in value:
        import capo_accessanalyzer.types.shared_via_list

        out["sharedVia"] = capo_accessanalyzer.types.shared_via_list.serialize_json(
            value["shared_via"]
        )
    if "status" in value:
        out["status"] = value["status"]
    out["resourceOwnerAccount"] = value["resource_owner_account"]
    if "error" in value:
        out["error"] = value["error"]
    return out


def deserialize_json(data: dict) -> AnalyzedResource:
    out: AnalyzedResource = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("createdAt") is not None:
        import capo_accessanalyzer.types.timestamp

        out["created_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("analyzedAt") is not None:
        import capo_accessanalyzer.types.timestamp

        out["analyzed_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["analyzedAt"]
        )
    else:
        import datetime

        out["analyzed_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updatedAt") is not None:
        import capo_accessanalyzer.types.timestamp

        out["updated_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("isPublic") is not None:
        out["is_public"] = data["isPublic"]
    else:
        out["is_public"] = False
    if data.get("actions") is not None:
        import capo_accessanalyzer.types.action_list

        out["actions"] = capo_accessanalyzer.types.action_list.deserialize_json(
            data["actions"]
        )
    if data.get("sharedVia") is not None:
        import capo_accessanalyzer.types.shared_via_list

        out["shared_via"] = capo_accessanalyzer.types.shared_via_list.deserialize_json(
            data["sharedVia"]
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("resourceOwnerAccount") is not None:
        out["resource_owner_account"] = data["resourceOwnerAccount"]
    else:
        out["resource_owner_account"] = ""
    if data.get("error") is not None:
        out["error"] = data["error"]
    return out
