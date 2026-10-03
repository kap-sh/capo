"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#PublicKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.public_key_arn
    import capo_ivs_realtime.types.public_key_fingerprint
    import capo_ivs_realtime.types.public_key_material
    import capo_ivs_realtime.types.public_key_name
    import capo_ivs_realtime.types.tags


class PublicKey(TypedDict, closed=True):
    arn: NotRequired["capo_ivs_realtime.types.public_key_arn.PublicKeyArn"]
    """<p>Public key ARN.</p>"""
    name: NotRequired["capo_ivs_realtime.types.public_key_name.PublicKeyName"]
    """<p>Public key name.</p>"""
    public_key_material: NotRequired[
        "capo_ivs_realtime.types.public_key_material.PublicKeyMaterial"
    ]
    """<p>Public key material.</p>"""
    fingerprint: NotRequired[
        "capo_ivs_realtime.types.public_key_fingerprint.PublicKeyFingerprint"
    ]
    """<p>The public key fingerprint, a short string used to identify or verify the full public key.</p>"""
    tags: NotRequired["capo_ivs_realtime.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublicKey) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "public_key_material" in value:
        out["publicKeyMaterial"] = value["public_key_material"]
    if "fingerprint" in value:
        out["fingerprint"] = value["fingerprint"]
    if "tags" in value:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PublicKey:
    out: PublicKey = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("publicKeyMaterial") is not None:
        out["public_key_material"] = data["publicKeyMaterial"]
    if data.get("fingerprint") is not None:
        out["fingerprint"] = data["fingerprint"]
    if data.get("tags") is not None:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
