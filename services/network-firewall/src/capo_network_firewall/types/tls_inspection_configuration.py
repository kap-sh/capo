"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TLSInspectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.server_certificate_configurations


class TLSInspectionConfiguration(TypedDict, closed=True):
    server_certificate_configurations: NotRequired[
        "capo_network_firewall.types.server_certificate_configurations.ServerCertificateConfigurations"
    ]
    """<p>Lists the server certificate configurations that are associated with the TLS configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TLSInspectionConfiguration) -> dict:
    out: dict = {}
    if "server_certificate_configurations" in value:
        import capo_network_firewall.types.server_certificate_configurations

        out["ServerCertificateConfigurations"] = (
            capo_network_firewall.types.server_certificate_configurations.serialize_aws_json_1_0(
                value["server_certificate_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TLSInspectionConfiguration:
    out: TLSInspectionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ServerCertificateConfigurations") is not None:
        import capo_network_firewall.types.server_certificate_configurations

        out["server_certificate_configurations"] = (
            capo_network_firewall.types.server_certificate_configurations.deserialize_aws_json_1_0(
                data["ServerCertificateConfigurations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TLSInspectionConfiguration) -> dict:
    out: dict = {}
    if "server_certificate_configurations" in value:
        import capo_network_firewall.types.server_certificate_configurations

        out["ServerCertificateConfigurations"] = (
            capo_network_firewall.types.server_certificate_configurations.serialize_cbor(
                value["server_certificate_configurations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> TLSInspectionConfiguration:
    out: TLSInspectionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ServerCertificateConfigurations") is not None:
        import capo_network_firewall.types.server_certificate_configurations

        out["server_certificate_configurations"] = (
            capo_network_firewall.types.server_certificate_configurations.deserialize_cbor(
                data["ServerCertificateConfigurations"]
            )
        )
    return out
