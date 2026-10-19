"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#CreditCode``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_allocation_status
    import capo_partnercentral_benefits.types.monetary_value
    import capo_partnercentral_benefits.types.timestamp


class CreditCode(TypedDict, closed=True):
    aws_account_id: "str"
    """<p>The AWS account ID that the credit code is associated with or can be applied to.</p>"""
    value: "capo_partnercentral_benefits.types.monetary_value.MonetaryValue"
    """<p>The monetary value of the credit code.</p>"""
    aws_credit_code: "str"
    """<p>The actual credit code string that can be redeemed in the AWS billing console.</p>"""
    status: "capo_partnercentral_benefits.types.benefit_allocation_status.BenefitAllocationStatus"
    """<p>The current status of the credit code (e.g., active, redeemed, expired).</p>"""
    issued_at: "capo_partnercentral_benefits.types.timestamp.Timestamp"
    """<p>The timestamp when the credit code was issued.</p>"""
    expires_at: "capo_partnercentral_benefits.types.timestamp.Timestamp"
    """<p>The timestamp when the credit code expires and can no longer be redeemed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreditCode) -> dict:
    out: dict = {}
    out["AwsAccountId"] = value["aws_account_id"]
    import capo_partnercentral_benefits.types.monetary_value

    out["Value"] = (
        capo_partnercentral_benefits.types.monetary_value.serialize_aws_json_1_0(
            value["value"]
        )
    )
    out["AwsCreditCode"] = value["aws_credit_code"]
    import capo_partnercentral_benefits.types.benefit_allocation_status

    out["Status"] = (
        capo_partnercentral_benefits.types.benefit_allocation_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import capo_partnercentral_benefits.types.timestamp

    out["IssuedAt"] = (
        capo_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
            value["issued_at"]
        )
    )
    import capo_partnercentral_benefits.types.timestamp

    out["ExpiresAt"] = (
        capo_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
            value["expires_at"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreditCode:
    out: CreditCode = {}  # type: ignore[typeddict-item]
    if data.get("AwsAccountId") is not None:
        out["aws_account_id"] = data["AwsAccountId"]
    else:
        out["aws_account_id"] = ""
    if data.get("Value") is not None:
        import capo_partnercentral_benefits.types.monetary_value

        out["value"] = (
            capo_partnercentral_benefits.types.monetary_value.deserialize_aws_json_1_0(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("CreditCode.value required")
    if data.get("AwsCreditCode") is not None:
        out["aws_credit_code"] = data["AwsCreditCode"]
    else:
        out["aws_credit_code"] = ""
    if data.get("Status") is not None:
        import capo_partnercentral_benefits.types.benefit_allocation_status

        out["status"] = (
            capo_partnercentral_benefits.types.benefit_allocation_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_benefits.types.benefit_allocation_status.BenefitAllocationStatus",
            "",
        )
    if data.get("IssuedAt") is not None:
        import capo_partnercentral_benefits.types.timestamp

        out["issued_at"] = (
            capo_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["IssuedAt"]
            )
        )
    else:
        import datetime

        out["issued_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("ExpiresAt") is not None:
        import capo_partnercentral_benefits.types.timestamp

        out["expires_at"] = (
            capo_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["ExpiresAt"]
            )
        )
    else:
        import datetime

        out["expires_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
