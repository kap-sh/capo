"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#TermTemplate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_agreement.errors import DeserializationError, SerializationError
from capo_marketplace_agreement.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.payment_schedule_term_template


class TermTemplatePaymentScheduleTermTemplateMember(TypedDict, closed=True):
    paymentScheduleTermTemplate: "capo_marketplace_agreement.types.payment_schedule_term_template.PaymentScheduleTermTemplate"


TermTemplate: TypeAlias = (
    TermTemplatePaymentScheduleTermTemplateMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TermTemplate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TermTemplate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "paymentScheduleTermTemplate" in value:
        import capo_marketplace_agreement.types.payment_schedule_term_template

        return {
            "paymentScheduleTermTemplate": capo_marketplace_agreement.types.payment_schedule_term_template.serialize_aws_json_1_0(
                value["paymentScheduleTermTemplate"]
            )
        }
    else:
        raise SerializationError("TermTemplate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> TermTemplate:
    if data.get("paymentScheduleTermTemplate") is not None:
        import capo_marketplace_agreement.types.payment_schedule_term_template

        return {
            "paymentScheduleTermTemplate": capo_marketplace_agreement.types.payment_schedule_term_template.deserialize_aws_json_1_0(
                data["paymentScheduleTermTemplate"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TermTemplate: no recognized variant key")
