"""Generated from Smithy shape ``com.amazonaws.signer#RevokeSigningProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signer.types.profile_name
    import capo_signer.types.profile_version
    import capo_signer.types.revocation_reason_string
    import capo_signer.types.timestamp


class RevokeSigningProfileRequest(TypedDict, closed=True):
    profile_name: "capo_signer.types.profile_name.ProfileName"
    """<p>The name of the signing profile to be revoked.</p>"""
    profile_version: "capo_signer.types.profile_version.ProfileVersion"
    """<p>The version of the signing profile to be revoked.</p>"""
    reason: "capo_signer.types.revocation_reason_string.RevocationReasonString"
    """<p>The reason for revoking a signing profile.</p>"""
    effective_time: "capo_signer.types.timestamp.Timestamp"
    """<p>A timestamp for when revocation of a Signing Profile should become effective. Signatures generated using the signing profile after this timestamp are not trusted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeSigningProfileRequest) -> dict:
    out: dict = {}
    out["profileVersion"] = value["profile_version"]
    out["reason"] = value["reason"]
    import capo_signer.types.timestamp

    out["effectiveTime"] = capo_signer.types.timestamp.serialize_json(
        value["effective_time"]
    )
    return out


def deserialize_json(data: dict) -> RevokeSigningProfileRequest:
    out: RevokeSigningProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("profileVersion") is not None:
        out["profile_version"] = data["profileVersion"]
    else:
        out["profile_version"] = ""
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        out["reason"] = ""
    if data.get("effectiveTime") is not None:
        import capo_signer.types.timestamp

        out["effective_time"] = capo_signer.types.timestamp.deserialize_json(
            data["effectiveTime"]
        )
    else:
        import datetime

        out["effective_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
