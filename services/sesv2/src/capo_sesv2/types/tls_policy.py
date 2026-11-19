"""Generated from Smithy shape ``com.amazonaws.sesv2#TlsPolicy``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is <code>REQUIRE</code>, messages are only delivered if a TLS connection can be established. If the value is <code>OPTIONAL</code>, messages can be delivered in plain text if a TLS connection can't be established.</p>"""
TlsPolicy: TypeAlias = Literal[
    "REQUIRE",
    "OPTIONAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: TlsPolicy) -> str:
    return value


def deserialize_json(data: str) -> TlsPolicy:
    return cast(TlsPolicy, data)
