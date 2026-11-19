"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentReadFeatureTypes``."""

from typing import Literal, TypeAlias, cast

"""<p>TABLES or FORMS</p>"""
DocumentReadFeatureTypes: TypeAlias = Literal[
    "TABLES",
    "FORMS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentReadFeatureTypes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentReadFeatureTypes:
    return cast(DocumentReadFeatureTypes, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentReadFeatureTypes) -> str:
    return value


def deserialize_cbor(data: str) -> DocumentReadFeatureTypes:
    return cast(DocumentReadFeatureTypes, data)
