"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateTrustStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class CreateTrustStoreResponse(TypedDict, closed=True):
    trust_store_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrustStoreResponse) -> dict:
    out: dict = {}
    out["trustStoreArn"] = value["trust_store_arn"]
    return out


def deserialize_json(data: dict) -> CreateTrustStoreResponse:
    out: CreateTrustStoreResponse = {}  # type: ignore[typeddict-item]
    if data.get("trustStoreArn") is not None:
        out["trust_store_arn"] = data["trustStoreArn"]
    else:
        out["trust_store_arn"] = ""
    return out
