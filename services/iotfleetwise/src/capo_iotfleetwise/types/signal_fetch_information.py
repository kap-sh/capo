"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalFetchInformation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.event_expression_list
    import capo_iotfleetwise.types.language_version
    import capo_iotfleetwise.types.node_path
    import capo_iotfleetwise.types.signal_fetch_config


class SignalFetchInformation(TypedDict, closed=True):
    fully_qualified_name: "capo_iotfleetwise.types.node_path.NodePath"
    """<p>The fully qualified name of the signal to be fetched.</p>"""
    signal_fetch_config: "capo_iotfleetwise.types.signal_fetch_config.SignalFetchConfig"
    """<p>The configuration of the signal fetch operation.</p>"""
    condition_language_version: NotRequired[
        "capo_iotfleetwise.types.language_version.languageVersion"
    ]
    """<p>The version of the condition language used.</p>"""
    actions: "capo_iotfleetwise.types.event_expression_list.EventExpressionList"
    """<p>The actions to be performed by the signal fetch.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalFetchInformation) -> dict:
    out: dict = {}
    out["fullyQualifiedName"] = value["fully_qualified_name"]
    import capo_iotfleetwise.types.signal_fetch_config

    out["signalFetchConfig"] = (
        capo_iotfleetwise.types.signal_fetch_config.serialize_aws_json_1_0(
            value["signal_fetch_config"]
        )
    )
    if "condition_language_version" in value:
        out["conditionLanguageVersion"] = value["condition_language_version"]
    import capo_iotfleetwise.types.event_expression_list

    out["actions"] = (
        capo_iotfleetwise.types.event_expression_list.serialize_aws_json_1_0(
            value["actions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> SignalFetchInformation:
    out: SignalFetchInformation = {}  # type: ignore[typeddict-item]
    if data.get("fullyQualifiedName") is not None:
        out["fully_qualified_name"] = data["fullyQualifiedName"]
    else:
        out["fully_qualified_name"] = ""
    if data.get("signalFetchConfig") is not None:
        import capo_iotfleetwise.types.signal_fetch_config

        out["signal_fetch_config"] = (
            capo_iotfleetwise.types.signal_fetch_config.deserialize_aws_json_1_0(
                data["signalFetchConfig"]
            )
        )
    else:
        out["signal_fetch_config"] = {"$unknown": {"name": ""}}
    if data.get("conditionLanguageVersion") is not None:
        out["condition_language_version"] = data["conditionLanguageVersion"]
    if data.get("actions") is not None:
        import capo_iotfleetwise.types.event_expression_list

        out["actions"] = (
            capo_iotfleetwise.types.event_expression_list.deserialize_aws_json_1_0(
                data["actions"]
            )
        )
    else:
        out["actions"] = []
    return out


def redact_sensitive(value: SignalFetchInformation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "signal_fetch_config" in value:
        import capo_iotfleetwise.types.signal_fetch_config

        out["signal_fetch_config"] = (
            capo_iotfleetwise.types.signal_fetch_config.redact_sensitive(
                value["signal_fetch_config"]
            )
        )
    if "actions" in value:
        import capo_iotfleetwise.types.event_expression_list

        out["actions"] = capo_iotfleetwise.types.event_expression_list.redact_sensitive(
            value["actions"]
        )
    return out
