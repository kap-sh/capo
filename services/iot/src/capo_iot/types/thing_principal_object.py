"""Generated from Smithy shape ``com.amazonaws.iot#ThingPrincipalObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.principal
    import capo_iot.types.thing_principal_type


class ThingPrincipalObject(TypedDict, closed=True):
    principal: "capo_iot.types.principal.Principal"
    """<p>The principal of the thing principal object.</p>"""
    thing_principal_type: NotRequired[
        "capo_iot.types.thing_principal_type.ThingPrincipalType"
    ]
    """<p>The type of the relation you want to specify when you attach a principal to a thing. The value defaults to <code>NON_EXCLUSIVE_THING</code>.</p> <ul> <li> <p> <code>EXCLUSIVE_THING</code> - Attaches the specified principal to the specified thing, exclusively. The thing will be the only thing that’s attached to the principal.</p> </li> </ul> <ul> <li> <p> <code>NON_EXCLUSIVE_THING</code> - Attaches the specified principal to the specified thing. Multiple things can be attached to the principal.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThingPrincipalObject) -> dict:
    out: dict = {}
    out["principal"] = value["principal"]
    if "thing_principal_type" in value:
        import capo_iot.types.thing_principal_type

        out["thingPrincipalType"] = capo_iot.types.thing_principal_type.serialize_json(
            value["thing_principal_type"]
        )
    return out


def deserialize_json(data: dict) -> ThingPrincipalObject:
    out: ThingPrincipalObject = {}  # type: ignore[typeddict-item]
    if data.get("principal") is not None:
        out["principal"] = data["principal"]
    else:
        out["principal"] = ""
    if data.get("thingPrincipalType") is not None:
        import capo_iot.types.thing_principal_type

        out["thing_principal_type"] = (
            capo_iot.types.thing_principal_type.deserialize_json(
                data["thingPrincipalType"]
            )
        )
    return out
