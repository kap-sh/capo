"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetFindingV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.finding_details_list
    import capo_accessanalyzer.types.finding_id
    import capo_accessanalyzer.types.finding_status
    import capo_accessanalyzer.types.finding_type
    import capo_accessanalyzer.types.resource_type
    import capo_accessanalyzer.types.timestamp
    import capo_accessanalyzer.types.token


class GetFindingV2Response(TypedDict, closed=True):
    analyzed_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the resource-based policy or IAM entity that generated the finding was analyzed.</p>"""
    created_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was created.</p>"""
    error: NotRequired["str"]
    """<p>An error.</p>"""
    id: "capo_accessanalyzer.types.finding_id.FindingId"
    """<p>The ID of the finding to retrieve.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""
    resource: NotRequired["str"]
    """<p>The resource that generated the finding.</p>"""
    resource_type: "capo_accessanalyzer.types.resource_type.ResourceType"
    """<p>The type of the resource identified in the finding.</p>"""
    resource_owner_account: "str"
    """<p>Tye Amazon Web Services account ID that owns the resource.</p>"""
    status: "capo_accessanalyzer.types.finding_status.FindingStatus"
    """<p>The status of the finding.</p>"""
    updated_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was updated.</p>"""
    finding_details: "capo_accessanalyzer.types.finding_details_list.FindingDetailsList"
    """<p>A localized message that explains the finding and provides guidance on how to address it.</p>"""
    finding_type: NotRequired["capo_accessanalyzer.types.finding_type.FindingType"]
    """<p>The type of the finding. For external access analyzers, the type is <code>ExternalAccess</code>. For unused access analyzers, the type can be <code>UnusedIAMRole</code>, <code>UnusedIAMUserAccessKey</code>, <code>UnusedIAMUserPassword</code>, or <code>UnusedPermission</code>. For internal access analyzers, the type is <code>InternalAccess</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingV2Response) -> dict:
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
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "resource" in value:
        out["resource"] = value["resource"]
    out["resourceType"] = value["resource_type"]
    out["resourceOwnerAccount"] = value["resource_owner_account"]
    out["status"] = value["status"]
    import capo_accessanalyzer.types.timestamp

    out["updatedAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["updated_at"]
    )
    import capo_accessanalyzer.types.finding_details_list

    out["findingDetails"] = (
        capo_accessanalyzer.types.finding_details_list.serialize_json(
            value["finding_details"]
        )
    )
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    return out


def deserialize_json(data: dict) -> GetFindingV2Response:
    out: GetFindingV2Response = {}  # type: ignore[typeddict-item]
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
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
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
    if data.get("findingDetails") is not None:
        import capo_accessanalyzer.types.finding_details_list

        out["finding_details"] = (
            capo_accessanalyzer.types.finding_details_list.deserialize_json(
                data["findingDetails"]
            )
        )
    else:
        out["finding_details"] = []
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    return out
