"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RecordExpiryAction``."""

from typing import Literal, TypeAlias, cast

"""<p>The action to apply to a strategy's record expiry (long-term memory time-to-live) configuration. <code>REMOVE</code> removes a previously configured time-to-live; newer records no longer have a time-to-live set and do not expire.</p>"""
RecordExpiryAction: TypeAlias = Literal["REMOVE",]


# --- restJson1 ser/de ---
def serialize_json(value: RecordExpiryAction) -> str:
    return value


def deserialize_json(data: str) -> RecordExpiryAction:
    return cast(RecordExpiryAction, data)
