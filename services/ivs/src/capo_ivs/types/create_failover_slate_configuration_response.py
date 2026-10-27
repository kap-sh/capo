"""Generated from Smithy shape ``com.amazonaws.ivs#CreateFailoverSlateConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.failover_slate_configuration


class CreateFailoverSlateConfigurationResponse(TypedDict, closed=True):
    failover_slate_configuration: (
        "capo_ivs.types.failover_slate_configuration.FailoverSlateConfiguration"
    )
    """<p>The failover slate configuration that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFailoverSlateConfigurationResponse) -> dict:
    out: dict = {}
    import capo_ivs.types.failover_slate_configuration

    out["failoverSlateConfiguration"] = (
        capo_ivs.types.failover_slate_configuration.serialize_json(
            value["failover_slate_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateFailoverSlateConfigurationResponse:
    out: CreateFailoverSlateConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("failoverSlateConfiguration") is not None:
        import capo_ivs.types.failover_slate_configuration

        out["failover_slate_configuration"] = (
            capo_ivs.types.failover_slate_configuration.deserialize_json(
                data["failoverSlateConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateFailoverSlateConfigurationResponse.failover_slate_configuration required"
        )
    return out
