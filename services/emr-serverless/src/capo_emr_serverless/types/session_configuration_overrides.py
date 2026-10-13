"""Generated from Smithy shape ``com.amazonaws.emrserverless#SessionConfigurationOverrides``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.configuration_list


class SessionConfigurationOverrides(TypedDict, closed=True):
    runtime_configuration: NotRequired[
        "capo_emr_serverless.types.configuration_list.ConfigurationList"
    ]
    """<p>The runtime configuration for the session. Contains Spark configuration properties specified at session creation time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionConfigurationOverrides) -> dict:
    out: dict = {}
    if "runtime_configuration" in value:
        import capo_emr_serverless.types.configuration_list

        out["runtimeConfiguration"] = (
            capo_emr_serverless.types.configuration_list.serialize_json(
                value["runtime_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SessionConfigurationOverrides:
    out: SessionConfigurationOverrides = {}  # type: ignore[typeddict-item]
    if data.get("runtimeConfiguration") is not None:
        import capo_emr_serverless.types.configuration_list

        out["runtime_configuration"] = (
            capo_emr_serverless.types.configuration_list.deserialize_json(
                data["runtimeConfiguration"]
            )
        )
    return out


def redact_sensitive(value: SessionConfigurationOverrides) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "runtime_configuration" in value:
        import capo_emr_serverless.types.configuration_list

        out["runtime_configuration"] = (
            capo_emr_serverless.types.configuration_list.redact_sensitive(
                value["runtime_configuration"]
            )
        )
    return out
