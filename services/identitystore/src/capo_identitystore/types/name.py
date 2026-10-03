"""Generated from Smithy shape ``com.amazonaws.identitystore#Name``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_identitystore.types.sensitive_string_type


class Name(TypedDict, closed=True):
    formatted: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing a formatted version of the name for display.</p>"""
    family_name: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The family name of the user.</p>"""
    given_name: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The given name of the user.</p>"""
    middle_name: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The middle name of the user.</p>"""
    honorific_prefix: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The honorific prefix of the user. For example, "Dr."</p>"""
    honorific_suffix: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The honorific suffix of the user. For example, "M.D."</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Name) -> dict:
    out: dict = {}
    if "formatted" in value:
        out["Formatted"] = value["formatted"]
    if "family_name" in value:
        out["FamilyName"] = value["family_name"]
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "middle_name" in value:
        out["MiddleName"] = value["middle_name"]
    if "honorific_prefix" in value:
        out["HonorificPrefix"] = value["honorific_prefix"]
    if "honorific_suffix" in value:
        out["HonorificSuffix"] = value["honorific_suffix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Name:
    out: Name = {}  # type: ignore[typeddict-item]
    if data.get("Formatted") is not None:
        out["formatted"] = data["Formatted"]
    if data.get("FamilyName") is not None:
        out["family_name"] = data["FamilyName"]
    if data.get("GivenName") is not None:
        out["given_name"] = data["GivenName"]
    if data.get("MiddleName") is not None:
        out["middle_name"] = data["MiddleName"]
    if data.get("HonorificPrefix") is not None:
        out["honorific_prefix"] = data["HonorificPrefix"]
    if data.get("HonorificSuffix") is not None:
        out["honorific_suffix"] = data["HonorificSuffix"]
    return out
