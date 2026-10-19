"""Generated from Smithy shape ``com.amazonaws.identitystore#Filter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_identitystore.types.attribute_path
    import capo_identitystore.types.sensitive_string_type


class Filter(TypedDict, closed=True):
    attribute_path: "capo_identitystore.types.attribute_path.AttributePath"
    """<p>The attribute path that is used to specify which attribute name to search. Length limit is 255 characters. For example, <code>UserName</code> is a valid attribute path for the <code> ListUsers</code> API, and <code>DisplayName</code> is a valid attribute path for the <code> ListGroups</code> API.</p>"""
    attribute_value: (
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    )
    """<p>Represents the data for an attribute. Each attribute value is described as a name-value pair. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    out["AttributePath"] = value["attribute_path"]
    out["AttributeValue"] = value["attribute_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("AttributePath") is not None:
        out["attribute_path"] = data["AttributePath"]
    else:
        out["attribute_path"] = ""
    if data.get("AttributeValue") is not None:
        out["attribute_value"] = data["AttributeValue"]
    else:
        out["attribute_value"] = ""
    return out


def redact_sensitive(value: Filter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attribute_value" in value:
        out["attribute_value"] = "*** Sensitive Data Redacted ***"
    return out
