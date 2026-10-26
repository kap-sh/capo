"""Generated from Smithy shape ``com.amazonaws.wisdom#ExternalSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.configuration
    import capo_wisdom.types.external_source


class ExternalSourceConfiguration(TypedDict, closed=True):
    source: "capo_wisdom.types.external_source.ExternalSource"
    """<p>The type of the external data source.</p>"""
    configuration: "capo_wisdom.types.configuration.Configuration"
    """<p>The configuration information of the external data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSourceConfiguration) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    import capo_wisdom.types.configuration

    out["configuration"] = capo_wisdom.types.configuration.serialize_json(
        value["configuration"]
    )
    return out


def deserialize_json(data: dict) -> ExternalSourceConfiguration:
    out: ExternalSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("configuration") is not None:
        import capo_wisdom.types.configuration

        out["configuration"] = capo_wisdom.types.configuration.deserialize_json(
            data["configuration"]
        )
    else:
        out["configuration"] = {"$unknown": {"name": ""}}
    return out
