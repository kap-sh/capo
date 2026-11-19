"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ValidationExceptionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.validation_exception_field

ValidationExceptionFieldList: TypeAlias = list[
    "capo_marketplace_agreement.types.validation_exception_field.ValidationExceptionField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionFieldList) -> list:
    import capo_marketplace_agreement.types.validation_exception_field

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.validation_exception_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ValidationExceptionFieldList:
    import capo_marketplace_agreement.types.validation_exception_field

    out: ValidationExceptionFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.validation_exception_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidationExceptionFieldList) -> list:
    import capo_marketplace_agreement.types.validation_exception_field

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.validation_exception_field.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ValidationExceptionFieldList:
    import capo_marketplace_agreement.types.validation_exception_field

    out: ValidationExceptionFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.validation_exception_field.deserialize_cbor(
                item
            )
        )
    return out
