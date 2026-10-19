"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataAccessorAuthenticationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.data_accessor_authentication_configuration
    import capo_qbusiness.types.data_accessor_authentication_type
    import capo_qbusiness.types.data_accessor_external_ids


class DataAccessorAuthenticationDetail(TypedDict, closed=True):
    authentication_type: "capo_qbusiness.types.data_accessor_authentication_type.DataAccessorAuthenticationType"
    """<p>The type of authentication to use for the data accessor. This determines how the ISV authenticates when accessing data. You can use one of two authentication types:</p> <ul> <li> <p> <code>AWS_IAM_IDC_TTI</code> - Authentication using IAM Identity Center Trusted Token Issuer (TTI). This authentication type allows the ISV to use a trusted token issuer to generate tokens for accessing the data.</p> </li> <li> <p> <code>AWS_IAM_IDC_AUTH_CODE</code> - Authentication using IAM Identity Center authorization code flow. This authentication type uses the standard OAuth 2.0 authorization code flow for authentication.</p> </li> </ul>"""
    authentication_configuration: NotRequired[
        "capo_qbusiness.types.data_accessor_authentication_configuration.DataAccessorAuthenticationConfiguration"
    ]
    """<p>The specific authentication configuration based on the authentication type.</p>"""
    external_ids: NotRequired[
        "capo_qbusiness.types.data_accessor_external_ids.DataAccessorExternalIds"
    ]
    """<p>A list of external identifiers associated with this authentication configuration. These are used to correlate the data accessor with external systems.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataAccessorAuthenticationDetail) -> dict:
    out: dict = {}
    import capo_qbusiness.types.data_accessor_authentication_type

    out["authenticationType"] = (
        capo_qbusiness.types.data_accessor_authentication_type.serialize_json(
            value["authentication_type"]
        )
    )
    if "authentication_configuration" in value:
        import capo_qbusiness.types.data_accessor_authentication_configuration

        out["authenticationConfiguration"] = (
            capo_qbusiness.types.data_accessor_authentication_configuration.serialize_json(
                value["authentication_configuration"]
            )
        )
    if "external_ids" in value:
        import capo_qbusiness.types.data_accessor_external_ids

        out["externalIds"] = (
            capo_qbusiness.types.data_accessor_external_ids.serialize_json(
                value["external_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataAccessorAuthenticationDetail:
    out: DataAccessorAuthenticationDetail = {}  # type: ignore[typeddict-item]
    if data.get("authenticationType") is not None:
        import capo_qbusiness.types.data_accessor_authentication_type

        out["authentication_type"] = (
            capo_qbusiness.types.data_accessor_authentication_type.deserialize_json(
                data["authenticationType"]
            )
        )
    else:
        import typing

        out["authentication_type"] = typing.cast(
            "capo_qbusiness.types.data_accessor_authentication_type.DataAccessorAuthenticationType",
            "",
        )
    if data.get("authenticationConfiguration") is not None:
        import capo_qbusiness.types.data_accessor_authentication_configuration

        out["authentication_configuration"] = (
            capo_qbusiness.types.data_accessor_authentication_configuration.deserialize_json(
                data["authenticationConfiguration"]
            )
        )
    if data.get("externalIds") is not None:
        import capo_qbusiness.types.data_accessor_external_ids

        out["external_ids"] = (
            capo_qbusiness.types.data_accessor_external_ids.deserialize_json(
                data["externalIds"]
            )
        )
    return out
