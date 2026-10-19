"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateTrustStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class AssociateTrustStoreResponse(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    trust_store_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateTrustStoreResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["trustStoreArn"] = value["trust_store_arn"]
    return out


def deserialize_json(data: dict) -> AssociateTrustStoreResponse:
    out: AssociateTrustStoreResponse = {}  # type: ignore[typeddict-item]
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    else:
        out["portal_arn"] = ""
    if data.get("trustStoreArn") is not None:
        out["trust_store_arn"] = data["trustStoreArn"]
    else:
        out["trust_store_arn"] = ""
    return out
