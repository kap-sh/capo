"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingSummaryV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.finding_id
    import capo_accessanalyzer.types.finding_status
    import capo_accessanalyzer.types.finding_type
    import capo_accessanalyzer.types.resource_type
    import capo_accessanalyzer.types.timestamp


class FindingSummaryV2(TypedDict, closed=True):
    analyzed_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the resource-based policy or IAM entity that generated the finding was analyzed.</p>"""
    created_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was created.</p>"""
    error: NotRequired["str"]
    """<p>The error that resulted in an Error finding.</p>"""
    id: "capo_accessanalyzer.types.finding_id.FindingId"
    """<p>The ID of the finding.</p>"""
    resource: NotRequired["str"]
    """<p>The resource that the external principal has access to.</p>"""
    resource_type: "capo_accessanalyzer.types.resource_type.ResourceType"
    """<p>The type of the resource that the external principal has access to.</p>"""
    resource_owner_account: "str"
    """<p>The Amazon Web Services account ID that owns the resource.</p>"""
    status: "capo_accessanalyzer.types.finding_status.FindingStatus"
    """<p>The status of the finding.</p>"""
    updated_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was most recently updated.</p>"""
    finding_type: NotRequired["capo_accessanalyzer.types.finding_type.FindingType"]
    """<p>The type of the access finding. For external access analyzers, the type is <code>ExternalAccess</code>. For unused access analyzers, the type can be <code>UnusedIAMRole</code>, <code>UnusedIAMUserAccessKey</code>, <code>UnusedIAMUserPassword</code>, or <code>UnusedPermission</code>. For internal access analyzers, the type is <code>InternalAccess</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingSummaryV2) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.timestamp

    out["analyzedAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["analyzed_at"]
    )
    import capo_accessanalyzer.types.timestamp

    out["createdAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["created_at"]
    )
    if "error" in value:
        out["error"] = value["error"]
    out["id"] = value["id"]
    if "resource" in value:
        out["resource"] = value["resource"]
    out["resourceType"] = value["resource_type"]
    out["resourceOwnerAccount"] = value["resource_owner_account"]
    out["status"] = value["status"]
    import capo_accessanalyzer.types.timestamp

    out["updatedAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["updated_at"]
    )
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    return out


def deserialize_json(data: dict) -> FindingSummaryV2:
    out: FindingSummaryV2 = {}  # type: ignore[typeddict-item]
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
    if data.get("createdAt") is not None:
        import capo_accessanalyzer.types.timestamp

        out["created_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("resourceOwnerAccount") is not None:
        out["resource_owner_account"] = data["resourceOwnerAccount"]
    else:
        out["resource_owner_account"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("updatedAt") is not None:
        import capo_accessanalyzer.types.timestamp

        out["updated_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    return out
