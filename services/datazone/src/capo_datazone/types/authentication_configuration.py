"""Generated from Smithy shape ``com.amazonaws.datazone#AuthenticationConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.authentication_type
    import capo_datazone.types.o_auth2_properties


class AuthenticationConfiguration(TypedDict, closed=True):
    authentication_type: NotRequired[
        "capo_datazone.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type of a connection.</p>"""
    secret_arn: NotRequired["str"]
    """<p>The secret ARN of a connection.</p>"""
    o_auth2_properties: NotRequired[
        "capo_datazone.types.o_auth2_properties.OAuth2Properties"
    ]
    """<p>The oAuth2 properties of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationConfiguration) -> dict:
    out: dict = {}
    if "authentication_type" in value:
        import capo_datazone.types.authentication_type

        out["authenticationType"] = (
            capo_datazone.types.authentication_type.serialize_json(
                value["authentication_type"]
            )
        )
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    if "o_auth2_properties" in value:
        import capo_datazone.types.o_auth2_properties

        out["oAuth2Properties"] = capo_datazone.types.o_auth2_properties.serialize_json(
            value["o_auth2_properties"]
        )
    return out


def deserialize_json(data: dict) -> AuthenticationConfiguration:
    out: AuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("authenticationType") is not None:
        import capo_datazone.types.authentication_type

        out["authentication_type"] = (
            capo_datazone.types.authentication_type.deserialize_json(
                data["authenticationType"]
            )
        )
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    if data.get("oAuth2Properties") is not None:
        import capo_datazone.types.o_auth2_properties

        out["o_auth2_properties"] = (
            capo_datazone.types.o_auth2_properties.deserialize_json(
                data["oAuth2Properties"]
            )
        )
    return out


def redact_sensitive(value: AuthenticationConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "o_auth2_properties" in value:
        import capo_datazone.types.o_auth2_properties

        out["o_auth2_properties"] = (
            capo_datazone.types.o_auth2_properties.redact_sensitive(
                value["o_auth2_properties"]
            )
        )
    return out
