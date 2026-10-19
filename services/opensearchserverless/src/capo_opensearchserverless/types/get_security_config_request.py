"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetSecurityConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.security_config_id


class GetSecurityConfigRequest(TypedDict, closed=True):
    id: "capo_opensearchserverless.types.security_config_id.SecurityConfigId"
    """<p>The unique identifier of the security configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSecurityConfigRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSecurityConfigRequest:
    out: GetSecurityConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
