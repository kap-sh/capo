"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeChannelDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.medical_scribe_channel_definition

MedicalScribeChannelDefinitions: TypeAlias = list[
    "capo_transcribe.types.medical_scribe_channel_definition.MedicalScribeChannelDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeChannelDefinitions) -> list:
    import capo_transcribe.types.medical_scribe_channel_definition

    out: list = []
    for item in value:
        out.append(
            capo_transcribe.types.medical_scribe_channel_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MedicalScribeChannelDefinitions:
    import capo_transcribe.types.medical_scribe_channel_definition

    out: MedicalScribeChannelDefinitions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transcribe.types.medical_scribe_channel_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MedicalScribeChannelDefinitions) -> list:
    import capo_transcribe.types.medical_scribe_channel_definition

    out: list = []
    for item in value:
        out.append(
            capo_transcribe.types.medical_scribe_channel_definition.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> MedicalScribeChannelDefinitions:
    import capo_transcribe.types.medical_scribe_channel_definition

    out: MedicalScribeChannelDefinitions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transcribe.types.medical_scribe_channel_definition.deserialize_cbor(
                item
            )
        )
    return out
