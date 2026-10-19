"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.index_id


class DescribeIndexRequest(TypedDict, closed=True):
    id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index you want to get information on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIndexRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIndexRequest:
    out: DescribeIndexRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out
