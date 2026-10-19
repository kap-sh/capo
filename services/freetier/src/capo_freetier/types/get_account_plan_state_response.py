"""Generated from Smithy shape ``com.amazonaws.freetier#GetAccountPlanStateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_freetier.types.account_id
    import capo_freetier.types.account_plan_status
    import capo_freetier.types.account_plan_type
    import capo_freetier.types.monetary_amount


class GetAccountPlanStateResponse(TypedDict, closed=True):
    account_id: "capo_freetier.types.account_id.AccountId"
    """<p> A unique identifier that identifies the account. </p>"""
    account_plan_type: "capo_freetier.types.account_plan_type.AccountPlanType"
    """<p> The plan type for the account. </p>"""
    account_plan_status: "capo_freetier.types.account_plan_status.AccountPlanStatus"
    """<p> The current status for the account plan. </p>"""
    account_plan_remaining_credits: NotRequired[
        "capo_freetier.types.monetary_amount.MonetaryAmount"
    ]
    """<p> The amount of credits remaining for the account. </p>"""
    account_plan_expiration_date: NotRequired["datetime.datetime"]
    """<p> The timestamp for when the current account plan expires. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccountPlanStateResponse) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_freetier.types.account_plan_type

    out["accountPlanType"] = (
        capo_freetier.types.account_plan_type.serialize_aws_json_1_0(
            value["account_plan_type"]
        )
    )
    import capo_freetier.types.account_plan_status

    out["accountPlanStatus"] = (
        capo_freetier.types.account_plan_status.serialize_aws_json_1_0(
            value["account_plan_status"]
        )
    )
    if "account_plan_remaining_credits" in value:
        import capo_freetier.types.monetary_amount

        out["accountPlanRemainingCredits"] = (
            capo_freetier.types.monetary_amount.serialize_aws_json_1_0(
                value["account_plan_remaining_credits"]
            )
        )
    if "account_plan_expiration_date" in value:
        import capo_freetier._protocol.serialize

        out["accountPlanExpirationDate"] = (
            capo_freetier._protocol.serialize.fmt_date_time(
                value["account_plan_expiration_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccountPlanStateResponse:
    out: GetAccountPlanStateResponse = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("accountPlanType") is not None:
        import capo_freetier.types.account_plan_type

        out["account_plan_type"] = (
            capo_freetier.types.account_plan_type.deserialize_aws_json_1_0(
                data["accountPlanType"]
            )
        )
    else:
        import typing

        out["account_plan_type"] = typing.cast(
            "capo_freetier.types.account_plan_type.AccountPlanType", ""
        )
    if data.get("accountPlanStatus") is not None:
        import capo_freetier.types.account_plan_status

        out["account_plan_status"] = (
            capo_freetier.types.account_plan_status.deserialize_aws_json_1_0(
                data["accountPlanStatus"]
            )
        )
    else:
        import typing

        out["account_plan_status"] = typing.cast(
            "capo_freetier.types.account_plan_status.AccountPlanStatus", ""
        )
    if data.get("accountPlanRemainingCredits") is not None:
        import capo_freetier.types.monetary_amount

        out["account_plan_remaining_credits"] = (
            capo_freetier.types.monetary_amount.deserialize_aws_json_1_0(
                data["accountPlanRemainingCredits"]
            )
        )
    if data.get("accountPlanExpirationDate") is not None:
        import datetime

        out["account_plan_expiration_date"] = datetime.datetime.fromisoformat(
            data["accountPlanExpirationDate"].replace("Z", "+00:00")
        )
    return out
