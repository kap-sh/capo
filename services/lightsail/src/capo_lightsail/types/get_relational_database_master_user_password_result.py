"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseMasterUserPasswordResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.sensitive_string


class GetRelationalDatabaseMasterUserPasswordResult(TypedDict, closed=True):
    master_user_password: NotRequired[
        "capo_lightsail.types.sensitive_string.SensitiveString"
    ]
    """<p>The master user password for the <code>password version</code> specified.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the specified version of the master user password was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetRelationalDatabaseMasterUserPasswordResult,
) -> dict:
    out: dict = {}
    if "master_user_password" in value:
        out["masterUserPassword"] = value["master_user_password"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetRelationalDatabaseMasterUserPasswordResult:
    out: GetRelationalDatabaseMasterUserPasswordResult = {}  # type: ignore[typeddict-item]
    if data.get("masterUserPassword") is not None:
        out["master_user_password"] = data["masterUserPassword"]
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    return out


def redact_sensitive(
    value: GetRelationalDatabaseMasterUserPasswordResult,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "master_user_password" in value:
        out["master_user_password"] = "*** Sensitive Data Redacted ***"
    return out
