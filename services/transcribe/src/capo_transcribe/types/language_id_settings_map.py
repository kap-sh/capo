"""Generated from Smithy shape ``com.amazonaws.transcribe#LanguageIdSettingsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.language_code
    import capo_transcribe.types.language_id_settings

LanguageIdSettingsMap: TypeAlias = dict[
    "capo_transcribe.types.language_code.LanguageCode",
    "capo_transcribe.types.language_id_settings.LanguageIdSettings",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LanguageIdSettingsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_transcribe.types.language_code
        import capo_transcribe.types.language_id_settings

        out[capo_transcribe.types.language_code.serialize_aws_json_1_1(key)] = (
            capo_transcribe.types.language_id_settings.serialize_aws_json_1_1(value)
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LanguageIdSettingsMap:
    out: LanguageIdSettingsMap = {}
    for key, value in data.items():
        import capo_transcribe.types.language_code

        if value is None:
            continue
        import capo_transcribe.types.language_id_settings

        out[capo_transcribe.types.language_code.deserialize_aws_json_1_1(key)] = (
            capo_transcribe.types.language_id_settings.deserialize_aws_json_1_1(value)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: LanguageIdSettingsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_transcribe.types.language_code
        import capo_transcribe.types.language_id_settings

        out[capo_transcribe.types.language_code.serialize_cbor(key)] = (
            capo_transcribe.types.language_id_settings.serialize_cbor(value)
        )
    return out


def deserialize_cbor(data: dict) -> LanguageIdSettingsMap:
    out: LanguageIdSettingsMap = {}
    for key, value in data.items():
        import capo_transcribe.types.language_code

        if value is None:
            continue
        import capo_transcribe.types.language_id_settings

        out[capo_transcribe.types.language_code.deserialize_cbor(key)] = (
            capo_transcribe.types.language_id_settings.deserialize_cbor(value)
        )
    return out
