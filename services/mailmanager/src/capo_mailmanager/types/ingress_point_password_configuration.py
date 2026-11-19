"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointPasswordConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class IngressPointPasswordConfiguration(TypedDict, closed=True):
    smtp_password_version: NotRequired["str"]
    """<p>The current password expiry timestamp of the ingress endpoint resource.</p>"""
    previous_smtp_password_version: NotRequired["str"]
    """<p>The previous password version of the ingress endpoint resource.</p>"""
    previous_smtp_password_expiry_timestamp: NotRequired["datetime.datetime"]
    """<p>The previous password expiry timestamp of the ingress endpoint resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressPointPasswordConfiguration) -> dict:
    out: dict = {}
    if "smtp_password_version" in value:
        out["SmtpPasswordVersion"] = value["smtp_password_version"]
    if "previous_smtp_password_version" in value:
        out["PreviousSmtpPasswordVersion"] = value["previous_smtp_password_version"]
    if "previous_smtp_password_expiry_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["PreviousSmtpPasswordExpiryTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["previous_smtp_password_expiry_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressPointPasswordConfiguration:
    out: IngressPointPasswordConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SmtpPasswordVersion") is not None:
        out["smtp_password_version"] = data["SmtpPasswordVersion"]
    if data.get("PreviousSmtpPasswordVersion") is not None:
        out["previous_smtp_password_version"] = data["PreviousSmtpPasswordVersion"]
    if data.get("PreviousSmtpPasswordExpiryTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["previous_smtp_password_expiry_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["PreviousSmtpPasswordExpiryTimestamp"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressPointPasswordConfiguration) -> dict:
    out: dict = {}
    if "smtp_password_version" in value:
        out["SmtpPasswordVersion"] = value["smtp_password_version"]
    if "previous_smtp_password_version" in value:
        out["PreviousSmtpPasswordVersion"] = value["previous_smtp_password_version"]
    if "previous_smtp_password_expiry_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["PreviousSmtpPasswordExpiryTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_cbor(
                value["previous_smtp_password_expiry_timestamp"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> IngressPointPasswordConfiguration:
    out: IngressPointPasswordConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SmtpPasswordVersion") is not None:
        out["smtp_password_version"] = data["SmtpPasswordVersion"]
    if data.get("PreviousSmtpPasswordVersion") is not None:
        out["previous_smtp_password_version"] = data["PreviousSmtpPasswordVersion"]
    if data.get("PreviousSmtpPasswordExpiryTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["previous_smtp_password_expiry_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_cbor(
                data["PreviousSmtpPasswordExpiryTimestamp"]
            )
        )
    return out
