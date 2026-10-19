"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetManagedViewInput``."""

from typing_extensions import TypedDict


class GetManagedViewInput(TypedDict, closed=True):
    managed_view_arn: "str"
    """<p>The Amazon resource name (ARN) of the managed view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedViewInput) -> dict:
    out: dict = {}
    out["ManagedViewArn"] = value["managed_view_arn"]
    return out


def deserialize_json(data: dict) -> GetManagedViewInput:
    out: GetManagedViewInput = {}  # type: ignore[typeddict-item]
    if data.get("ManagedViewArn") is not None:
        out["managed_view_arn"] = data["ManagedViewArn"]
    else:
        out["managed_view_arn"] = ""
    return out
