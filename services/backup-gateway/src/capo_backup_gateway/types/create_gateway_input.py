"""Generated from Smithy shape ``com.amazonaws.backupgateway#CreateGatewayInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.activation_key
    import capo_backup_gateway.types.gateway_type
    import capo_backup_gateway.types.name
    import capo_backup_gateway.types.tags


class CreateGatewayInput(TypedDict, closed=True):
    activation_key: "capo_backup_gateway.types.activation_key.ActivationKey"
    """<p>The activation key of the created gateway.</p>"""
    gateway_display_name: "capo_backup_gateway.types.name.Name"
    """<p>The display name of the created gateway.</p>"""
    gateway_type: "capo_backup_gateway.types.gateway_type.GatewayType"
    """<p>The type of created gateway.</p>"""
    tags: NotRequired["capo_backup_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags to assign to the gateway. Each tag is a key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateGatewayInput) -> dict:
    out: dict = {}
    out["ActivationKey"] = value["activation_key"]
    out["GatewayDisplayName"] = value["gateway_display_name"]
    out["GatewayType"] = value["gateway_type"]
    if "tags" in value:
        import capo_backup_gateway.types.tags

        out["Tags"] = capo_backup_gateway.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateGatewayInput:
    out: CreateGatewayInput = {}  # type: ignore[typeddict-item]
    if data.get("ActivationKey") is not None:
        out["activation_key"] = data["ActivationKey"]
    else:
        out["activation_key"] = ""
    if data.get("GatewayDisplayName") is not None:
        out["gateway_display_name"] = data["GatewayDisplayName"]
    else:
        out["gateway_display_name"] = ""
    if data.get("GatewayType") is not None:
        out["gateway_type"] = data["GatewayType"]
    else:
        out["gateway_type"] = ""
    if data.get("Tags") is not None:
        import capo_backup_gateway.types.tags

        out["tags"] = capo_backup_gateway.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
