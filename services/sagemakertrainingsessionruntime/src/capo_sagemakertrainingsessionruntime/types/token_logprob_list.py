"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#TokenLogprobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.token_logprob

TokenLogprobList: TypeAlias = list[
    "capo_sagemakertrainingsessionruntime.types.token_logprob.TokenLogprob"
]


# --- restJson1 ser/de ---
def serialize_json(value: TokenLogprobList) -> list:
    import capo_sagemakertrainingsessionruntime.types.token_logprob

    out: list = []
    for item in value:
        out.append(
            capo_sagemakertrainingsessionruntime.types.token_logprob.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TokenLogprobList:
    import capo_sagemakertrainingsessionruntime.types.token_logprob

    out: TokenLogprobList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemakertrainingsessionruntime.types.token_logprob.deserialize_json(
                item
            )
        )
    return out
