"""Generated from Smithy shape ``com.amazonaws.memorydb#AuthenticationMode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.input_authentication_type
    import capo_memorydb.types.password_list_input


class AuthenticationMode(TypedDict, closed=True):
    type: NotRequired[
        "capo_memorydb.types.input_authentication_type.InputAuthenticationType"
    ]
    """<p>Indicates whether the user requires a password to authenticate. All newly-created users require a password.</p>"""
    passwords: NotRequired["capo_memorydb.types.password_list_input.PasswordListInput"]
    """<p>The password(s) used for authentication</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationMode) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_memorydb.types.input_authentication_type

        out["Type"] = (
            capo_memorydb.types.input_authentication_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "passwords" in value:
        import capo_memorydb.types.password_list_input

        out["Passwords"] = (
            capo_memorydb.types.password_list_input.serialize_aws_json_1_1(
                value["passwords"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationMode:
    out: AuthenticationMode = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_memorydb.types.input_authentication_type

        out["type"] = (
            capo_memorydb.types.input_authentication_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Passwords") is not None:
        import capo_memorydb.types.password_list_input

        out["passwords"] = (
            capo_memorydb.types.password_list_input.deserialize_aws_json_1_1(
                data["Passwords"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AuthenticationMode) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_memorydb.types.input_authentication_type

        out["Type"] = capo_memorydb.types.input_authentication_type.serialize_cbor(
            value["type"]
        )
    if "passwords" in value:
        import capo_memorydb.types.password_list_input

        out["Passwords"] = capo_memorydb.types.password_list_input.serialize_cbor(
            value["passwords"]
        )
    return out


def deserialize_cbor(data: dict) -> AuthenticationMode:
    out: AuthenticationMode = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_memorydb.types.input_authentication_type

        out["type"] = capo_memorydb.types.input_authentication_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("Passwords") is not None:
        import capo_memorydb.types.password_list_input

        out["passwords"] = capo_memorydb.types.password_list_input.deserialize_cbor(
            data["Passwords"]
        )
    return out
