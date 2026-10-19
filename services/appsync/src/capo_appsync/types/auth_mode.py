"""Generated from Smithy shape ``com.amazonaws.appsync#AuthMode``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.authentication_type


class AuthMode(TypedDict, closed=True):
    auth_type: "capo_appsync.types.authentication_type.AuthenticationType"
    """<p>The authorization type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthMode) -> dict:
    out: dict = {}
    import capo_appsync.types.authentication_type

    out["authType"] = capo_appsync.types.authentication_type.serialize_json(
        value["auth_type"]
    )
    return out


def deserialize_json(data: dict) -> AuthMode:
    out: AuthMode = {}  # type: ignore[typeddict-item]
    if data.get("authType") is not None:
        import capo_appsync.types.authentication_type

        out["auth_type"] = capo_appsync.types.authentication_type.deserialize_json(
            data["authType"]
        )
    else:
        import typing

        out["auth_type"] = typing.cast(
            "capo_appsync.types.authentication_type.AuthenticationType", ""
        )
    return out
