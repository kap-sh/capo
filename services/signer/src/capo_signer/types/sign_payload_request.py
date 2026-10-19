"""Generated from Smithy shape ``com.amazonaws.signer#SignPayloadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.account_id
    import capo_signer.types.payload
    import capo_signer.types.profile_name
    import capo_signer.types.string


class SignPayloadRequest(TypedDict, closed=True):
    profile_name: "capo_signer.types.profile_name.ProfileName"
    """<p>The name of the signing profile.</p>"""
    profile_owner: NotRequired["capo_signer.types.account_id.AccountId"]
    """<p>The AWS account ID of the profile owner.</p>"""
    payload: "capo_signer.types.payload.Payload"
    """<p>Specifies the object digest (hash) to sign.</p>"""
    payload_format: "capo_signer.types.string.String"
    """<p>Payload content type. The single valid type is <code>application/vnd.cncf.notary.payload.v1+json</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignPayloadRequest) -> dict:
    out: dict = {}
    out["profileName"] = value["profile_name"]
    if "profile_owner" in value:
        out["profileOwner"] = value["profile_owner"]
    import capo_signer.types.payload

    out["payload"] = capo_signer.types.payload.serialize_json(value["payload"])
    out["payloadFormat"] = value["payload_format"]
    return out


def deserialize_json(data: dict) -> SignPayloadRequest:
    out: SignPayloadRequest = {}  # type: ignore[typeddict-item]
    if data.get("profileName") is not None:
        out["profile_name"] = data["profileName"]
    else:
        out["profile_name"] = ""
    if data.get("profileOwner") is not None:
        out["profile_owner"] = data["profileOwner"]
    if data.get("payload") is not None:
        import capo_signer.types.payload

        out["payload"] = capo_signer.types.payload.deserialize_json(data["payload"])
    else:
        out["payload"] = b""
    if data.get("payloadFormat") is not None:
        out["payload_format"] = data["payloadFormat"]
    else:
        out["payload_format"] = ""
    return out
