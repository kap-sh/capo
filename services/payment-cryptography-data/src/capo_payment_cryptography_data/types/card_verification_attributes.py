"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#CardVerificationAttributes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.amex_card_security_code_version1
    import capo_payment_cryptography_data.types.amex_card_security_code_version2
    import capo_payment_cryptography_data.types.card_holder_verification_value
    import capo_payment_cryptography_data.types.card_verification_value1
    import capo_payment_cryptography_data.types.card_verification_value2
    import capo_payment_cryptography_data.types.discover_dynamic_card_verification_code
    import capo_payment_cryptography_data.types.dynamic_card_verification_code
    import capo_payment_cryptography_data.types.dynamic_card_verification_value


class CardVerificationAttributesAmexCardSecurityCodeVersion1Member(
    TypedDict, closed=True
):
    AmexCardSecurityCodeVersion1: "capo_payment_cryptography_data.types.amex_card_security_code_version1.AmexCardSecurityCodeVersion1"


class CardVerificationAttributesAmexCardSecurityCodeVersion2Member(
    TypedDict, closed=True
):
    AmexCardSecurityCodeVersion2: "capo_payment_cryptography_data.types.amex_card_security_code_version2.AmexCardSecurityCodeVersion2"


class CardVerificationAttributesCardVerificationValue1Member(TypedDict, closed=True):
    CardVerificationValue1: "capo_payment_cryptography_data.types.card_verification_value1.CardVerificationValue1"


class CardVerificationAttributesCardVerificationValue2Member(TypedDict, closed=True):
    CardVerificationValue2: "capo_payment_cryptography_data.types.card_verification_value2.CardVerificationValue2"


class CardVerificationAttributesCardHolderVerificationValueMember(
    TypedDict, closed=True
):
    CardHolderVerificationValue: "capo_payment_cryptography_data.types.card_holder_verification_value.CardHolderVerificationValue"


class CardVerificationAttributesDynamicCardVerificationCodeMember(
    TypedDict, closed=True
):
    DynamicCardVerificationCode: "capo_payment_cryptography_data.types.dynamic_card_verification_code.DynamicCardVerificationCode"


class CardVerificationAttributesDynamicCardVerificationValueMember(
    TypedDict, closed=True
):
    DynamicCardVerificationValue: "capo_payment_cryptography_data.types.dynamic_card_verification_value.DynamicCardVerificationValue"


class CardVerificationAttributesDiscoverDynamicCardVerificationCodeMember(
    TypedDict, closed=True
):
    DiscoverDynamicCardVerificationCode: "capo_payment_cryptography_data.types.discover_dynamic_card_verification_code.DiscoverDynamicCardVerificationCode"


CardVerificationAttributes: TypeAlias = (
    CardVerificationAttributesAmexCardSecurityCodeVersion1Member
    | CardVerificationAttributesAmexCardSecurityCodeVersion2Member
    | CardVerificationAttributesCardVerificationValue1Member
    | CardVerificationAttributesCardVerificationValue2Member
    | CardVerificationAttributesCardHolderVerificationValueMember
    | CardVerificationAttributesDynamicCardVerificationCodeMember
    | CardVerificationAttributesDynamicCardVerificationValueMember
    | CardVerificationAttributesDiscoverDynamicCardVerificationCodeMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CardVerificationAttributes) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CardVerificationAttributes: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "AmexCardSecurityCodeVersion1" in value:
        import capo_payment_cryptography_data.types.amex_card_security_code_version1

        return {
            "AmexCardSecurityCodeVersion1": capo_payment_cryptography_data.types.amex_card_security_code_version1.serialize_json(
                value["AmexCardSecurityCodeVersion1"]
            )
        }
    elif "AmexCardSecurityCodeVersion2" in value:
        import capo_payment_cryptography_data.types.amex_card_security_code_version2

        return {
            "AmexCardSecurityCodeVersion2": capo_payment_cryptography_data.types.amex_card_security_code_version2.serialize_json(
                value["AmexCardSecurityCodeVersion2"]
            )
        }
    elif "CardVerificationValue1" in value:
        import capo_payment_cryptography_data.types.card_verification_value1

        return {
            "CardVerificationValue1": capo_payment_cryptography_data.types.card_verification_value1.serialize_json(
                value["CardVerificationValue1"]
            )
        }
    elif "CardVerificationValue2" in value:
        import capo_payment_cryptography_data.types.card_verification_value2

        return {
            "CardVerificationValue2": capo_payment_cryptography_data.types.card_verification_value2.serialize_json(
                value["CardVerificationValue2"]
            )
        }
    elif "CardHolderVerificationValue" in value:
        import capo_payment_cryptography_data.types.card_holder_verification_value

        return {
            "CardHolderVerificationValue": capo_payment_cryptography_data.types.card_holder_verification_value.serialize_json(
                value["CardHolderVerificationValue"]
            )
        }
    elif "DynamicCardVerificationCode" in value:
        import capo_payment_cryptography_data.types.dynamic_card_verification_code

        return {
            "DynamicCardVerificationCode": capo_payment_cryptography_data.types.dynamic_card_verification_code.serialize_json(
                value["DynamicCardVerificationCode"]
            )
        }
    elif "DynamicCardVerificationValue" in value:
        import capo_payment_cryptography_data.types.dynamic_card_verification_value

        return {
            "DynamicCardVerificationValue": capo_payment_cryptography_data.types.dynamic_card_verification_value.serialize_json(
                value["DynamicCardVerificationValue"]
            )
        }
    elif "DiscoverDynamicCardVerificationCode" in value:
        import capo_payment_cryptography_data.types.discover_dynamic_card_verification_code

        return {
            "DiscoverDynamicCardVerificationCode": capo_payment_cryptography_data.types.discover_dynamic_card_verification_code.serialize_json(
                value["DiscoverDynamicCardVerificationCode"]
            )
        }
    else:
        raise SerializationError("CardVerificationAttributes: no variant present")


