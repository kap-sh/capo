"""Generated from Smithy shape ``com.amazonaws.sesv2#ConfigurationSetFilterKey``."""

from typing import Literal, TypeAlias, cast

"""<p>The filter key to use when listing configuration sets. This can be one of the following:</p> <ul> <li> <p> <code>CONFIGURATION_SET_NAME_CONTAINS</code> – Filter by a substring of the configuration set name.</p> </li> </ul>"""
ConfigurationSetFilterKey: TypeAlias = Literal["CONFIGURATION_SET_NAME_CONTAINS",]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationSetFilterKey) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationSetFilterKey:
    return cast(ConfigurationSetFilterKey, data)
