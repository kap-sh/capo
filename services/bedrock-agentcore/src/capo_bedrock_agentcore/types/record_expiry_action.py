"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecordExpiryAction``."""

from typing import Literal, TypeAlias, cast

"""<p>The action to apply to an existing record expiry (long-term memory time-to-live) configuration. <code>REMOVE</code> removes a previously configured expiry so that the records no longer expire.</p>"""
RecordExpiryAction: TypeAlias = Literal["REMOVE",]


# --- restJson1 ser/de ---
def serialize_json(value: RecordExpiryAction) -> str:
    return value


def deserialize_json(data: str) -> RecordExpiryAction:
    return cast(RecordExpiryAction, data)
