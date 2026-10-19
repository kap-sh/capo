"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.account_info_list
    import capo_compute_optimizer_automation.types.next_token


class ListAccountsResponse(TypedDict, closed=True):
    accounts: (
        "capo_compute_optimizer_automation.types.account_info_list.AccountInfoList"
    )
    """<p> The list of accounts in your organization enrolled in Compute Optimizer </p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p> The token to use to retrieve the next page of results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAccountsResponse) -> dict:
    out: dict = {}
    import capo_compute_optimizer_automation.types.account_info_list

    out["accounts"] = (
        capo_compute_optimizer_automation.types.account_info_list.serialize_aws_json_1_0(
            value["accounts"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAccountsResponse:
    out: ListAccountsResponse = {}  # type: ignore[typeddict-item]
    if data.get("accounts") is not None:
        import capo_compute_optimizer_automation.types.account_info_list

        out["accounts"] = (
            capo_compute_optimizer_automation.types.account_info_list.deserialize_aws_json_1_0(
                data["accounts"]
            )
        )
    else:
        out["accounts"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
