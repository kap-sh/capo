"""Generated from Smithy shape ``com.amazonaws.transcribe#LanguageOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.language_code

LanguageOptions: TypeAlias = list["capo_transcribe.types.language_code.LanguageCode"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LanguageOptions) -> list:
    import capo_transcribe.types.language_code

    out: list = []
    for item in value:
        out.append(capo_transcribe.types.language_code.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LanguageOptions:
    import capo_transcribe.types.language_code

    out: LanguageOptions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_transcribe.types.language_code.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LanguageOptions) -> list:
    import capo_transcribe.types.language_code

    out: list = []
    for item in value:
        out.append(capo_transcribe.types.language_code.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LanguageOptions:
    import capo_transcribe.types.language_code

    out: LanguageOptions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_transcribe.types.language_code.deserialize_cbor(item))
    return out
