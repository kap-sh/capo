"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#CreateMicrovmAuthTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.list_of_port_specification
    import capo_lambda_microvms.types.microvm_identifier
    import capo_lambda_microvms.types.positive_integer


class CreateMicrovmAuthTokenRequest(TypedDict, closed=True):
    microvm_identifier: (
        "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier"
    )
    """<p>The ID of the MicroVM to create an authentication token for.</p>"""
    expiration_in_minutes: "capo_lambda_microvms.types.positive_integer.PositiveInteger"
    """<p>The duration in minutes before the authentication token expires. Maximum: 60 minutes.</p>"""
    allowed_ports: (
        "capo_lambda_microvms.types.list_of_port_specification.ListOfPortSpecification"
    )
    """<p>The list of port specifications that the authentication token grants access to on the MicroVM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMicrovmAuthTokenRequest) -> dict:
    out: dict = {}
    out["expirationInMinutes"] = value["expiration_in_minutes"]
    import capo_lambda_microvms.types.list_of_port_specification

    out["allowedPorts"] = (
        capo_lambda_microvms.types.list_of_port_specification.serialize_json(
            value["allowed_ports"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateMicrovmAuthTokenRequest:
    out: CreateMicrovmAuthTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("expirationInMinutes") is not None:
        out["expiration_in_minutes"] = data["expirationInMinutes"]
    else:
        raise DeserializationError(
            "CreateMicrovmAuthTokenRequest.expiration_in_minutes required"
        )
    if data.get("allowedPorts") is not None:
        import capo_lambda_microvms.types.list_of_port_specification

        out["allowed_ports"] = (
            capo_lambda_microvms.types.list_of_port_specification.deserialize_json(
                data["allowedPorts"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMicrovmAuthTokenRequest.allowed_ports required"
        )
    return out
