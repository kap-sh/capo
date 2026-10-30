"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OnBehalfOfClientAuthenticationMethod``."""

from typing import Literal, TypeAlias, cast

OnBehalfOfClientAuthenticationMethod: TypeAlias = Literal["NO_CLIENT",]


# --- restJson1 ser/de ---
def serialize_json(value: OnBehalfOfClientAuthenticationMethod) -> str:
    return value


def deserialize_json(data: str) -> OnBehalfOfClientAuthenticationMethod:
    return cast(OnBehalfOfClientAuthenticationMethod, data)
