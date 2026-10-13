"""Generated from Smithy shape ``com.amazonaws.lightsail#Session``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.sensitive_non_empty_string


class Session(TypedDict, closed=True):
    name: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The session name.</p>"""
    url: NotRequired[
        "capo_lightsail.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The session URL.</p>"""
    is_primary: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>When true, this Boolean value indicates the primary session for the specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Session) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "url" in value:
        out["url"] = value["url"]
    if "is_primary" in value:
        out["isPrimary"] = value["is_primary"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("isPrimary") is not None:
        out["is_primary"] = data["isPrimary"]
    return out


def redact_sensitive(value: Session) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
