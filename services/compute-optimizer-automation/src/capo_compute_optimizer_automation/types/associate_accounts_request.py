"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AssociateAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.account_id_list
    import capo_compute_optimizer_automation.types.client_token


class AssociateAccountsRequest(TypedDict, closed=True):
    account_ids: "capo_compute_optimizer_automation.types.account_id_list.AccountIdList"
    """<p> The IDs of the member accounts to associate. You can specify up to 50 account IDs. </p>"""
    client_token: NotRequired[
        "capo_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p> A unique identifier to ensure idempotency of the request. Valid for 24 hours after creation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateAccountsRequest) -> dict:
    out: dict = {}
    import capo_compute_optimizer_automation.types.account_id_list

    out["accountIds"] = (
        capo_compute_optimizer_automation.types.account_id_list.serialize_aws_json_1_0(
            value["account_ids"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateAccountsRequest:
    out: AssociateAccountsRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_compute_optimizer_automation.types.account_id_list

        out["account_ids"] = (
            capo_compute_optimizer_automation.types.account_id_list.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    else:
        out["account_ids"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
