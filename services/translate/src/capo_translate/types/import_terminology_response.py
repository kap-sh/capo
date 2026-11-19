"""Generated from Smithy shape ``com.amazonaws.translate#ImportTerminologyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.terminology_data_location
    import capo_translate.types.terminology_properties


class ImportTerminologyResponse(TypedDict, closed=True):
    terminology_properties: NotRequired[
        "capo_translate.types.terminology_properties.TerminologyProperties"
    ]
    """<p>The properties of the custom terminology being imported.</p>"""
    auxiliary_data_location: NotRequired[
        "capo_translate.types.terminology_data_location.TerminologyDataLocation"
    ]
    """<p>The Amazon S3 location of a file that provides any errors or warnings that were produced by your input file. This file was created when Amazon Translate attempted to create a terminology resource. The location is returned as a presigned URL to that has a 30 minute expiration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportTerminologyResponse) -> dict:
    out: dict = {}
    if "terminology_properties" in value:
        import capo_translate.types.terminology_properties

        out["TerminologyProperties"] = (
            capo_translate.types.terminology_properties.serialize_aws_json_1_1(
                value["terminology_properties"]
            )
        )
    if "auxiliary_data_location" in value:
        import capo_translate.types.terminology_data_location

        out["AuxiliaryDataLocation"] = (
            capo_translate.types.terminology_data_location.serialize_aws_json_1_1(
                value["auxiliary_data_location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportTerminologyResponse:
    out: ImportTerminologyResponse = {}  # type: ignore[typeddict-item]
    if data.get("TerminologyProperties") is not None:
        import capo_translate.types.terminology_properties

        out["terminology_properties"] = (
            capo_translate.types.terminology_properties.deserialize_aws_json_1_1(
                data["TerminologyProperties"]
            )
        )
    if data.get("AuxiliaryDataLocation") is not None:
        import capo_translate.types.terminology_data_location

        out["auxiliary_data_location"] = (
            capo_translate.types.terminology_data_location.deserialize_aws_json_1_1(
                data["AuxiliaryDataLocation"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImportTerminologyResponse) -> dict:
    out: dict = {}
    if "terminology_properties" in value:
        import capo_translate.types.terminology_properties

        out["TerminologyProperties"] = (
            capo_translate.types.terminology_properties.serialize_cbor(
                value["terminology_properties"]
            )
        )
    if "auxiliary_data_location" in value:
        import capo_translate.types.terminology_data_location

        out["AuxiliaryDataLocation"] = (
            capo_translate.types.terminology_data_location.serialize_cbor(
                value["auxiliary_data_location"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ImportTerminologyResponse:
    out: ImportTerminologyResponse = {}  # type: ignore[typeddict-item]
    if data.get("TerminologyProperties") is not None:
        import capo_translate.types.terminology_properties

        out["terminology_properties"] = (
            capo_translate.types.terminology_properties.deserialize_cbor(
                data["TerminologyProperties"]
            )
        )
    if data.get("AuxiliaryDataLocation") is not None:
        import capo_translate.types.terminology_data_location

        out["auxiliary_data_location"] = (
            capo_translate.types.terminology_data_location.deserialize_cbor(
                data["AuxiliaryDataLocation"]
            )
        )
    return out
