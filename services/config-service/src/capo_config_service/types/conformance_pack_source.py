"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_source_identifier


class ConformancePackSource(TypedDict, closed=True):
    source_identifier: "capo_config_service.types.conformance_pack_source_identifier.ConformancePackSourceIdentifier"
    """<p>A predefined identifier for a managed conformance pack. The identifier specifies which managed conformance pack Config deploys in your account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackSource) -> dict:
    out: dict = {}
    out["SourceIdentifier"] = value["source_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackSource:
    out: ConformancePackSource = {}  # type: ignore[typeddict-item]
    if data.get("SourceIdentifier") is not None:
        out["source_identifier"] = data["SourceIdentifier"]
    else:
        out["source_identifier"] = ""
    return out
