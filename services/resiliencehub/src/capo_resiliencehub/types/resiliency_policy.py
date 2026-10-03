"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResiliencyPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.data_location_constraint
    import capo_resiliencehub.types.disruption_policy
    import capo_resiliencehub.types.entity_description
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.estimated_cost_tier
    import capo_resiliencehub.types.resiliency_policy_tier
    import capo_resiliencehub.types.tag_map
    import capo_resiliencehub.types.time_stamp


class ResiliencyPolicy(TypedDict, closed=True):
    policy_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    policy_name: NotRequired["capo_resiliencehub.types.entity_name.EntityName"]
    """<p>The name of the policy</p>"""
    policy_description: NotRequired[
        "capo_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>Description of the resiliency policy.</p>"""
    data_location_constraint: NotRequired[
        "capo_resiliencehub.types.data_location_constraint.DataLocationConstraint"
    ]
    """<p>Specifies a high-level geographical location constraint for where your resilience policy data can be stored.</p>"""
    tier: NotRequired[
        "capo_resiliencehub.types.resiliency_policy_tier.ResiliencyPolicyTier"
    ]
    """<p>The tier for this resiliency policy, ranging from the highest severity (<code>MissionCritical</code>) to lowest (<code>NonCritical</code>).</p>"""
    estimated_cost_tier: NotRequired[
        "capo_resiliencehub.types.estimated_cost_tier.EstimatedCostTier"
    ]
    """<p>Specifies the estimated cost tier of the resiliency policy.</p>"""
    policy: NotRequired["capo_resiliencehub.types.disruption_policy.DisruptionPolicy"]
    """<p>The resiliency policy.</p>"""
    creation_time: NotRequired["capo_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>Date and time when the resiliency policy was created.</p>"""
    tags: NotRequired["capo_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResiliencyPolicy) -> dict:
    out: dict = {}
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "policy_description" in value:
        out["policyDescription"] = value["policy_description"]
    if "data_location_constraint" in value:
        import capo_resiliencehub.types.data_location_constraint

        out["dataLocationConstraint"] = (
            capo_resiliencehub.types.data_location_constraint.serialize_json(
                value["data_location_constraint"]
            )
        )
    if "tier" in value:
        import capo_resiliencehub.types.resiliency_policy_tier

        out["tier"] = capo_resiliencehub.types.resiliency_policy_tier.serialize_json(
            value["tier"]
        )
    if "estimated_cost_tier" in value:
        import capo_resiliencehub.types.estimated_cost_tier

        out["estimatedCostTier"] = (
            capo_resiliencehub.types.estimated_cost_tier.serialize_json(
                value["estimated_cost_tier"]
            )
        )
    if "policy" in value:
        import capo_resiliencehub.types.disruption_policy

        out["policy"] = capo_resiliencehub.types.disruption_policy.serialize_json(
            value["policy"]
        )
    if "creation_time" in value:
        import capo_resiliencehub.types.time_stamp

        out["creationTime"] = capo_resiliencehub.types.time_stamp.serialize_json(
            value["creation_time"]
        )
    if "tags" in value:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ResiliencyPolicy:
    out: ResiliencyPolicy = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    if data.get("policyName") is not None:
        out["policy_name"] = data["policyName"]
    if data.get("policyDescription") is not None:
        out["policy_description"] = data["policyDescription"]
    if data.get("dataLocationConstraint") is not None:
        import capo_resiliencehub.types.data_location_constraint

        out["data_location_constraint"] = (
            capo_resiliencehub.types.data_location_constraint.deserialize_json(
                data["dataLocationConstraint"]
            )
        )
    if data.get("tier") is not None:
        import capo_resiliencehub.types.resiliency_policy_tier

        out["tier"] = capo_resiliencehub.types.resiliency_policy_tier.deserialize_json(
            data["tier"]
        )
    if data.get("estimatedCostTier") is not None:
        import capo_resiliencehub.types.estimated_cost_tier

        out["estimated_cost_tier"] = (
            capo_resiliencehub.types.estimated_cost_tier.deserialize_json(
                data["estimatedCostTier"]
            )
        )
    if data.get("policy") is not None:
        import capo_resiliencehub.types.disruption_policy

        out["policy"] = capo_resiliencehub.types.disruption_policy.deserialize_json(
            data["policy"]
        )
    if data.get("creationTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["creation_time"] = capo_resiliencehub.types.time_stamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("tags") is not None:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.deserialize_json(data["tags"])
    return out
