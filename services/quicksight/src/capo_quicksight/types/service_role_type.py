"""Generated from Smithy shape ``com.amazonaws.quicksight#ServiceRoleType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of service role that Amazon Quick Sight uses to access resources in an Amazon Web Services account. Valid values:</p> <ul> <li> <p> <code>QUICKSIGHT_MANAGED</code>: Amazon Quick Sight manages the role.</p> </li> <li> <p> <code>CUSTOMER_MANAGED</code>: You manage the role and its permissions.</p> </li> </ul>"""
ServiceRoleType: TypeAlias = Literal[
    "QUICKSIGHT_MANAGED",
    "CUSTOMER_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceRoleType) -> str:
    return value


def deserialize_json(data: str) -> ServiceRoleType:
    return cast(ServiceRoleType, data)
