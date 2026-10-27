"""Generated from Smithy shape ``com.amazonaws.elementalinference#UpdateClippingDataSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elementalinference.types.data_source_configuration
    import capo_elementalinference.types.resource_name


class UpdateClippingDataSourceConfiguration(TypedDict, closed=True):
    output_name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the output that you want to attach the game to.</p>"""
    data_source_configuration: "capo_elementalinference.types.data_source_configuration.DataSourceConfiguration"
    """<p>The game that you want to attach to the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClippingDataSourceConfiguration) -> dict:
    out: dict = {}
    out["outputName"] = value["output_name"]
    import capo_elementalinference.types.data_source_configuration

    out["dataSourceConfiguration"] = (
        capo_elementalinference.types.data_source_configuration.serialize_json(
            value["data_source_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateClippingDataSourceConfiguration:
    out: UpdateClippingDataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("outputName") is not None:
        out["output_name"] = data["outputName"]
    else:
        out["output_name"] = ""
    if data.get("dataSourceConfiguration") is not None:
        import capo_elementalinference.types.data_source_configuration

        out["data_source_configuration"] = (
            capo_elementalinference.types.data_source_configuration.deserialize_json(
                data["dataSourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateClippingDataSourceConfiguration.data_source_configuration required"
        )
    return out
