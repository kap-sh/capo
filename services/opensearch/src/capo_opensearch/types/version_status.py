"""Generated from Smithy shape ``com.amazonaws.opensearch#VersionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.option_status
    import capo_opensearch.types.version_string


class VersionStatus(TypedDict, closed=True):
    options: "capo_opensearch.types.version_string.VersionString"
    """<p>The OpenSearch or Elasticsearch version for the specified domain.</p>"""
    status: "capo_opensearch.types.option_status.OptionStatus"
    """<p>The status of the version options for the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionStatus) -> dict:
    out: dict = {}
    out["Options"] = value["options"]
    import capo_opensearch.types.option_status

    out["Status"] = capo_opensearch.types.option_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> VersionStatus:
    out: VersionStatus = {}  # type: ignore[typeddict-item]
    if data.get("Options") is not None:
        out["options"] = data["Options"]
    else:
        out["options"] = ""
    if data.get("Status") is not None:
        import capo_opensearch.types.option_status

        out["status"] = capo_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("VersionStatus.status required")
    return out
