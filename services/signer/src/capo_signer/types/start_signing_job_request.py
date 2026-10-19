"""Generated from Smithy shape ``com.amazonaws.signer#StartSigningJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_signer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signer.types.account_id
    import capo_signer.types.client_request_token
    import capo_signer.types.destination
    import capo_signer.types.profile_name
    import capo_signer.types.source


class StartSigningJobRequest(TypedDict, closed=True):
    source: "capo_signer.types.source.Source"
    """<p>The S3 bucket that contains the object to sign or a BLOB that contains your raw code.</p>"""
    destination: "capo_signer.types.destination.Destination"
    """<p>The S3 bucket in which to save your signed object. The destination contains the name of your bucket and an optional prefix.</p>"""
    profile_name: "capo_signer.types.profile_name.ProfileName"
    """<p>The name of the signing profile.</p>"""
    client_request_token: "capo_signer.types.client_request_token.ClientRequestToken"
    """<p>String that identifies the signing request. All calls after the first that use this token return the same response as the first call.</p>"""
    profile_owner: NotRequired["capo_signer.types.account_id.AccountId"]
    """<p>The AWS account ID of the signing profile owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSigningJobRequest) -> dict:
    out: dict = {}
    import capo_signer.types.source

    out["source"] = capo_signer.types.source.serialize_json(value["source"])
    import capo_signer.types.destination

    out["destination"] = capo_signer.types.destination.serialize_json(
        value["destination"]
    )
    out["profileName"] = value["profile_name"]
    out["clientRequestToken"] = value["client_request_token"]
    if "profile_owner" in value:
        out["profileOwner"] = value["profile_owner"]
    return out


def deserialize_json(data: dict) -> StartSigningJobRequest:
    out: StartSigningJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_signer.types.source

        out["source"] = capo_signer.types.source.deserialize_json(data["source"])
    else:
        raise DeserializationError("StartSigningJobRequest.source required")
    if data.get("destination") is not None:
        import capo_signer.types.destination

        out["destination"] = capo_signer.types.destination.deserialize_json(
            data["destination"]
        )
    else:
        raise DeserializationError("StartSigningJobRequest.destination required")
    if data.get("profileName") is not None:
        out["profile_name"] = data["profileName"]
    else:
        out["profile_name"] = ""
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    else:
        out["client_request_token"] = ""
    if data.get("profileOwner") is not None:
        out["profile_owner"] = data["profileOwner"]
    return out
