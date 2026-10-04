"""Generated from Smithy shape ``com.amazonaws.sesv2#ListTenantsFilterKey``."""

from typing import Literal, TypeAlias, cast

"""<p>The filter key to use when listing tenants. This can be one of the following:</p> <ul> <li> <p> <code>TENANT_NAME_CONTAINS</code> – Filter by a substring of the tenant name.</p> </li> <li> <p> <code>SENDING_STATUS</code> – Filter by sending status.</p> </li> </ul>"""
ListTenantsFilterKey: TypeAlias = Literal[
    "TENANT_NAME_CONTAINS",
    "SENDING_STATUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTenantsFilterKey) -> str:
    return value


def deserialize_json(data: str) -> ListTenantsFilterKey:
    return cast(ListTenantsFilterKey, data)
