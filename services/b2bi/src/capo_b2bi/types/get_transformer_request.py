"""Generated from Smithy shape ``com.amazonaws.b2bi#GetTransformerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.transformer_id


class GetTransformerRequest(TypedDict, closed=True):
    transformer_id: "capo_b2bi.types.transformer_id.TransformerId"
    """<p>Specifies the system-assigned unique identifier for the transformer.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTransformerRequest) -> dict:
    out: dict = {}
    out["transformerId"] = value["transformer_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTransformerRequest:
    out: GetTransformerRequest = {}  # type: ignore[typeddict-item]
    if data.get("transformerId") is not None:
        out["transformer_id"] = data["transformerId"]
    else:
        out["transformer_id"] = ""
    return out
