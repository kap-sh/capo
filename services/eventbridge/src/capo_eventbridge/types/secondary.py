"""Generated from Smithy shape ``com.amazonaws.eventbridge#Secondary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.route


class Secondary(TypedDict, closed=True):
    route: "capo_eventbridge.types.route.Route"
    """<p>Defines the secondary Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Secondary) -> dict:
    out: dict = {}
    out["Route"] = value["route"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Secondary:
    out: Secondary = {}  # type: ignore[typeddict-item]
    if data.get("Route") is not None:
        out["route"] = data["Route"]
    else:
        out["route"] = ""
    return out
