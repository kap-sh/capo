"""Generated from Smithy shape ``com.amazonaws.quicksight#IAMConnectionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.role_arn


class IAMConnectionMetadata(TypedDict, closed=True):
    role_arn: "capo_quicksight.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to assume for authentication with Amazon Web Services services. This IAM role should be in the same account as Quick Sight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IAMConnectionMetadata) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> IAMConnectionMetadata:
    out: IAMConnectionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    return out
