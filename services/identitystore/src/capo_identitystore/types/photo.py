"""Generated from Smithy shape ``com.amazonaws.identitystore#Photo``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_identitystore.types.boolean_type
    import capo_identitystore.types.sensitive_string_type


class Photo(TypedDict, closed=True):
    value: "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    """<p>The photo data or URL. Supported formats include jpg, jpeg, png, and gif. This field is required for all photo entries.</p>"""
    type: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The type of photo. This field is optional and can be used to categorize different types of photos.</p>"""
    display: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A human-readable description of the photo for display purposes. This optional field provides context about the photo.</p>"""
    primary: "capo_identitystore.types.boolean_type.BooleanType"
    """<p>Specifies whether this is the user's primary photo. Default value is <code>false</code>. Only one photo can be designated as primary per user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Photo) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    if "type" in value:
        out["Type"] = value["type"]
    if "display" in value:
        out["Display"] = value["display"]
    out["Primary"] = value.get("primary", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> Photo:
    out: Photo = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Display") is not None:
        out["display"] = data["Display"]
    if data.get("Primary") is not None:
        out["primary"] = data["Primary"]
    else:
        out["primary"] = False
    return out


def redact_sensitive(value: Photo) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    if "display" in value:
        out["display"] = "*** Sensitive Data Redacted ***"
    return out
