"""Generated from Smithy shape ``com.amazonaws.signer#AddProfilePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_signer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signer.types.profile_name
    import capo_signer.types.profile_version
    import capo_signer.types.string


class AddProfilePermissionRequest(TypedDict, closed=True):
    profile_name: "capo_signer.types.profile_name.ProfileName"
    """<p>The human-readable name of the signing profile.</p>"""
    profile_version: NotRequired["capo_signer.types.profile_version.ProfileVersion"]
    """<p>The version of the signing profile.</p>"""
    action: "capo_signer.types.string.String"
    """<p>For cross-account signing. Grant a designated account permission to perform one or more of the following actions. Each action is associated with a specific API's operations. For more information about cross-account signing, see <a href="http://docs.aws.amazon.com/signer/latest/developerguide/signing-profile-cross-account.html">Using cross-account signing with signing profiles</a> in the <i>AWS Signer Developer Guide</i>.</p> <p>You can designate the following actions to an account.</p> <ul> <li> <p> <code>signer:StartSigningJob</code>. This action isn't supported for container image workflows. For details, see <a>StartSigningJob</a>.</p> </li> <li> <p> <code>signer:SignPayload</code>. This action isn't supported for AWS Lambda workflows. For details, see <a>SignPayload</a> </p> </li> <li> <p> <code>signer:GetSigningProfile</code>. For details, see <a>GetSigningProfile</a>.</p> </li> <li> <p> <code>signer:RevokeSignature</code>. For details, see <a>RevokeSignature</a>.</p> </li> </ul>"""
    principal: "capo_signer.types.string.String"
    """<p>The AWS principal receiving cross-account permissions. This may be an IAM role or another AWS account ID.</p>"""
    revision_id: NotRequired["capo_signer.types.string.String"]
    """<p>A unique identifier for the current profile revision.</p>"""
    statement_id: "capo_signer.types.string.String"
    """<p>A unique identifier for the cross-account permission statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddProfilePermissionRequest) -> dict:
    out: dict = {}
    if "profile_version" in value:
        out["profileVersion"] = value["profile_version"]
    out["action"] = value["action"]
    out["principal"] = value["principal"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    out["statementId"] = value["statement_id"]
    return out


def deserialize_json(data: dict) -> AddProfilePermissionRequest:
    out: AddProfilePermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("profileVersion") is not None:
        out["profile_version"] = data["profileVersion"]
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        raise DeserializationError("AddProfilePermissionRequest.action required")
    if data.get("principal") is not None:
        out["principal"] = data["principal"]
    else:
        raise DeserializationError("AddProfilePermissionRequest.principal required")
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    if data.get("statementId") is not None:
        out["statement_id"] = data["statementId"]
    else:
        raise DeserializationError("AddProfilePermissionRequest.statement_id required")
    return out
