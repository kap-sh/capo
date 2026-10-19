"""Generated from Smithy shape ``com.amazonaws.glue#ConnectorAuthenticationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.authentication_types
    import capo_glue.types.basic_authentication_properties
    import capo_glue.types.connector_o_auth2_properties
    import capo_glue.types.custom_authentication_properties


class ConnectorAuthenticationConfiguration(TypedDict, closed=True):
    authentication_types: "capo_glue.types.authentication_types.AuthenticationTypes"
    """<p>A list of authentication types supported by this connection type, such as Basic, OAuth2, or Custom authentication methods.</p>"""
    o_auth2_properties: NotRequired[
        "capo_glue.types.connector_o_auth2_properties.ConnectorOAuth2Properties"
    ]
    basic_authentication_properties: NotRequired[
        "capo_glue.types.basic_authentication_properties.BasicAuthenticationProperties"
    ]
    custom_authentication_properties: NotRequired[
        "capo_glue.types.custom_authentication_properties.CustomAuthenticationProperties"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorAuthenticationConfiguration) -> dict:
    out: dict = {}
    import capo_glue.types.authentication_types

    out["AuthenticationTypes"] = (
        capo_glue.types.authentication_types.serialize_aws_json_1_1(
            value["authentication_types"]
        )
    )
    if "o_auth2_properties" in value:
        import capo_glue.types.connector_o_auth2_properties

        out["OAuth2Properties"] = (
            capo_glue.types.connector_o_auth2_properties.serialize_aws_json_1_1(
                value["o_auth2_properties"]
            )
        )
    if "basic_authentication_properties" in value:
        import capo_glue.types.basic_authentication_properties

        out["BasicAuthenticationProperties"] = (
            capo_glue.types.basic_authentication_properties.serialize_aws_json_1_1(
                value["basic_authentication_properties"]
            )
        )
    if "custom_authentication_properties" in value:
        import capo_glue.types.custom_authentication_properties

        out["CustomAuthenticationProperties"] = (
            capo_glue.types.custom_authentication_properties.serialize_aws_json_1_1(
                value["custom_authentication_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorAuthenticationConfiguration:
    out: ConnectorAuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AuthenticationTypes") is not None:
        import capo_glue.types.authentication_types

        out["authentication_types"] = (
            capo_glue.types.authentication_types.deserialize_aws_json_1_1(
                data["AuthenticationTypes"]
            )
        )
    else:
        out["authentication_types"] = []
    if data.get("OAuth2Properties") is not None:
        import capo_glue.types.connector_o_auth2_properties

        out["o_auth2_properties"] = (
            capo_glue.types.connector_o_auth2_properties.deserialize_aws_json_1_1(
                data["OAuth2Properties"]
            )
        )
    if data.get("BasicAuthenticationProperties") is not None:
        import capo_glue.types.basic_authentication_properties

        out["basic_authentication_properties"] = (
            capo_glue.types.basic_authentication_properties.deserialize_aws_json_1_1(
                data["BasicAuthenticationProperties"]
            )
        )
    if data.get("CustomAuthenticationProperties") is not None:
        import capo_glue.types.custom_authentication_properties

        out["custom_authentication_properties"] = (
            capo_glue.types.custom_authentication_properties.deserialize_aws_json_1_1(
                data["CustomAuthenticationProperties"]
            )
        )
    return out
