"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateTLSInspectionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.tls_inspection_configuration_response
    import capo_network_firewall.types.update_token


class UpdateTLSInspectionConfigurationResponse(TypedDict, closed=True):
    update_token: "capo_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the TLS inspection configuration. The token marks the state of the TLS inspection configuration resource at the time of the request. </p> <p>To make changes to the TLS inspection configuration, you provide the token in your request. Network Firewall uses the token to ensure that the TLS inspection configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the TLS inspection configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    tls_inspection_configuration_response: "capo_network_firewall.types.tls_inspection_configuration_response.TLSInspectionConfigurationResponse"
    """<p>The high-level properties of a TLS inspection configuration. This, along with the <a>TLSInspectionConfiguration</a>, define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling <a>DescribeTLSInspectionConfiguration</a>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTLSInspectionConfigurationResponse) -> dict:
    out: dict = {}
    out["UpdateToken"] = value["update_token"]
    import capo_network_firewall.types.tls_inspection_configuration_response

    out["TLSInspectionConfigurationResponse"] = (
        capo_network_firewall.types.tls_inspection_configuration_response.serialize_aws_json_1_0(
            value["tls_inspection_configuration_response"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTLSInspectionConfigurationResponse:
    out: UpdateTLSInspectionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    else:
        out["update_token"] = ""
    if data.get("TLSInspectionConfigurationResponse") is not None:
        import capo_network_firewall.types.tls_inspection_configuration_response

        out["tls_inspection_configuration_response"] = (
            capo_network_firewall.types.tls_inspection_configuration_response.deserialize_aws_json_1_0(
                data["TLSInspectionConfigurationResponse"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTLSInspectionConfigurationResponse.tls_inspection_configuration_response required"
        )
    return out
