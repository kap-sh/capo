"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeTLSInspectionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class DescribeTLSInspectionConfigurationRequest(TypedDict, closed=True):
    tls_inspection_configuration_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the TLS inspection configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    tls_inspection_configuration_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeTLSInspectionConfigurationRequest) -> dict:
    out: dict = {}
    if "tls_inspection_configuration_arn" in value:
        out["TLSInspectionConfigurationArn"] = value["tls_inspection_configuration_arn"]
    if "tls_inspection_configuration_name" in value:
        out["TLSInspectionConfigurationName"] = value[
            "tls_inspection_configuration_name"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeTLSInspectionConfigurationRequest:
    out: DescribeTLSInspectionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("TLSInspectionConfigurationArn") is not None:
        out["tls_inspection_configuration_arn"] = data["TLSInspectionConfigurationArn"]
    if data.get("TLSInspectionConfigurationName") is not None:
        out["tls_inspection_configuration_name"] = data[
            "TLSInspectionConfigurationName"
        ]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeTLSInspectionConfigurationRequest) -> dict:
    out: dict = {}
    if "tls_inspection_configuration_arn" in value:
        out["TLSInspectionConfigurationArn"] = value["tls_inspection_configuration_arn"]
    if "tls_inspection_configuration_name" in value:
        out["TLSInspectionConfigurationName"] = value[
            "tls_inspection_configuration_name"
        ]
    return out


def deserialize_cbor(data: dict) -> DescribeTLSInspectionConfigurationRequest:
    out: DescribeTLSInspectionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("TLSInspectionConfigurationArn") is not None:
        out["tls_inspection_configuration_arn"] = data["TLSInspectionConfigurationArn"]
    if data.get("TLSInspectionConfigurationName") is not None:
        out["tls_inspection_configuration_name"] = data[
            "TLSInspectionConfigurationName"
        ]
    return out
