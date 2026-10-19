"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateSMBLocalGroupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.smb_local_groups


class UpdateSMBLocalGroupsInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    smb_local_groups: "capo_storage_gateway.types.smb_local_groups.SMBLocalGroups"
    """<p>A list of Active Directory users and groups that you want to grant special permissions for SMB file shares on the gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSMBLocalGroupsInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    import capo_storage_gateway.types.smb_local_groups

    out["SMBLocalGroups"] = (
        capo_storage_gateway.types.smb_local_groups.serialize_aws_json_1_1(
            value["smb_local_groups"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSMBLocalGroupsInput:
    out: UpdateSMBLocalGroupsInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("SMBLocalGroups") is not None:
        import capo_storage_gateway.types.smb_local_groups

        out["smb_local_groups"] = (
            capo_storage_gateway.types.smb_local_groups.deserialize_aws_json_1_1(
                data["SMBLocalGroups"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSMBLocalGroupsInput.smb_local_groups required"
        )
    return out
