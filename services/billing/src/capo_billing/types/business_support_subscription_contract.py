"""Generated from Smithy shape ``com.amazonaws.billing#BusinessSupportSubscriptionContract``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.account_id


class BusinessSupportSubscriptionContract(TypedDict, closed=True):
    account_id: "capo_billing.types.account_id.AccountId"
    """<p>The account ID associated with this subscription contract.</p>"""
    plan_name: "str"
    """<p>The name of the Support plan for this subscription contract. Valid values: <code>AWSSupportBusiness</code> (Business Support plan), <code>AWSSupportDeveloper</code> (Developer Support plan), <code>AWSSupportEssential</code> (Basic Support plan).</p>"""
    contract_start_date: "datetime.datetime"
    """<p>The start date of the subscription contract.</p>"""
    contract_end_date: "datetime.datetime"
    """<p>The end date of the subscription contract.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessSupportSubscriptionContract) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["planName"] = value["plan_name"]
    import capo_billing.types._prelude.timestamp

    out["contractStartDate"] = (
        capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["contract_start_date"]
        )
    )
    import capo_billing.types._prelude.timestamp

    out["contractEndDate"] = (
        capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["contract_end_date"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BusinessSupportSubscriptionContract:
    out: BusinessSupportSubscriptionContract = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError(
            "BusinessSupportSubscriptionContract.account_id required"
        )
    if data.get("planName") is not None:
        out["plan_name"] = data["planName"]
    else:
        raise DeserializationError(
            "BusinessSupportSubscriptionContract.plan_name required"
        )
    if data.get("contractStartDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["contract_start_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["contractStartDate"]
            )
        )
    else:
        raise DeserializationError(
            "BusinessSupportSubscriptionContract.contract_start_date required"
        )
    if data.get("contractEndDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["contract_end_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["contractEndDate"]
            )
        )
    else:
        raise DeserializationError(
            "BusinessSupportSubscriptionContract.contract_end_date required"
        )
    return out
