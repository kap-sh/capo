"""Generated from Smithy shape ``com.amazonaws.wafv2#SingleHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.field_to_match_data


class SingleHeader(TypedDict, closed=True):
    name: "capo_wafv2.types.field_to_match_data.FieldToMatchData"
    """<p>The name of the query header to inspect.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SingleHeader) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SingleHeader:
    out: SingleHeader = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
