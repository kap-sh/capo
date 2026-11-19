"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#DisassociateAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.account_id_list
    import capo_compute_optimizer_automation.types.string_list


class DisassociateAccountsResponse(TypedDict, closed=True):
    account_ids: NotRequired[
        "capo_compute_optimizer_automation.types.account_id_list.AccountIdList"
    ]
    """<p> The IDs of the member accounts that were successfully disassociated. </p>"""
    errors: NotRequired[
        "capo_compute_optimizer_automation.types.string_list.StringList"
    ]
    """<p> Any errors that occurred during the disassociation process. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateAccountsResponse) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_compute_optimizer_automation.types.account_id_list

        out["accountIds"] = (
            capo_compute_optimizer_automation.types.account_id_list.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "errors" in value:
        import capo_compute_optimizer_automation.types.string_list

        out["errors"] = (
            capo_compute_optimizer_automation.types.string_list.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateAccountsResponse:
    out: DisassociateAccountsResponse = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_compute_optimizer_automation.types.account_id_list

        out["account_ids"] = (
            capo_compute_optimizer_automation.types.account_id_list.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if data.get("errors") is not None:
        import capo_compute_optimizer_automation.types.string_list

        out["errors"] = (
            capo_compute_optimizer_automation.types.string_list.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateAccountsResponse) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_compute_optimizer_automation.types.account_id_list

        out["accountIds"] = (
            capo_compute_optimizer_automation.types.account_id_list.serialize_cbor(
                value["account_ids"]
            )
        )
    if "errors" in value:
        import capo_compute_optimizer_automation.types.string_list

        out["errors"] = (
            capo_compute_optimizer_automation.types.string_list.serialize_cbor(
                value["errors"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DisassociateAccountsResponse:
    out: DisassociateAccountsResponse = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_compute_optimizer_automation.types.account_id_list

        out["account_ids"] = (
            capo_compute_optimizer_automation.types.account_id_list.deserialize_cbor(
                data["accountIds"]
            )
        )
    if data.get("errors") is not None:
        import capo_compute_optimizer_automation.types.string_list

        out["errors"] = (
            capo_compute_optimizer_automation.types.string_list.deserialize_cbor(
                data["errors"]
            )
        )
    return out
