"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#GetRequestAuthorizationDetailsInput``."""

from typing_extensions import NotRequired, TypedDict


class GetRequestAuthorizationDetailsInput(TypedDict, closed=True):
    authorization_id: "str"
    """<p>The authorization ID received in the access denied error message. This ID identifies the specific request to retrieve details for.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token from a previous call, used to retrieve the next page of evaluations. Omit this value on the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRequestAuthorizationDetailsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRequestAuthorizationDetailsInput:
    out: GetRequestAuthorizationDetailsInput = {}  # type: ignore[typeddict-item]
    return out
