"""Generated from Smithy shape ``com.amazonaws.lambda#TenancyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.tenant_isolation_mode


class TenancyConfig(TypedDict, closed=True):
    tenant_isolation_mode: "capo_lambda.types.tenant_isolation_mode.TenantIsolationMode"
    """<p>Tenant isolation mode allows for invocation to be sent to a corresponding execution environment dedicated to a specific tenant ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TenancyConfig) -> dict:
    out: dict = {}
    import capo_lambda.types.tenant_isolation_mode

    out["TenantIsolationMode"] = capo_lambda.types.tenant_isolation_mode.serialize_json(
        value["tenant_isolation_mode"]
    )
    return out


def deserialize_json(data: dict) -> TenancyConfig:
    out: TenancyConfig = {}  # type: ignore[typeddict-item]
    if data.get("TenantIsolationMode") is not None:
        import capo_lambda.types.tenant_isolation_mode

        out["tenant_isolation_mode"] = (
            capo_lambda.types.tenant_isolation_mode.deserialize_json(
                data["TenantIsolationMode"]
            )
        )
    else:
        import typing

        out["tenant_isolation_mode"] = typing.cast(
            "capo_lambda.types.tenant_isolation_mode.TenantIsolationMode", ""
        )
    return out
