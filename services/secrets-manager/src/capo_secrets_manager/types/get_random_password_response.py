"""Generated from Smithy shape ``com.amazonaws.secretsmanager#GetRandomPasswordResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.random_password_type


class GetRandomPasswordResponse(TypedDict, closed=True):
    random_password: NotRequired[
        "capo_secrets_manager.types.random_password_type.RandomPasswordType"
    ]
    """<p>A string with the password.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRandomPasswordResponse) -> dict:
    out: dict = {}
    if "random_password" in value:
        out["RandomPassword"] = value["random_password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRandomPasswordResponse:
    out: GetRandomPasswordResponse = {}  # type: ignore[typeddict-item]
    if data.get("RandomPassword") is not None:
        out["random_password"] = data["RandomPassword"]
    return out


def redact_sensitive(value: GetRandomPasswordResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "random_password" in value:
        out["random_password"] = "*** Sensitive Data Redacted ***"
    return out
