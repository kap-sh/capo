"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListSuggestedResiliencyPoliciesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.resiliency_policies


class ListSuggestedResiliencyPoliciesResponse(TypedDict, closed=True):
    resiliency_policies: (
        "capo_resiliencehub.types.resiliency_policies.ResiliencyPolicies"
    )
    """<p>The suggested resiliency policies for the Resilience Hub applications.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSuggestedResiliencyPoliciesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.resiliency_policies

    out["resiliencyPolicies"] = (
        capo_resiliencehub.types.resiliency_policies.serialize_json(
            value["resiliency_policies"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSuggestedResiliencyPoliciesResponse:
    out: ListSuggestedResiliencyPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyPolicies") is not None:
        import capo_resiliencehub.types.resiliency_policies

        out["resiliency_policies"] = (
            capo_resiliencehub.types.resiliency_policies.deserialize_json(
                data["resiliencyPolicies"]
            )
        )
    else:
        raise DeserializationError(
            "ListSuggestedResiliencyPoliciesResponse.resiliency_policies required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListSuggestedResiliencyPoliciesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resiliency_policies" in value:
        import capo_resiliencehub.types.resiliency_policies

        out["resiliency_policies"] = (
            capo_resiliencehub.types.resiliency_policies.redact_sensitive(
                value["resiliency_policies"]
            )
        )
    return out
