"""Generated from Smithy shape ``com.amazonaws.freetier#UpgradeAccountPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_freetier.types.account_plan_type


class UpgradeAccountPlanRequest(TypedDict, closed=True):
    account_plan_type: "capo_freetier.types.account_plan_type.AccountPlanType"
    """<p> The target account plan type. This makes it explicit about the change and latest value of the <code>accountPlanType</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpgradeAccountPlanRequest) -> dict:
    out: dict = {}
    import capo_freetier.types.account_plan_type

    out["accountPlanType"] = (
        capo_freetier.types.account_plan_type.serialize_aws_json_1_0(
            value["account_plan_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpgradeAccountPlanRequest:
    out: UpgradeAccountPlanRequest = {}  # type: ignore[typeddict-item]
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
    return out
