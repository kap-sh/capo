"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CheckIngestedDocumentAclResponse``."""

from typing_extensions import TypedDict


class CheckIngestedDocumentAclResponse(TypedDict, closed=True):
    has_access: "bool"
    """<p>Specifies whether the user has access to the document based on the ingested access control list (ACL). Returns <code>true</code> if the user is allowed access, and <code>false</code> otherwise.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckIngestedDocumentAclResponse) -> dict:
    out: dict = {}
    out["hasAccess"] = value["has_access"]
    return out


def deserialize_json(data: dict) -> CheckIngestedDocumentAclResponse:
    out: CheckIngestedDocumentAclResponse = {}  # type: ignore[typeddict-item]
    if data.get("hasAccess") is not None:
        out["has_access"] = data["hasAccess"]
    else:
        out["has_access"] = False
    return out
