"""Generated from Smithy shape ``com.amazonaws.translate#TerminologyData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.directionality
    import capo_translate.types.terminology_data_format
    import capo_translate.types.terminology_file


class TerminologyData(TypedDict, closed=True):
    file: "capo_translate.types.terminology_file.TerminologyFile"
    """<p>The file containing the custom terminology data. Your version of the AWS SDK performs a Base64-encoding on this field before sending a request to the AWS service. Users of the SDK should not perform Base64-encoding themselves.</p>"""
    format: "capo_translate.types.terminology_data_format.TerminologyDataFormat"
    """<p>The data format of the custom terminology.</p>"""
    directionality: NotRequired["capo_translate.types.directionality.Directionality"]
    """<p>The directionality of your terminology resource indicates whether it has one source language (uni-directional) or multiple (multi-directional).</p> <dl> <dt>UNI</dt> <dd> <p>The terminology resource has one source language (for example, the first column in a CSV file), and all of its other languages are target languages. </p> </dd> <dt>MULTI</dt> <dd> <p>Any language in the terminology resource can be the source language or a target language. A single multi-directional terminology resource can be used for jobs that translate different language pairs. For example, if the terminology contains English and Spanish terms, it can be used for jobs that translate English to Spanish and Spanish to English.</p> </dd> </dl> <p>When you create a custom terminology resource without specifying the directionality, it behaves as uni-directional terminology, although this parameter will have a null value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminologyData) -> dict:
    out: dict = {}
    import capo_translate.types.terminology_file

    out["File"] = capo_translate.types.terminology_file.serialize_aws_json_1_1(
        value["file"]
    )
    import capo_translate.types.terminology_data_format

    out["Format"] = capo_translate.types.terminology_data_format.serialize_aws_json_1_1(
        value["format"]
    )
    if "directionality" in value:
        import capo_translate.types.directionality

        out["Directionality"] = (
            capo_translate.types.directionality.serialize_aws_json_1_1(
                value["directionality"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminologyData:
    out: TerminologyData = {}  # type: ignore[typeddict-item]
    if data.get("File") is not None:
        import capo_translate.types.terminology_file

        out["file"] = capo_translate.types.terminology_file.deserialize_aws_json_1_1(
            data["File"]
        )
    else:
        out["file"] = b""
    if data.get("Format") is not None:
        import capo_translate.types.terminology_data_format

        out["format"] = (
            capo_translate.types.terminology_data_format.deserialize_aws_json_1_1(
                data["Format"]
            )
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_translate.types.terminology_data_format.TerminologyDataFormat", ""
        )
    if data.get("Directionality") is not None:
        import capo_translate.types.directionality

        out["directionality"] = (
            capo_translate.types.directionality.deserialize_aws_json_1_1(
                data["Directionality"]
            )
        )
    return out


def redact_sensitive(value: TerminologyData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file" in value:
        out["file"] = "*** Sensitive Data Redacted ***"
    return out
