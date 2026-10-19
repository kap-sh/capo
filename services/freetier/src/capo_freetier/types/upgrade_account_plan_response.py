"""Generated from Smithy shape ``com.amazonaws.freetier#UpgradeAccountPlanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_freetier.types.account_id
    import capo_freetier.types.account_plan_status
    import capo_freetier.types.account_plan_type


class UpgradeAccountPlanResponse(TypedDict, closed=True):
    account_id: "capo_freetier.types.account_id.AccountId"
    """<p> A unique identifier that identifies the account. </p>"""
    account_plan_type: "capo_freetier.types.account_plan_type.AccountPlanType"
    """<p> The type of plan for the account. </p>"""
    account_plan_status: "capo_freetier.types.account_plan_status.AccountPlanStatus"
    """<p> This indicates the latest state of the account plan within its lifecycle. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpgradeAccountPlanResponse) -> dict:
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
    return out


def deserialize_aws_json_1_0(data: dict) -> UpgradeAccountPlanResponse:
    out: UpgradeAccountPlanResponse = {}  # type: ignore[typeddict-item]
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
    return out
