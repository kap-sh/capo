"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#Challenge``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pca_connector_scep.types.challenge_arn
    import capo_pca_connector_scep.types.connector_arn
    import capo_pca_connector_scep.types.sensitive_string


class Challenge(TypedDict, closed=True):
    arn: NotRequired["capo_pca_connector_scep.types.challenge_arn.ChallengeArn"]
    """<p>The Amazon Resource Name (ARN) of the challenge.</p>"""
    connector_arn: NotRequired[
        "capo_pca_connector_scep.types.connector_arn.ConnectorArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the challenge was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the challenge was updated.</p>"""
    password: NotRequired[
        "capo_pca_connector_scep.types.sensitive_string.SensitiveString"
    ]
    """<p>The SCEP challenge password, in UUID format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Challenge) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "created_at" in value:
        import capo_pca_connector_scep.types._prelude.timestamp

        out["CreatedAt"] = (
            capo_pca_connector_scep.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_pca_connector_scep.types._prelude.timestamp

        out["UpdatedAt"] = (
            capo_pca_connector_scep.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    if "password" in value:
        out["Password"] = value["password"]
    return out


def deserialize_json(data: dict) -> Challenge:
    out: Challenge = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ConnectorArn") is not None:
        out["connector_arn"] = data["ConnectorArn"]
    if data.get("CreatedAt") is not None:
        import capo_pca_connector_scep.types._prelude.timestamp

        out["created_at"] = (
            capo_pca_connector_scep.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_pca_connector_scep.types._prelude.timestamp

        out["updated_at"] = (
            capo_pca_connector_scep.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    return out


def redact_sensitive(value: Challenge) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
