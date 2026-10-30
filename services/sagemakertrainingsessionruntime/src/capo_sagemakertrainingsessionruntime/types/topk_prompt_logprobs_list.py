"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#TopkPromptLogprobsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.token_logprob_list

TopkPromptLogprobsList: TypeAlias = list[
    "capo_sagemakertrainingsessionruntime.types.token_logprob_list.TokenLogprobList"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopkPromptLogprobsList) -> list:
    import capo_sagemakertrainingsessionruntime.types.token_logprob_list

    out: list = []
    for item in value:
        out.append(
            capo_sagemakertrainingsessionruntime.types.token_logprob_list.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TopkPromptLogprobsList:
    import capo_sagemakertrainingsessionruntime.types.token_logprob_list

    out: TopkPromptLogprobsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemakertrainingsessionruntime.types.token_logprob_list.deserialize_json(
                item
            )
        )
    return out
