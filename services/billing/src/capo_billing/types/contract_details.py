"""Generated from Smithy shape ``com.amazonaws.billing#ContractDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError, SerializationError
from capo_billing.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_billing.types.private_pricing_addendum


class ContractDetailsPrivatePricingAddendumMember(TypedDict, closed=True):
    privatePricingAddendum: (
        "capo_billing.types.private_pricing_addendum.PrivatePricingAddendum"
    )


ContractDetails: TypeAlias = (
    ContractDetailsPrivatePricingAddendumMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContractDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ContractDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "privatePricingAddendum" in value:
        import capo_billing.types.private_pricing_addendum

        return {
            "privatePricingAddendum": capo_billing.types.private_pricing_addendum.serialize_aws_json_1_0(
                value["privatePricingAddendum"]
            )
        }
    else:
        raise SerializationError("ContractDetails: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ContractDetails:
    if data.get("privatePricingAddendum") is not None:
        import capo_billing.types.private_pricing_addendum

        return {
            "privatePricingAddendum": capo_billing.types.private_pricing_addendum.deserialize_aws_json_1_0(
                data["privatePricingAddendum"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ContractDetails: no recognized variant key")


def redact_sensitive(value: ContractDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "privatePricingAddendum" in value:
        import capo_billing.types.private_pricing_addendum

        out["privatePricingAddendum"] = (
            capo_billing.types.private_pricing_addendum.redact_sensitive(
                value["privatePricingAddendum"]
            )
        )
    return out