def deserialize_json(data: dict) -> CardVerificationAttributes:
    if data.get("AmexCardSecurityCodeVersion1") is not None:
        import capo_payment_cryptography_data.types.amex_card_security_code_version1

        return {
            "AmexCardSecurityCodeVersion1": capo_payment_cryptography_data.types.amex_card_security_code_version1.deserialize_json(
                data["AmexCardSecurityCodeVersion1"]
            )
        }
    elif data.get("AmexCardSecurityCodeVersion2") is not None:
        import capo_payment_cryptography_data.types.amex_card_security_code_version2

        return {
            "AmexCardSecurityCodeVersion2": capo_payment_cryptography_data.types.amex_card_security_code_version2.deserialize_json(
                data["AmexCardSecurityCodeVersion2"]
            )
        }
    elif data.get("CardVerificationValue1") is not None:
        import capo_payment_cryptography_data.types.card_verification_value1

        return {
            "CardVerificationValue1": capo_payment_cryptography_data.types.card_verification_value1.deserialize_json(
                data["CardVerificationValue1"]
            )
        }
    elif data.get("CardVerificationValue2") is not None:
        import capo_payment_cryptography_data.types.card_verification_value2

        return {
            "CardVerificationValue2": capo_payment_cryptography_data.types.card_verification_value2.deserialize_json(
                data["CardVerificationValue2"]
            )
        }
    elif data.get("CardHolderVerificationValue") is not None:
        import capo_payment_cryptography_data.types.card_holder_verification_value

        return {
            "CardHolderVerificationValue": capo_payment_cryptography_data.types.card_holder_verification_value.deserialize_json(
                data["CardHolderVerificationValue"]
            )
        }
    elif data.get("DynamicCardVerificationCode") is not None:
        import capo_payment_cryptography_data.types.dynamic_card_verification_code

        return {
            "DynamicCardVerificationCode": capo_payment_cryptography_data.types.dynamic_card_verification_code.deserialize_json(
                data["DynamicCardVerificationCode"]
            )
        }
    elif data.get("DynamicCardVerificationValue") is not None:
        import capo_payment_cryptography_data.types.dynamic_card_verification_value

        return {
            "DynamicCardVerificationValue": capo_payment_cryptography_data.types.dynamic_card_verification_value.deserialize_json(
                data["DynamicCardVerificationValue"]
            )
        }
    elif data.get("DiscoverDynamicCardVerificationCode") is not None:
        import capo_payment_cryptography_data.types.discover_dynamic_card_verification_code

        return {
            "DiscoverDynamicCardVerificationCode": capo_payment_cryptography_data.types.discover_dynamic_card_verification_code.deserialize_json(
                data["DiscoverDynamicCardVerificationCode"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "CardVerificationAttributes: no recognized variant key"
        )


def redact_sensitive(value: CardVerificationAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "AmexCardSecurityCodeVersion1" in value:
        import capo_payment_cryptography_data.types.amex_card_security_code_version1

        out["AmexCardSecurityCodeVersion1"] = (
            capo_payment_cryptography_data.types.amex_card_security_code_version1.redact_sensitive(
                value["AmexCardSecurityCodeVersion1"]
            )
        )
    if "AmexCardSecurityCodeVersion2" in value:
        import capo_payment_cryptography_data.types.amex_card_security_code_version2

        out["AmexCardSecurityCodeVersion2"] = (
            capo_payment_cryptography_data.types.amex_card_security_code_version2.redact_sensitive(
                value["AmexCardSecurityCodeVersion2"]
            )
        )
    if "CardVerificationValue1" in value:
        import capo_payment_cryptography_data.types.card_verification_value1

        out["CardVerificationValue1"] = (
            capo_payment_cryptography_data.types.card_verification_value1.redact_sensitive(
                value["CardVerificationValue1"]
            )
        )
    if "CardVerificationValue2" in value:
        import capo_payment_cryptography_data.types.card_verification_value2

        out["CardVerificationValue2"] = (
            capo_payment_cryptography_data.types.card_verification_value2.redact_sensitive(
                value["CardVerificationValue2"]
            )
        )
    if "DynamicCardVerificationCode" in value:
        import capo_payment_cryptography_data.types.dynamic_card_verification_code

        out["DynamicCardVerificationCode"] = (
            capo_payment_cryptography_data.types.dynamic_card_verification_code.redact_sensitive(
                value["DynamicCardVerificationCode"]
            )
        )
    if "DynamicCardVerificationValue" in value:
        import capo_payment_cryptography_data.types.dynamic_card_verification_value

        out["DynamicCardVerificationValue"] = (
            capo_payment_cryptography_data.types.dynamic_card_verification_value.redact_sensitive(
                value["DynamicCardVerificationValue"]
            )
        )
    if "DiscoverDynamicCardVerificationCode" in value:
        import capo_payment_cryptography_data.types.discover_dynamic_card_verification_code

        out["DiscoverDynamicCardVerificationCode"] = (
            capo_payment_cryptography_data.types.discover_dynamic_card_verification_code.redact_sensitive(
                value["DiscoverDynamicCardVerificationCode"]
            )
        )
    return out
