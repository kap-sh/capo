"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#UserContext``."""

from typing_extensions import TypedDict


class UserContext(TypedDict, closed=True):
    user_id: "str"
    """<p>The identifier of the user making the retrieval request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserContext) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> UserContext:
    out: UserContext = {}  # type: ignore[typeddict-item]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    return out
