"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedPrincipals``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.subscribed_principal

SubscribedPrincipals: TypeAlias = list[
    "capo_datazone.types.subscribed_principal.SubscribedPrincipal"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedPrincipals) -> list:
    import capo_datazone.types.subscribed_principal

    out: list = []
    for item in value:
        out.append(capo_datazone.types.subscribed_principal.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscribedPrincipals:
    import capo_datazone.types.subscribed_principal

    out: SubscribedPrincipals = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.subscribed_principal.deserialize_json(item))
    return out


def redact_sensitive(value: SubscribedPrincipals) -> list[Any]:
    import capo_datazone.types.subscribed_principal

    return [
        capo_datazone.types.subscribed_principal.redact_sensitive(item)
        for item in value
    ]
