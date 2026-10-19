"""Generated from Smithy shape ``com.amazonaws.dax#SSESpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dax.types.sse_enabled


class SSESpecification(TypedDict, closed=True):
    enabled: "capo_dax.types.sse_enabled.SSEEnabled"
    """<p>Indicates whether server-side encryption is enabled (true) or disabled (false) on the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SSESpecification) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SSESpecification:
    out: SSESpecification = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
