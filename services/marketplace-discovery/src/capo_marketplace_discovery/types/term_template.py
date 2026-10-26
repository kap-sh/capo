"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#TermTemplate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError, SerializationError
from capo_marketplace_discovery.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.payment_schedule_term_template


class _TermTemplate_paymentScheduleTermTemplate(TypedDict, closed=True):
    paymentScheduleTermTemplate: "capo_marketplace_discovery.types.payment_schedule_term_template.PaymentScheduleTermTemplate"


TermTemplate: TypeAlias = _TermTemplate_paymentScheduleTermTemplate | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: TermTemplate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TermTemplate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "paymentScheduleTermTemplate" in value:
        import capo_marketplace_discovery.types.payment_schedule_term_template

        return {
            "paymentScheduleTermTemplate": capo_marketplace_discovery.types.payment_schedule_term_template.serialize_json(
                value["paymentScheduleTermTemplate"]
            )
        }
    else:
        raise SerializationError("TermTemplate: no variant present")


def deserialize_json(data: dict) -> TermTemplate:
    if data.get("paymentScheduleTermTemplate") is not None:
        import capo_marketplace_discovery.types.payment_schedule_term_template

        return {
            "paymentScheduleTermTemplate": capo_marketplace_discovery.types.payment_schedule_term_template.deserialize_json(
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
