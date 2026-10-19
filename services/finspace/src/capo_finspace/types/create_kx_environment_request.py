"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.client_token
    import capo_finspace.types.description
    import capo_finspace.types.kms_key_arn
    import capo_finspace.types.kx_environment_name
    import capo_finspace.types.tag_map


class CreateKxEnvironmentRequest(TypedDict, closed=True):
    name: "capo_finspace.types.kx_environment_name.KxEnvironmentName"
    """<p>The name of the kdb environment that you want to create.</p>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p>A description for the kdb environment.</p>"""
    kms_key_id: "capo_finspace.types.kms_key_arn.KmsKeyARN"
    """<p>The KMS key ID to encrypt your data in the FinSpace environment.</p>"""
    tags: NotRequired["capo_finspace.types.tag_map.TagMap"]
    """<p>A list of key-value pairs to label the kdb environment. You can add up to 50 tags to your kdb environment.</p>"""
    client_token: NotRequired["capo_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxEnvironmentRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateKxEnvironmentRequest:
    out: CreateKxEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        out["kms_key_id"] = ""
    if data.get("tags") is not None:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
