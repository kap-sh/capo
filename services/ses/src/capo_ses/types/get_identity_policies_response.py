"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.policy_map


class GetIdentityPoliciesResponse(TypedDict, closed=True):
    policies: "capo_ses.types.policy_map.PolicyMap"
    """<p>A map of policy names to policies.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityPoliciesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.policy_map

    capo_ses.types.policy_map.serialize_query(
        value["policies"], pairs, f"{key_prefix}Policies"
    )


def deserialize_query(el: Element) -> GetIdentityPoliciesResponse:
    out: GetIdentityPoliciesResponse = {}  # type: ignore[typeddict-item]
    child_policies = el.find("Policies")
    if child_policies is not None:
        import capo_ses.types.policy_map

        out["policies"] = capo_ses.types.policy_map.deserialize_query(child_policies)
    else:
        out["policies"] = {}
    return out
