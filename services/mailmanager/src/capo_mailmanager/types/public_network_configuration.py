"""Generated from Smithy shape ``com.amazonaws.mailmanager#PublicNetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ip_type


class PublicNetworkConfiguration(TypedDict, closed=True):
    ip_type: "capo_mailmanager.types.ip_type.IpType"
    """<p>The IP address type for the public ingress point. Valid values are IPV4 and DUAL_STACK.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PublicNetworkConfiguration) -> dict:
    out: dict = {}
    import capo_mailmanager.types.ip_type

    out["IpType"] = capo_mailmanager.types.ip_type.serialize_aws_json_1_0(
        value.get("ip_type", "IPV4")
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PublicNetworkConfiguration:
    out: PublicNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("IpType") is not None:
        import capo_mailmanager.types.ip_type

        out["ip_type"] = capo_mailmanager.types.ip_type.deserialize_aws_json_1_0(
            data["IpType"]
        )
    else:
        out["ip_type"] = "IPV4"
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PublicNetworkConfiguration) -> dict:
    out: dict = {}
    import capo_mailmanager.types.ip_type

    out["IpType"] = capo_mailmanager.types.ip_type.serialize_cbor(
        value.get("ip_type", "IPV4")
    )
    return out


def deserialize_cbor(data: dict) -> PublicNetworkConfiguration:
    out: PublicNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("IpType") is not None:
        import capo_mailmanager.types.ip_type

        out["ip_type"] = capo_mailmanager.types.ip_type.deserialize_cbor(data["IpType"])
    else:
        out["ip_type"] = "IPV4"
    return out
