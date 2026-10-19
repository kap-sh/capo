"""Generated from Smithy shape ``com.amazonaws.qbusiness#AuthChallengeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.authorization_response_map


class AuthChallengeResponse(TypedDict, closed=True):
    response_map: (
        "capo_qbusiness.types.authorization_response_map.AuthorizationResponseMap"
    )
    """<p>The mapping of key-value pairs in an authentication challenge response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthChallengeResponse) -> dict:
    out: dict = {}
    import capo_qbusiness.types.authorization_response_map

    out["responseMap"] = capo_qbusiness.types.authorization_response_map.serialize_json(
        value["response_map"]
    )
    return out


def deserialize_json(data: dict) -> AuthChallengeResponse:
    out: AuthChallengeResponse = {}  # type: ignore[typeddict-item]
    if data.get("responseMap") is not None:
        import capo_qbusiness.types.authorization_response_map

        out["response_map"] = (
            capo_qbusiness.types.authorization_response_map.deserialize_json(
                data["responseMap"]
            )
        )
    else:
        out["response_map"] = {}
    return out
