"""Generated from Smithy shape ``com.amazonaws.transcribe#ContentRedaction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.pii_entity_types
    import capo_transcribe.types.redaction_output
    import capo_transcribe.types.redaction_type


class ContentRedaction(TypedDict, closed=True):
    redaction_type: "capo_transcribe.types.redaction_type.RedactionType"
    """<p>Specify the category of information you want to redact; <code>PII</code> (personally identifiable information) is the only valid value. You can use <code>PiiEntityTypes</code> to choose which types of PII you want to redact. If you do not include <code>PiiEntityTypes</code> in your request, all PII is redacted.</p>"""
    redaction_output: "capo_transcribe.types.redaction_output.RedactionOutput"
    """<p>Specify if you want only a redacted transcript, or if you want a redacted and an unredacted transcript.</p> <p>When you choose <code>redacted</code> Amazon Transcribe creates only a redacted transcript.</p> <p>When you choose <code>redacted_and_unredacted</code> Amazon Transcribe creates a redacted and an unredacted transcript (as two separate files).</p>"""
    pii_entity_types: NotRequired[
        "capo_transcribe.types.pii_entity_types.PiiEntityTypes"
    ]
    """<p>Specify which types of personally identifiable information (PII) you want to redact in your transcript. You can include as many types as you'd like, or you can select <code>ALL</code>. If you do not include <code>PiiEntityTypes</code> in your request, all PII is redacted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentRedaction) -> dict:
    out: dict = {}
    import capo_transcribe.types.redaction_type

    out["RedactionType"] = capo_transcribe.types.redaction_type.serialize_aws_json_1_1(
        value["redaction_type"]
    )
    import capo_transcribe.types.redaction_output

    out["RedactionOutput"] = (
        capo_transcribe.types.redaction_output.serialize_aws_json_1_1(
            value["redaction_output"]
        )
    )
    if "pii_entity_types" in value:
        import capo_transcribe.types.pii_entity_types

        out["PiiEntityTypes"] = (
            capo_transcribe.types.pii_entity_types.serialize_aws_json_1_1(
                value["pii_entity_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContentRedaction:
    out: ContentRedaction = {}  # type: ignore[typeddict-item]
    if data.get("RedactionType") is not None:
        import capo_transcribe.types.redaction_type

        out["redaction_type"] = (
            capo_transcribe.types.redaction_type.deserialize_aws_json_1_1(
                data["RedactionType"]
            )
        )
    else:
        import typing

        out["redaction_type"] = typing.cast(
            "capo_transcribe.types.redaction_type.RedactionType", ""
        )
    if data.get("RedactionOutput") is not None:
        import capo_transcribe.types.redaction_output

        out["redaction_output"] = (
            capo_transcribe.types.redaction_output.deserialize_aws_json_1_1(
                data["RedactionOutput"]
            )
        )
    else:
        import typing

        out["redaction_output"] = typing.cast(
            "capo_transcribe.types.redaction_output.RedactionOutput", ""
        )
    if data.get("PiiEntityTypes") is not None:
        import capo_transcribe.types.pii_entity_types

        out["pii_entity_types"] = (
            capo_transcribe.types.pii_entity_types.deserialize_aws_json_1_1(
                data["PiiEntityTypes"]
            )
        )
    return out
