"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#EncryptionSetting``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.file_password
    import capo_lex_models_v2.types.kms_key_arn


class EncryptionSetting(TypedDict, closed=True):
    kms_key_arn: NotRequired["capo_lex_models_v2.types.kms_key_arn.KmsKeyArn"]
    """<p>The KMS key ARN used to encrypt the metadata associated with the bot recommendation.</p>"""
    bot_locale_export_password: NotRequired[
        "capo_lex_models_v2.types.file_password.FilePassword"
    ]
    """<p>The password used to encrypt the recommended bot recommendation file.</p>"""
    associated_transcripts_password: NotRequired[
        "capo_lex_models_v2.types.file_password.FilePassword"
    ]
    """<p>The password used to encrypt the associated transcript file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionSetting) -> dict:
    out: dict = {}
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "bot_locale_export_password" in value:
        out["botLocaleExportPassword"] = value["bot_locale_export_password"]
    if "associated_transcripts_password" in value:
        out["associatedTranscriptsPassword"] = value["associated_transcripts_password"]
    return out


def deserialize_json(data: dict) -> EncryptionSetting:
    out: EncryptionSetting = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("botLocaleExportPassword") is not None:
        out["bot_locale_export_password"] = data["botLocaleExportPassword"]
    if data.get("associatedTranscriptsPassword") is not None:
        out["associated_transcripts_password"] = data["associatedTranscriptsPassword"]
    return out


def redact_sensitive(value: EncryptionSetting) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bot_locale_export_password" in value:
        out["bot_locale_export_password"] = "*** Sensitive Data Redacted ***"
    if "associated_transcripts_password" in value:
        out["associated_transcripts_password"] = "*** Sensitive Data Redacted ***"
    return out
