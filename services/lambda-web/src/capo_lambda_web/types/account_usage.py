"""Generated from Smithy shape ``com.amazonaws.lambdaweb#AccountUsage``."""

from typing_extensions import TypedDict


class AccountUsage(TypedDict, closed=True):
    function_count: "int"
    """<p>The number of web functions in your account in the current AWS Region. This count includes web functions in all states, not only functions in the <code>Active</code> state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountUsage) -> dict:
    out: dict = {}
    out["functionCount"] = value["function_count"]
    return out


def deserialize_json(data: dict) -> AccountUsage:
    out: AccountUsage = {}  # type: ignore[typeddict-item]
    if data.get("functionCount") is not None:
        out["function_count"] = data["functionCount"]
    else:
        out["function_count"] = 0
    return out
