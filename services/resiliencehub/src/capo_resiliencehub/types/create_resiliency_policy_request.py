"""Generated from Smithy shape ``com.amazonaws.resiliencehub#CreateResiliencyPolicyRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.client_token
    import capo_resiliencehub.types.data_location_constraint
    import capo_resiliencehub.types.disruption_policy
    import capo_resiliencehub.types.entity_description
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.resiliency_policy_tier
    import capo_resiliencehub.types.tag_map


class CreateResiliencyPolicyRequest(TypedDict, closed=True):
    policy_name: "capo_resiliencehub.types.entity_name.EntityName"
    """<p>Name of the resiliency policy.</p>"""
    policy_description: NotRequired[
        "capo_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>Description of the resiliency policy.</p>"""
    data_location_constraint: NotRequired[
        "capo_resiliencehub.types.data_location_constraint.DataLocationConstraint"
    ]
    """<p>Specifies a high-level geographical location constraint for where your resilience policy data can be stored.</p>"""
    tier: "capo_resiliencehub.types.resiliency_policy_tier.ResiliencyPolicyTier"
    """<p>The tier for this resiliency policy, ranging from the highest severity (<code>MissionCritical</code>) to lowest (<code>NonCritical</code>).</p>"""
    policy: "capo_resiliencehub.types.disruption_policy.DisruptionPolicy"
    """<p>The type of resiliency policy to be created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.</p>"""
    client_token: NotRequired["capo_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""
    tags: NotRequired["capo_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResiliencyPolicyRequest) -> dict:
    out: dict = {}
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
    import capo_resiliencehub.types.resiliency_policy_tier

    out["tier"] = capo_resiliencehub.types.resiliency_policy_tier.serialize_json(
        value["tier"]
    )
    import capo_resiliencehub.types.disruption_policy

    out["policy"] = capo_resiliencehub.types.disruption_policy.serialize_json(
        value["policy"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateResiliencyPolicyRequest:
    out: CreateResiliencyPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyName") is not None:
        out["policy_name"] = data["policyName"]
    else:
        out["policy_name"] = ""
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
    else:
        import typing

        out["tier"] = typing.cast(
            "capo_resiliencehub.types.resiliency_policy_tier.ResiliencyPolicyTier", ""
        )
    if data.get("policy") is not None:
        import capo_resiliencehub.types.disruption_policy

        out["policy"] = capo_resiliencehub.types.disruption_policy.deserialize_json(
            data["policy"]
        )
    else:
        out["policy"] = {}
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateResiliencyPolicyRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
