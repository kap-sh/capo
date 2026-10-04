"""Generated from Smithy shape ``com.amazonaws.lambdaweb#AccountUsage``."""

from typing_extensions import TypedDict

from capo_lambda_web.errors import DeserializationError


class AccountUsage(TypedDict, closed=True):
    function_count: "int"
    """<p>The number of web functions in your account in the current AWS Region.</p>"""


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
        raise DeserializationError("AccountUsage.function_count required")
    return out
