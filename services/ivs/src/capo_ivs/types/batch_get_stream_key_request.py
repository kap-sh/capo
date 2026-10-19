"""Generated from Smithy shape ``com.amazonaws.ivs#BatchGetStreamKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.stream_key_arn_list


class BatchGetStreamKeyRequest(TypedDict, closed=True):
    arns: "capo_ivs.types.stream_key_arn_list.StreamKeyArnList"
    """<p>Array of ARNs, one per stream key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStreamKeyRequest) -> dict:
    out: dict = {}
    import capo_ivs.types.stream_key_arn_list

    out["arns"] = capo_ivs.types.stream_key_arn_list.serialize_json(value["arns"])
    return out


def deserialize_json(data: dict) -> BatchGetStreamKeyRequest:
    out: BatchGetStreamKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("arns") is not None:
        import capo_ivs.types.stream_key_arn_list

        out["arns"] = capo_ivs.types.stream_key_arn_list.deserialize_json(data["arns"])
    else:
        out["arns"] = []
    return out
