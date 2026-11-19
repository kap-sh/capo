"""Generated from Smithy shape ``com.amazonaws.workspaces#LoginMessage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.client_locale
    import capo_workspaces.types.client_login_message

LoginMessage: TypeAlias = dict[
    "capo_workspaces.types.client_locale.ClientLocale",
    "capo_workspaces.types.client_login_message.ClientLoginMessage",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LoginMessage) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> LoginMessage:
    out: LoginMessage = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: LoginMessage) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> LoginMessage:
    out: LoginMessage = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
