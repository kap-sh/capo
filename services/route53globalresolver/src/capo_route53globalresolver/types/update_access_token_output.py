"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateAccessTokenOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name_short


class UpdateAccessTokenOutput(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the token.</p>"""
    name: "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
    """<p>The name of the token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessTokenOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateAccessTokenOutput:
    out: UpdateAccessTokenOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
