"""Generated from Smithy shape ``com.amazonaws.amp#GetDefaultScraperConfigurationResponse``."""

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError


class GetDefaultScraperConfigurationResponse(TypedDict, closed=True):
    configuration: "bytes"
    """<p>The configuration file. Base 64 encoded. For more information, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration">Scraper configuration</a>in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDefaultScraperConfigurationResponse) -> dict:
    out: dict = {}
    import capo_amp.types._prelude.blob

    out["configuration"] = capo_amp.types._prelude.blob.serialize_json(
        value["configuration"]
    )
    return out


def deserialize_json(data: dict) -> GetDefaultScraperConfigurationResponse:
    out: GetDefaultScraperConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        import capo_amp.types._prelude.blob

        out["configuration"] = capo_amp.types._prelude.blob.deserialize_json(
            data["configuration"]
        )
    else:
        raise DeserializationError(
            "GetDefaultScraperConfigurationResponse.configuration required"
        )
    return out
