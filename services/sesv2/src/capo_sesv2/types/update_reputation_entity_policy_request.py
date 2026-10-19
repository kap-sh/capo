"""Generated from Smithy shape ``com.amazonaws.sesv2#UpdateReputationEntityPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.amazon_resource_name
    import capo_sesv2.types.reputation_entity_reference
    import capo_sesv2.types.reputation_entity_type


class UpdateReputationEntityPolicyRequest(TypedDict, closed=True):
    reputation_entity_type: (
        "capo_sesv2.types.reputation_entity_type.ReputationEntityType"
    )
    """<p>The type of reputation entity. Currently, only <code>RESOURCE</code> type entities are supported.</p>"""
    reputation_entity_reference: (
        "capo_sesv2.types.reputation_entity_reference.ReputationEntityReference"
    )
    """<p>The unique identifier for the reputation entity. For resource-type entities, this is the Amazon Resource Name (ARN) of the resource.</p>"""
    reputation_entity_policy: "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the reputation management policy to apply to this entity. This is an Amazon Web Services Amazon SES-managed policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReputationEntityPolicyRequest) -> dict:
    out: dict = {}
    out["ReputationEntityPolicy"] = value["reputation_entity_policy"]
    return out


def deserialize_json(data: dict) -> UpdateReputationEntityPolicyRequest:
    out: UpdateReputationEntityPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReputationEntityPolicy") is not None:
        out["reputation_entity_policy"] = data["ReputationEntityPolicy"]
    else:
        out["reputation_entity_policy"] = ""
    return out
