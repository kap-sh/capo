"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.action_list
    import capo_accessanalyzer.types.condition_key_map
    import capo_accessanalyzer.types.finding_id
    import capo_accessanalyzer.types.finding_source_list
    import capo_accessanalyzer.types.finding_status
    import capo_accessanalyzer.types.principal_map
    import capo_accessanalyzer.types.resource_control_policy_restriction
    import capo_accessanalyzer.types.resource_type
    import capo_accessanalyzer.types.timestamp


class FindingSummary(TypedDict, closed=True):
    id: "capo_accessanalyzer.types.finding_id.FindingId"
    """<p>The ID of the finding.</p>"""
    principal: NotRequired["capo_accessanalyzer.types.principal_map.PrincipalMap"]
    """<p>The external principal that has access to a resource within the zone of trust.</p>"""
    action: NotRequired["capo_accessanalyzer.types.action_list.ActionList"]
    """<p>The action in the analyzed policy statement that an external principal has permission to use.</p>"""
    resource: NotRequired["str"]
    """<p>The resource that the external principal has access to.</p>"""
    is_public: NotRequired["bool"]
    """<p>Indicates whether the finding reports a resource that has a policy that allows public access.</p>"""
    resource_type: "capo_accessanalyzer.types.resource_type.ResourceType"
    """<p>The type of the resource that the external principal has access to.</p>"""
    condition: "capo_accessanalyzer.types.condition_key_map.ConditionKeyMap"
    """<p>The condition in the analyzed policy statement that resulted in a finding.</p>"""
    created_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was created.</p>"""
    analyzed_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the resource-based policy that generated the finding was analyzed.</p>"""
    updated_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was most recently updated.</p>"""
    status: "capo_accessanalyzer.types.finding_status.FindingStatus"
    """<p>The status of the finding.</p>"""
    resource_owner_account: "str"
    """<p>The Amazon Web Services account ID that owns the resource.</p>"""
    error: NotRequired["str"]
    """<p>The error that resulted in an Error finding.</p>"""
    sources: NotRequired[
        "capo_accessanalyzer.types.finding_source_list.FindingSourceList"
    ]
    """<p>The sources of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.</p>"""
    resource_control_policy_restriction: NotRequired[
        "capo_accessanalyzer.types.resource_control_policy_restriction.ResourceControlPolicyRestriction"
    ]
    """<p>The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "principal" in value:
        import capo_accessanalyzer.types.principal_map

        out["principal"] = capo_accessanalyzer.types.principal_map.serialize_json(
            value["principal"]
        )
    if "action" in value:
        import capo_accessanalyzer.types.action_list

        out["action"] = capo_accessanalyzer.types.action_list.serialize_json(
            value["action"]
        )
    if "resource" in value:
        out["resource"] = value["resource"]
    if "is_public" in value:
        out["isPublic"] = value["is_public"]
    out["resourceType"] = value["resource_type"]
    import capo_accessanalyzer.types.condition_key_map

    out["condition"] = capo_accessanalyzer.types.condition_key_map.serialize_json(
        value["condition"]
    )
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
    out["status"] = value["status"]
    out["resourceOwnerAccount"] = value["resource_owner_account"]
    if "error" in value:
        out["error"] = value["error"]
    if "sources" in value:
        import capo_accessanalyzer.types.finding_source_list

        out["sources"] = capo_accessanalyzer.types.finding_source_list.serialize_json(
            value["sources"]
        )
    if "resource_control_policy_restriction" in value:
        out["resourceControlPolicyRestriction"] = value[
            "resource_control_policy_restriction"
        ]
    return out


def deserialize_json(data: dict) -> FindingSummary:
    out: FindingSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("principal") is not None:
        import capo_accessanalyzer.types.principal_map

        out["principal"] = capo_accessanalyzer.types.principal_map.deserialize_json(
            data["principal"]
        )
    if data.get("action") is not None:
        import capo_accessanalyzer.types.action_list

        out["action"] = capo_accessanalyzer.types.action_list.deserialize_json(
            data["action"]
        )
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    if data.get("isPublic") is not None:
        out["is_public"] = data["isPublic"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("condition") is not None:
        import capo_accessanalyzer.types.condition_key_map

        out["condition"] = capo_accessanalyzer.types.condition_key_map.deserialize_json(
            data["condition"]
        )
    else:
        out["condition"] = {}
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
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("resourceOwnerAccount") is not None:
        out["resource_owner_account"] = data["resourceOwnerAccount"]
    else:
        out["resource_owner_account"] = ""
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("sources") is not None:
        import capo_accessanalyzer.types.finding_source_list

        out["sources"] = capo_accessanalyzer.types.finding_source_list.deserialize_json(
            data["sources"]
        )
    if data.get("resourceControlPolicyRestriction") is not None:
        out["resource_control_policy_restriction"] = data[
            "resourceControlPolicyRestriction"
        ]
    return out
