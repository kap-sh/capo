"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetGlueFunctionSessionContextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.expiration_timestamp
    import capo_lakeformation.types.session_context_id_string


class GetGlueFunctionSessionContextResponse(TypedDict, closed=True):
    session_context_id: NotRequired[
        "capo_lakeformation.types.session_context_id_string.SessionContextIdString"
    ]
    """<p>The ID of the session context.</p>"""
    expiration: NotRequired[
        "capo_lakeformation.types.expiration_timestamp.ExpirationTimestamp"
    ]
    """<p>The date and time when the session context expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGlueFunctionSessionContextResponse) -> dict:
    out: dict = {}
    if "session_context_id" in value:
        out["SessionContextId"] = value["session_context_id"]
    if "expiration" in value:
        import capo_lakeformation.types.expiration_timestamp

        out["Expiration"] = (
            capo_lakeformation.types.expiration_timestamp.serialize_json(
                value["expiration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetGlueFunctionSessionContextResponse:
    out: GetGlueFunctionSessionContextResponse = {}  # type: ignore[typeddict-item]
    if data.get("SessionContextId") is not None:
        out["session_context_id"] = data["SessionContextId"]
    if data.get("Expiration") is not None:
        import capo_lakeformation.types.expiration_timestamp

        out["expiration"] = (
            capo_lakeformation.types.expiration_timestamp.deserialize_json(
                data["Expiration"]
            )
        )
    return out
