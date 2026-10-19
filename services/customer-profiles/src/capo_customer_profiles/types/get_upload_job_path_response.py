"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetUploadJobPathResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.string_to2048
    import capo_customer_profiles.types.text
    import capo_customer_profiles.types.timestamp


class GetUploadJobPathResponse(TypedDict, closed=True):
    url: "capo_customer_profiles.types.string_to2048.stringTo2048"
    """<p>The pre-signed S3 URL for uploading the CSV file associated with the upload job. </p>"""
    client_token: NotRequired["capo_customer_profiles.types.text.text"]
    """<p>The plaintext data key used to encrypt the upload file. </p> <p>To persist to the pre-signed url, use the client token and MD5 client token as header. The required headers are as follows: </p> <ul> <li> <p>x-amz-server-side-encryption-customer-key: Client Token </p> </li> <li> <p>x-amz-server-side-encryption-customer-key-MD5: MD5 Client Token </p> </li> <li> <p>x-amz-server-side-encryption-customer-algorithm: AES256 </p> </li> </ul>"""
    valid_until: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The expiry timestamp for the pre-signed URL, after which the URL will no longer be valid. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUploadJobPathResponse) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "valid_until" in value:
        import capo_customer_profiles.types.timestamp

        out["ValidUntil"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["valid_until"]
        )
    return out


def deserialize_json(data: dict) -> GetUploadJobPathResponse:
    out: GetUploadJobPathResponse = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        out["url"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ValidUntil") is not None:
        import capo_customer_profiles.types.timestamp

        out["valid_until"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["ValidUntil"]
        )
    return out
