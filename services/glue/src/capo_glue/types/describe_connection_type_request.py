"""Generated from Smithy shape ``com.amazonaws.glue#DescribeConnectionTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string


class DescribeConnectionTypeRequest(TypedDict, closed=True):
    connection_type: "capo_glue.types.name_string.NameString"
    """<p>The name of the connection type to be described.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionTypeRequest) -> dict:
    out: dict = {}
    out["ConnectionType"] = value["connection_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionTypeRequest:
    out: DescribeConnectionTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionType") is not None:
        out["connection_type"] = data["ConnectionType"]
    else:
        out["connection_type"] = ""
    return out
