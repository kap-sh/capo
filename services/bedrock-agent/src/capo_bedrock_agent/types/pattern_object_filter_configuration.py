"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PatternObjectFilterConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.pattern_object_filter_list


class PatternObjectFilterConfiguration(TypedDict, closed=True):
    filters: (
        "capo_bedrock_agent.types.pattern_object_filter_list.PatternObjectFilterList"
    )
    """<p>The configuration of specific filters applied to your data source content. You can filter out or include certain content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PatternObjectFilterConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.pattern_object_filter_list

    out["filters"] = capo_bedrock_agent.types.pattern_object_filter_list.serialize_json(
        value["filters"]
    )
    return out


def deserialize_json(data: dict) -> PatternObjectFilterConfiguration:
    out: PatternObjectFilterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_bedrock_agent.types.pattern_object_filter_list

        out["filters"] = (
            capo_bedrock_agent.types.pattern_object_filter_list.deserialize_json(
                data["filters"]
            )
        )
    else:
        raise DeserializationError("PatternObjectFilterConfiguration.filters required")
    return out


def redact_sensitive(value: PatternObjectFilterConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters" in value:
        out["filters"] = "*** Sensitive Data Redacted ***"
    return out
