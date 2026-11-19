"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#DocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.document_item

DocumentList: TypeAlias = list[
    "capo_marketplace_agreement.types.document_item.DocumentItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DocumentList) -> list:
    import capo_marketplace_agreement.types.document_item

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.document_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DocumentList:
    import capo_marketplace_agreement.types.document_item

    out: DocumentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.document_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentList) -> list:
    import capo_marketplace_agreement.types.document_item

    out: list = []
    for item in value:
        out.append(capo_marketplace_agreement.types.document_item.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DocumentList:
    import capo_marketplace_agreement.types.document_item

    out: DocumentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.document_item.deserialize_cbor(item)
        )
    return out
