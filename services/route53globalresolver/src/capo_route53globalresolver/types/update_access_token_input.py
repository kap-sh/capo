"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateAccessTokenInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name_short


class UpdateAccessTokenInput(TypedDict, closed=True):
    access_token_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the token.</p>"""
    name: "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
    """<p>The new name of the token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessTokenInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateAccessTokenInput:
    out: UpdateAccessTokenInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
