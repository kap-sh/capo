"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateUsagePlanKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class CreateUsagePlanKeyRequest(TypedDict, closed=True):
    usage_plan_id: "capo_api_gateway.types.string.String"
    """<p>The Id of the UsagePlan resource representing the usage plan containing the to-be-created UsagePlanKey resource representing a plan customer.</p>"""
    key_id: "capo_api_gateway.types.string.String"
    """<p>The identifier of a UsagePlanKey resource for a plan customer.</p>"""
    key_type: "capo_api_gateway.types.string.String"
    """<p>The type of a UsagePlanKey resource for a plan customer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUsagePlanKeyRequest) -> dict:
    out: dict = {}
    out["keyId"] = value["key_id"]
    out["keyType"] = value["key_type"]
    return out


def deserialize_json(data: dict) -> CreateUsagePlanKeyRequest:
    out: CreateUsagePlanKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("keyId") is not None:
        out["key_id"] = data["keyId"]
    else:
        out["key_id"] = ""
    if data.get("keyType") is not None:
        out["key_type"] = data["keyType"]
    else:
        out["key_type"] = ""
    return out
