"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#EndTimeBehavior``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.end_time_behavior_reason_code
    import capo_marketplace_agreement.types.end_time_behavior_type
    import capo_marketplace_agreement.types.renewal_summary


class EndTimeBehavior(TypedDict, closed=True):
    type: "capo_marketplace_agreement.types.end_time_behavior_type.EndTimeBehaviorType"
    """<p>The behavior of the agreement when it reaches its end date.</p> <p>Types include:</p> <ul> <li> <p> <code>RENEW</code> – A new agreement is created from the accepted terms of this agreement.</p> </li> <li> <p> <code>REPLACE</code> – A new agreement is created from a different offer than the one this agreement was created from. This happens, for example, when a private offer reaches its end date and the acceptor transitions to the public offer for the product.</p> </li> <li> <p> <code>EXPIRE</code> – The agreement ends and isn't renewed or replaced.</p> </li> </ul>"""
    reason_code: NotRequired[
        "capo_marketplace_agreement.types.end_time_behavior_reason_code.EndTimeBehaviorReasonCode"
    ]
    """<p>The reason why the agreement doesn't renew at its end date. The field is <code>null</code> when the agreement renews.</p> <p>More than one reason can apply to the same agreement. When that happens, the operation returns only one reason code, and <code>PROPOSER_RENEW_OPTED_OUT</code> takes precedence over all others.</p> <p>The <code>EnableAutoRenew</code> field reflects only the acceptor's preference, and doesn't reflect the other reasons an agreement might not renew.</p> <p>Reason codes include:</p> <ul> <li> <p> <code>PROPOSER_RENEW_OPTED_OUT</code> – The proposer opted out of renewing the agreement.</p> </li> <li> <p> <code>ACCEPTOR_RENEW_OPTED_OUT</code> – The acceptor opted out of renewing the agreement.</p> </li> <li> <p> <code>NO_RENEWAL_TERM</code> – The accepted terms of the agreement don't include a renewal term, which is required for an agreement to renew.</p> </li> <li> <p> <code>RENEWAL_LIMIT_EXHAUSTED</code> – The agreement reached the maximum number of renewals allowed by its renewal term.</p> </li> </ul>"""
    renewal_summary: NotRequired[
        "capo_marketplace_agreement.types.renewal_summary.RenewalSummary"
    ]
    """<p>The details of the renewal that applies at the end date of the agreement. This field is present when <code>Type</code> is <code>RENEW</code>. It is also present when <code>ReasonCode</code> is <code>PROPOSER_RENEW_OPTED_OUT</code> or <code>ACCEPTOR_RENEW_OPTED_OUT</code>. In those cases, it identifies the offer that the agreement would otherwise have renewed from. The field is <code>null</code> in all other cases.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EndTimeBehavior) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.end_time_behavior_type

    out["type"] = (
        capo_marketplace_agreement.types.end_time_behavior_type.serialize_aws_json_1_0(
            value["type"]
        )
    )
    if "reason_code" in value:
        import capo_marketplace_agreement.types.end_time_behavior_reason_code

        out["reasonCode"] = (
            capo_marketplace_agreement.types.end_time_behavior_reason_code.serialize_aws_json_1_0(
                value["reason_code"]
            )
        )
    if "renewal_summary" in value:
        import capo_marketplace_agreement.types.renewal_summary

        out["renewalSummary"] = (
            capo_marketplace_agreement.types.renewal_summary.serialize_aws_json_1_0(
                value["renewal_summary"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EndTimeBehavior:
    out: EndTimeBehavior = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_marketplace_agreement.types.end_time_behavior_type

        out["type"] = (
            capo_marketplace_agreement.types.end_time_behavior_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_marketplace_agreement.types.end_time_behavior_type.EndTimeBehaviorType",
            "",
        )
    if data.get("reasonCode") is not None:
        import capo_marketplace_agreement.types.end_time_behavior_reason_code

        out["reason_code"] = (
            capo_marketplace_agreement.types.end_time_behavior_reason_code.deserialize_aws_json_1_0(
                data["reasonCode"]
            )
        )
    if data.get("renewalSummary") is not None:
        import capo_marketplace_agreement.types.renewal_summary

        out["renewal_summary"] = (
            capo_marketplace_agreement.types.renewal_summary.deserialize_aws_json_1_0(
                data["renewalSummary"]
            )
        )
    return out
