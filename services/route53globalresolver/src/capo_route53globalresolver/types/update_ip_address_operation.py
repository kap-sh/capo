"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateIpAddressOperation``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of change to apply to a DNS IP address of a core network endpoint during an update. Valid values are the following:</p> <ul> <li> <p> <code>ADD</code> - Adds a new DNS IP address to the core network endpoint.</p> </li> <li> <p> <code>REMOVE</code> - Removes an existing DNS IP address from the core network endpoint.</p> </li> <li> <p> <code>UPDATE</code> - Updates the configuration of an existing DNS IP address on the core network endpoint.</p> </li> </ul>"""
UpdateIpAddressOperation: TypeAlias = Literal[
    "ADD",
    "REMOVE",
    "UPDATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIpAddressOperation) -> str:
    return value


def deserialize_json(data: str) -> UpdateIpAddressOperation:
    return cast(UpdateIpAddressOperation, data)
