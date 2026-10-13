"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListBillingGroupsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_group_list
    import capo_billingconductor.types.token


class ListBillingGroupsOutput(TypedDict, closed=True):
    billing_groups: NotRequired[
        "capo_billingconductor.types.billing_group_list.BillingGroupList"
    ]
    """<p>A list of <code>BillingGroupListElement</code> retrieved. </p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p>The pagination token that's used on subsequent calls to get billing groups. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupsOutput) -> dict:
    out: dict = {}
    if "billing_groups" in value:
        import capo_billingconductor.types.billing_group_list

        out["BillingGroups"] = (
            capo_billingconductor.types.billing_group_list.serialize_json(
                value["billing_groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBillingGroupsOutput:
    out: ListBillingGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("BillingGroups") is not None:
        import capo_billingconductor.types.billing_group_list

        out["billing_groups"] = (
            capo_billingconductor.types.billing_group_list.deserialize_json(
                data["BillingGroups"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListBillingGroupsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "billing_groups" in value:
        import capo_billingconductor.types.billing_group_list

        out["billing_groups"] = (
            capo_billingconductor.types.billing_group_list.redact_sensitive(
                value["billing_groups"]
            )
        )
    return out
