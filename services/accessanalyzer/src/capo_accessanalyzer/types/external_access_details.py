"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ExternalAccessDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.action_list
    import capo_accessanalyzer.types.condition_key_map
    import capo_accessanalyzer.types.finding_source_list
    import capo_accessanalyzer.types.principal_map
    import capo_accessanalyzer.types.resource_control_policy_restriction


class ExternalAccessDetails(TypedDict, closed=True):
    action: NotRequired["capo_accessanalyzer.types.action_list.ActionList"]
    """<p>The action in the analyzed policy statement that an external principal has permission to use.</p>"""
    condition: "capo_accessanalyzer.types.condition_key_map.ConditionKeyMap"
    """<p>The condition in the analyzed policy statement that resulted in an external access finding.</p>"""
    is_public: NotRequired["bool"]
    """<p>Specifies whether the external access finding is public.</p>"""
    principal: NotRequired["capo_accessanalyzer.types.principal_map.PrincipalMap"]
    """<p>The external principal that has access to a resource within the zone of trust.</p>"""
    sources: NotRequired[
        "capo_accessanalyzer.types.finding_source_list.FindingSourceList"
    ]
    """<p>The sources of the external access finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.</p>"""
    resource_control_policy_restriction: NotRequired[
        "capo_accessanalyzer.types.resource_control_policy_restriction.ResourceControlPolicyRestriction"
    ]
    """<p>The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).</p> <ul> <li> <p> <code>APPLICABLE</code>: There is an RCP present in the organization but IAM Access Analyzer does not include it in the evaluation of effective permissions. For example, if <code>s3:DeleteObject</code> is blocked by the RCP and the restriction is <code>APPLICABLE</code>, then <code>s3:DeleteObject</code> would still be included in the list of actions for the finding.</p> </li> <li> <p> <code>FAILED_TO_EVALUATE_RCP</code>: There was an error evaluating the RCP.</p> </li> <li> <p> <code>NOT_APPLICABLE</code>: There was no RCP present in the organization, or there was no RCP applicable to the resource. For example, the resource being analyzed is an Amazon RDS snapshot and there is an RCP in the organization, but the RCP only impacts Amazon S3 buckets.</p> </li> <li> <p> <code>APPLIED</code>: This restriction is not currently available for external access findings. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalAccessDetails) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_accessanalyzer.types.action_list

        out["action"] = capo_accessanalyzer.types.action_list.serialize_json(
            value["action"]
        )
    import capo_accessanalyzer.types.condition_key_map

    out["condition"] = capo_accessanalyzer.types.condition_key_map.serialize_json(
        value["condition"]
    )
    if "is_public" in value:
        out["isPublic"] = value["is_public"]
    if "principal" in value:
        import capo_accessanalyzer.types.principal_map

        out["principal"] = capo_accessanalyzer.types.principal_map.serialize_json(
            value["principal"]
        )
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


def deserialize_json(data: dict) -> ExternalAccessDetails:
    out: ExternalAccessDetails = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_accessanalyzer.types.action_list

        out["action"] = capo_accessanalyzer.types.action_list.deserialize_json(
            data["action"]
        )
    if data.get("condition") is not None:
        import capo_accessanalyzer.types.condition_key_map

        out["condition"] = capo_accessanalyzer.types.condition_key_map.deserialize_json(
            data["condition"]
        )
    else:
        out["condition"] = {}
    if data.get("isPublic") is not None:
        out["is_public"] = data["isPublic"]
    if data.get("principal") is not None:
        import capo_accessanalyzer.types.principal_map

        out["principal"] = capo_accessanalyzer.types.principal_map.deserialize_json(
            data["principal"]
        )
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
