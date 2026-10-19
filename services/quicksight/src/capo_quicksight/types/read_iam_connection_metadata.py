"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadIamConnectionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.resource_arn
    import capo_quicksight.types.role_arn


class ReadIamConnectionMetadata(TypedDict, closed=True):
    role_arn: "capo_quicksight.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to assume for authentication.</p>"""
    source_arn: "capo_quicksight.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the source resource for IAM authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadIamConnectionMetadata) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    out["SourceArn"] = value["source_arn"]
    return out


def deserialize_json(data: dict) -> ReadIamConnectionMetadata:
    out: ReadIamConnectionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    else:
        out["source_arn"] = ""
    return out
