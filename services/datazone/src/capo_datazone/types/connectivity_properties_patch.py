"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectivityPropertiesPatch``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.authentication_configuration_patch
    import capo_datazone.types.connection_properties


class ConnectivityPropertiesPatch(TypedDict, closed=True):
    description: NotRequired["str"]
    """<p>A description of the connectivity properties update.</p>"""
    connection_properties: NotRequired[
        "capo_datazone.types.connection_properties.ConnectionProperties"
    ]
    """<p>The connection properties to update.</p>"""
    authentication_configuration: NotRequired[
        "capo_datazone.types.authentication_configuration_patch.AuthenticationConfigurationPatch"
    ]
    """<p>The authentication settings to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectivityPropertiesPatch) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "connection_properties" in value:
        import capo_datazone.types.connection_properties

        out["connectionProperties"] = (
            capo_datazone.types.connection_properties.serialize_json(
                value["connection_properties"]
            )
        )
    if "authentication_configuration" in value:
        import capo_datazone.types.authentication_configuration_patch

        out["authenticationConfiguration"] = (
            capo_datazone.types.authentication_configuration_patch.serialize_json(
                value["authentication_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectivityPropertiesPatch:
    out: ConnectivityPropertiesPatch = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("connectionProperties") is not None:
        import capo_datazone.types.connection_properties

        out["connection_properties"] = (
            capo_datazone.types.connection_properties.deserialize_json(
                data["connectionProperties"]
            )
        )
    if data.get("authenticationConfiguration") is not None:
        import capo_datazone.types.authentication_configuration_patch

        out["authentication_configuration"] = (
            capo_datazone.types.authentication_configuration_patch.deserialize_json(
                data["authenticationConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ConnectivityPropertiesPatch) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_configuration" in value:
        import capo_datazone.types.authentication_configuration_patch

        out["authentication_configuration"] = (
            capo_datazone.types.authentication_configuration_patch.redact_sensitive(
                value["authentication_configuration"]
            )
        )
    return out
