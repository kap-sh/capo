"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DeletionProtection``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the deletion protection setting that a rule applies to the log groups that it creates. If you don't specify a value, the rule doesn't enable deletion protection. The following value is supported:</p> <ul> <li> <p> <code>ENABLED</code> – The rule enables deletion protection on log groups that it creates.</p> </li> </ul>"""
DeletionProtection: TypeAlias = Literal["ENABLED",]


# --- restJson1 ser/de ---
def serialize_json(value: DeletionProtection) -> str:
    return value


def deserialize_json(data: str) -> DeletionProtection:
    return cast(DeletionProtection, data)
