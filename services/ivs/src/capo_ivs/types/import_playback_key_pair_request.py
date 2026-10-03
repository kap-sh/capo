"""Generated from Smithy shape ``com.amazonaws.ivs#ImportPlaybackKeyPairRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.playback_key_pair_name
    import capo_ivs.types.playback_public_key_material
    import capo_ivs.types.tags


class ImportPlaybackKeyPairRequest(TypedDict, closed=True):
    public_key_material: (
        "capo_ivs.types.playback_public_key_material.PlaybackPublicKeyMaterial"
    )
    """<p>The public portion of a customer-generated key pair.</p>"""
    name: NotRequired["capo_ivs.types.playback_key_pair_name.PlaybackKeyPairName"]
    """<p>Playback-key-pair name. The value does not need to be unique.</p>"""
    tags: NotRequired["capo_ivs.types.tags.Tags"]
    """<p>Any tags provided with the request are added to the playback key pair tags. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportPlaybackKeyPairRequest) -> dict:
    out: dict = {}
    out["publicKeyMaterial"] = value["public_key_material"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ImportPlaybackKeyPairRequest:
    out: ImportPlaybackKeyPairRequest = {}  # type: ignore[typeddict-item]
    if data.get("publicKeyMaterial") is not None:
        out["public_key_material"] = data["publicKeyMaterial"]
    else:
        raise DeserializationError(
            "ImportPlaybackKeyPairRequest.public_key_material required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("tags") is not None:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.deserialize_json(data["tags"])
    return out
