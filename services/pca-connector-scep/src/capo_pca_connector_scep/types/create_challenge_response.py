"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#CreateChallengeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.challenge


class CreateChallengeResponse(TypedDict, closed=True):
    challenge: NotRequired["capo_pca_connector_scep.types.challenge.Challenge"]
    """<p>Returns the challenge details for the specified connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChallengeResponse) -> dict:
    out: dict = {}
    if "challenge" in value:
        import capo_pca_connector_scep.types.challenge

        out["Challenge"] = capo_pca_connector_scep.types.challenge.serialize_json(
            value["challenge"]
        )
    return out


def deserialize_json(data: dict) -> CreateChallengeResponse:
    out: CreateChallengeResponse = {}  # type: ignore[typeddict-item]
    if data.get("Challenge") is not None:
        import capo_pca_connector_scep.types.challenge

        out["challenge"] = capo_pca_connector_scep.types.challenge.deserialize_json(
            data["Challenge"]
        )
    return out


def redact_sensitive(value: CreateChallengeResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "challenge" in value:
        import capo_pca_connector_scep.types.challenge

        out["challenge"] = capo_pca_connector_scep.types.challenge.redact_sensitive(
            value["challenge"]
        )
    return out
