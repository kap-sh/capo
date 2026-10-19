"""Generated from Smithy shape ``com.amazonaws.billing#ListEnterpriseSupportLinkedAccountChargesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.linked_account_charge_list
    import capo_billing.types.page_token


class ListEnterpriseSupportLinkedAccountChargesResponse(TypedDict, closed=True):
    linked_account: (
        "capo_billing.types.linked_account_charge_list.LinkedAccountChargeList"
    )
    """<p>The list of Enterprise Support charges per linked account.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>The pagination token for the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListEnterpriseSupportLinkedAccountChargesResponse,
) -> dict:
    out: dict = {}
    import capo_billing.types.linked_account_charge_list

    out["linkedAccount"] = (
        capo_billing.types.linked_account_charge_list.serialize_aws_json_1_0(
            value["linked_account"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListEnterpriseSupportLinkedAccountChargesResponse:
    out: ListEnterpriseSupportLinkedAccountChargesResponse = {}  # type: ignore[typeddict-item]
    if data.get("linkedAccount") is not None:
        import capo_billing.types.linked_account_charge_list

        out["linked_account"] = (
            capo_billing.types.linked_account_charge_list.deserialize_aws_json_1_0(
                data["linkedAccount"]
            )
        )
    else:
        out["linked_account"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
