"""Generated from Smithy shape ``com.amazonaws.appstream#VpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.security_group_id_list
    import capo_appstream.types.subnet_id_list


class VpcConfig(TypedDict, closed=True):
    subnet_ids: NotRequired["capo_appstream.types.subnet_id_list.SubnetIdList"]
    """<p>The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.</p>"""
    security_group_ids: NotRequired[
        "capo_appstream.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The identifiers of the security groups for the fleet or image builder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfig) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import capo_appstream.types.subnet_id_list

        out["SubnetIds"] = capo_appstream.types.subnet_id_list.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_appstream.types.security_group_id_list

        out["SecurityGroupIds"] = (
            capo_appstream.types.security_group_id_list.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if data.get("SubnetIds") is not None:
        import capo_appstream.types.subnet_id_list

        out["subnet_ids"] = (
            capo_appstream.types.subnet_id_list.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    if data.get("SecurityGroupIds") is not None:
        import capo_appstream.types.security_group_id_list

        out["security_group_ids"] = (
            capo_appstream.types.security_group_id_list.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VpcConfig) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import capo_appstream.types.subnet_id_list

        out["SubnetIds"] = capo_appstream.types.subnet_id_list.serialize_cbor(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_appstream.types.security_group_id_list

        out["SecurityGroupIds"] = (
            capo_appstream.types.security_group_id_list.serialize_cbor(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if data.get("SubnetIds") is not None:
        import capo_appstream.types.subnet_id_list

        out["subnet_ids"] = capo_appstream.types.subnet_id_list.deserialize_cbor(
            data["SubnetIds"]
        )
    if data.get("SecurityGroupIds") is not None:
        import capo_appstream.types.security_group_id_list

        out["security_group_ids"] = (
            capo_appstream.types.security_group_id_list.deserialize_cbor(
                data["SecurityGroupIds"]
            )
        )
    return out
