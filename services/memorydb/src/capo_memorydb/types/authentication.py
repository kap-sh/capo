"""Generated from Smithy shape ``com.amazonaws.memorydb#Authentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.authentication_type
    import capo_memorydb.types.integer_optional


class Authentication(TypedDict, closed=True):
    type: NotRequired["capo_memorydb.types.authentication_type.AuthenticationType"]
    """<p>Indicates whether the user requires a password to authenticate.</p>"""
    password_count: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The number of passwords belonging to the user. The maximum is two.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Authentication) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_memorydb.types.authentication_type

        out["Type"] = capo_memorydb.types.authentication_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "password_count" in value:
        out["PasswordCount"] = value["password_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Authentication:
    out: Authentication = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_memorydb.types.authentication_type

        out["type"] = capo_memorydb.types.authentication_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("PasswordCount") is not None:
        out["password_count"] = data["PasswordCount"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Authentication) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_memorydb.types.authentication_type

        out["Type"] = capo_memorydb.types.authentication_type.serialize_cbor(
            value["type"]
        )
    if "password_count" in value:
        out["PasswordCount"] = value["password_count"]
    return out


def deserialize_cbor(data: dict) -> Authentication:
    out: Authentication = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_memorydb.types.authentication_type

        out["type"] = capo_memorydb.types.authentication_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("PasswordCount") is not None:
        out["password_count"] = data["PasswordCount"]
    return out
