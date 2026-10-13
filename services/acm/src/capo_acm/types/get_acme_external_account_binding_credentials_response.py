"""Generated from Smithy shape ``com.amazonaws.acm#GetAcmeExternalAccountBindingCredentialsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.mac_key


class GetAcmeExternalAccountBindingCredentialsResponse(TypedDict, closed=True):
    key_id: NotRequired["str"]
    """<p>The key identifier for the external account binding credentials.</p>"""
    mac_key: NotRequired["capo_acm.types.mac_key.MacKey"]
    """<p>The MAC key for the external account binding credentials.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetAcmeExternalAccountBindingCredentialsResponse,
) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "mac_key" in value:
        out["MacKey"] = value["mac_key"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetAcmeExternalAccountBindingCredentialsResponse:
    out: GetAcmeExternalAccountBindingCredentialsResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("MacKey") is not None:
        out["mac_key"] = data["MacKey"]
    return out


def redact_sensitive(
    value: GetAcmeExternalAccountBindingCredentialsResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "mac_key" in value:
        out["mac_key"] = "*** Sensitive Data Redacted ***"
    return out
