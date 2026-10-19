"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicSearchFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_string
    import capo_quicksight.types.topic_filter_attribute
    import capo_quicksight.types.topic_filter_operator


class TopicSearchFilter(TypedDict, closed=True):
    operator: "capo_quicksight.types.topic_filter_operator.TopicFilterOperator"
    """<p>The operator like equals or like.</p>"""
    name: "capo_quicksight.types.topic_filter_attribute.TopicFilterAttribute"
    """<p>The name of the topic search filter.</p>"""
    value: "capo_quicksight.types.sensitive_string.SensitiveString"
    """<p>The value of the topic search filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicSearchFilter) -> dict:
    out: dict = {}
    import capo_quicksight.types.topic_filter_operator

    out["Operator"] = capo_quicksight.types.topic_filter_operator.serialize_json(
        value["operator"]
    )
    import capo_quicksight.types.topic_filter_attribute

    out["Name"] = capo_quicksight.types.topic_filter_attribute.serialize_json(
        value["name"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TopicSearchFilter:
    out: TopicSearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("Operator") is not None:
        import capo_quicksight.types.topic_filter_operator

        out["operator"] = capo_quicksight.types.topic_filter_operator.deserialize_json(
            data["Operator"]
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_quicksight.types.topic_filter_operator.TopicFilterOperator", ""
        )
    if data.get("Name") is not None:
        import capo_quicksight.types.topic_filter_attribute

        out["name"] = capo_quicksight.types.topic_filter_attribute.deserialize_json(
            data["Name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_quicksight.types.topic_filter_attribute.TopicFilterAttribute", ""
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out


def redact_sensitive(value: TopicSearchFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
