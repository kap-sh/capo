"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteTLSInspectionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.tls_inspection_configuration_response


class DeleteTLSInspectionConfigurationResponse(TypedDict, closed=True):
    tls_inspection_configuration_response: "capo_network_firewall.types.tls_inspection_configuration_response.TLSInspectionConfigurationResponse"
    """<p>The high-level properties of a TLS inspection configuration. This, along with the <a>TLSInspectionConfiguration</a>, define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling <a>DescribeTLSInspectionConfiguration</a>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTLSInspectionConfigurationResponse) -> dict:
    out: dict = {}
    import capo_network_firewall.types.tls_inspection_configuration_response

    out["TLSInspectionConfigurationResponse"] = (
        capo_network_firewall.types.tls_inspection_configuration_response.serialize_aws_json_1_0(
            value["tls_inspection_configuration_response"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTLSInspectionConfigurationResponse:
    out: DeleteTLSInspectionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("TLSInspectionConfigurationResponse") is not None:
        import capo_network_firewall.types.tls_inspection_configuration_response

        out["tls_inspection_configuration_response"] = (
            capo_network_firewall.types.tls_inspection_configuration_response.deserialize_aws_json_1_0(
                data["TLSInspectionConfigurationResponse"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteTLSInspectionConfigurationResponse.tls_inspection_configuration_response required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteTLSInspectionConfigurationResponse) -> dict:
    out: dict = {}
    import capo_network_firewall.types.tls_inspection_configuration_response

    out["TLSInspectionConfigurationResponse"] = (
        capo_network_firewall.types.tls_inspection_configuration_response.serialize_cbor(
            value["tls_inspection_configuration_response"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> DeleteTLSInspectionConfigurationResponse:
    out: DeleteTLSInspectionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("TLSInspectionConfigurationResponse") is not None:
        import capo_network_firewall.types.tls_inspection_configuration_response

        out["tls_inspection_configuration_response"] = (
            capo_network_firewall.types.tls_inspection_configuration_response.deserialize_cbor(
                data["TLSInspectionConfigurationResponse"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteTLSInspectionConfigurationResponse.tls_inspection_configuration_response required"
        )
    return out
