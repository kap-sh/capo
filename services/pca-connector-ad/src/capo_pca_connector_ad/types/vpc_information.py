"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#VpcInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.ip_address_type
    import capo_pca_connector_ad.types.security_group_id_list


class VpcInformation(TypedDict, closed=True):
    ip_address_type: NotRequired[
        "capo_pca_connector_ad.types.ip_address_type.IpAddressType"
    ]
    """<p>The VPC IP address type.</p>"""
    security_group_ids: (
        "capo_pca_connector_ad.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The security groups used with the connector. You can use a maximum of 4 security groups with a connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcInformation) -> dict:
    out: dict = {}
    if "ip_address_type" in value:
        import capo_pca_connector_ad.types.ip_address_type

        out["IpAddressType"] = (
            capo_pca_connector_ad.types.ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    import capo_pca_connector_ad.types.security_group_id_list

    out["SecurityGroupIds"] = (
        capo_pca_connector_ad.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> VpcInformation:
    out: VpcInformation = {}  # type: ignore[typeddict-item]
    if data.get("IpAddressType") is not None:
        import capo_pca_connector_ad.types.ip_address_type

        out["ip_address_type"] = (
            capo_pca_connector_ad.types.ip_address_type.deserialize_json(
                data["IpAddressType"]
            )
        )
    if data.get("SecurityGroupIds") is not None:
        import capo_pca_connector_ad.types.security_group_id_list

        out["security_group_ids"] = (
            capo_pca_connector_ad.types.security_group_id_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    else:
        out["security_group_ids"] = []
    return out
