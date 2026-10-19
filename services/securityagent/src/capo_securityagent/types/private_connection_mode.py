"""Generated from Smithy shape ``com.amazonaws.securityagent#PrivateConnectionMode``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError
from capo_securityagent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityagent.types.self_managed_input
    import capo_securityagent.types.service_managed_input


class _PrivateConnectionMode_serviceManaged(TypedDict, closed=True):
    serviceManaged: "capo_securityagent.types.service_managed_input.ServiceManagedInput"


class _PrivateConnectionMode_selfManaged(TypedDict, closed=True):
    selfManaged: "capo_securityagent.types.self_managed_input.SelfManagedInput"


PrivateConnectionMode: TypeAlias = (
    _PrivateConnectionMode_serviceManaged
    | _PrivateConnectionMode_selfManaged
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionMode) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PrivateConnectionMode: cannot serialize unknown variant {value.name!r}"
        )
    elif "serviceManaged" in value:
        import capo_securityagent.types.service_managed_input

        return {
            "serviceManaged": capo_securityagent.types.service_managed_input.serialize_json(
                value["serviceManaged"]
            )
        }
    elif "selfManaged" in value:
        import capo_securityagent.types.self_managed_input

        return {
            "selfManaged": capo_securityagent.types.self_managed_input.serialize_json(
                value["selfManaged"]
            )
        }
    else:
        raise SerializationError("PrivateConnectionMode: no variant present")


def deserialize_json(data: dict) -> PrivateConnectionMode:
    if data.get("serviceManaged") is not None:
        import capo_securityagent.types.service_managed_input

        return {
            "serviceManaged": capo_securityagent.types.service_managed_input.deserialize_json(
                data["serviceManaged"]
            )
        }
    elif data.get("selfManaged") is not None:
        import capo_securityagent.types.self_managed_input

        return {
            "selfManaged": capo_securityagent.types.self_managed_input.deserialize_json(
                data["selfManaged"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("PrivateConnectionMode: no recognized variant key")


def redact_sensitive(
    value: PrivateConnectionMode,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "serviceManaged" in value:
        import capo_securityagent.types.service_managed_input

        out["serviceManaged"] = (
            capo_securityagent.types.service_managed_input.redact_sensitive(
                value["serviceManaged"]
            )
        )
    if "selfManaged" in value:
        import capo_securityagent.types.self_managed_input

        out["selfManaged"] = (
            capo_securityagent.types.self_managed_input.redact_sensitive(
                value["selfManaged"]
            )
        )
    return out
