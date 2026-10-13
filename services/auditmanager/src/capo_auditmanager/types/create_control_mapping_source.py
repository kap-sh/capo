"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateControlMappingSource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.source_description
    import capo_auditmanager.types.source_frequency
    import capo_auditmanager.types.source_keyword
    import capo_auditmanager.types.source_name
    import capo_auditmanager.types.source_set_up_option
    import capo_auditmanager.types.source_type
    import capo_auditmanager.types.troubleshooting_text


class CreateControlMappingSource(TypedDict, closed=True):
    source_name: NotRequired["capo_auditmanager.types.source_name.SourceName"]
    """<p> The name of the control mapping data source. </p>"""
    source_description: NotRequired[
        "capo_auditmanager.types.source_description.SourceDescription"
    ]
    """<p> The description of the data source that determines where Audit Manager collects evidence from for the control. </p>"""
    source_set_up_option: NotRequired[
        "capo_auditmanager.types.source_set_up_option.SourceSetUpOption"
    ]
    """<p>The setup option for the data source. This option reflects if the evidence collection method is automated or manual. If you don’t provide a value for <code>sourceSetUpOption</code>, Audit Manager automatically infers and populates the correct value based on the <code>sourceType</code> that you specify.</p>"""
    source_type: NotRequired["capo_auditmanager.types.source_type.SourceType"]
    """<p> Specifies which type of data source is used to collect evidence. </p> <ul> <li> <p>The source can be an individual data source type, such as <code>AWS_Cloudtrail</code>, <code>AWS_Config</code>, <code>AWS_Security_Hub</code>, <code>AWS_API_Call</code>, or <code>MANUAL</code>. </p> </li> <li> <p>The source can also be a managed grouping of data sources, such as a <code>Core_Control</code> or a <code>Common_Control</code>.</p> </li> </ul>"""
    source_keyword: NotRequired["capo_auditmanager.types.source_keyword.SourceKeyword"]
    source_frequency: NotRequired[
        "capo_auditmanager.types.source_frequency.SourceFrequency"
    ]
    """<p>Specifies how often evidence is collected from the control mapping source. </p>"""
    troubleshooting_text: NotRequired[
        "capo_auditmanager.types.troubleshooting_text.TroubleshootingText"
    ]
    """<p> The instructions for troubleshooting the control. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateControlMappingSource) -> dict:
    out: dict = {}
    if "source_name" in value:
        out["sourceName"] = value["source_name"]
    if "source_description" in value:
        out["sourceDescription"] = value["source_description"]
    if "source_set_up_option" in value:
        import capo_auditmanager.types.source_set_up_option

        out["sourceSetUpOption"] = (
            capo_auditmanager.types.source_set_up_option.serialize_json(
                value["source_set_up_option"]
            )
        )
    if "source_type" in value:
        import capo_auditmanager.types.source_type

        out["sourceType"] = capo_auditmanager.types.source_type.serialize_json(
            value["source_type"]
        )
    if "source_keyword" in value:
        import capo_auditmanager.types.source_keyword

        out["sourceKeyword"] = capo_auditmanager.types.source_keyword.serialize_json(
            value["source_keyword"]
        )
    if "source_frequency" in value:
        import capo_auditmanager.types.source_frequency

        out["sourceFrequency"] = (
            capo_auditmanager.types.source_frequency.serialize_json(
                value["source_frequency"]
            )
        )
    if "troubleshooting_text" in value:
        out["troubleshootingText"] = value["troubleshooting_text"]
    return out


def deserialize_json(data: dict) -> CreateControlMappingSource:
    out: CreateControlMappingSource = {}  # type: ignore[typeddict-item]
    if data.get("sourceName") is not None:
        out["source_name"] = data["sourceName"]
    if data.get("sourceDescription") is not None:
        out["source_description"] = data["sourceDescription"]
    if data.get("sourceSetUpOption") is not None:
        import capo_auditmanager.types.source_set_up_option

        out["source_set_up_option"] = (
            capo_auditmanager.types.source_set_up_option.deserialize_json(
                data["sourceSetUpOption"]
            )
        )
    if data.get("sourceType") is not None:
        import capo_auditmanager.types.source_type

        out["source_type"] = capo_auditmanager.types.source_type.deserialize_json(
            data["sourceType"]
        )
    if data.get("sourceKeyword") is not None:
        import capo_auditmanager.types.source_keyword

        out["source_keyword"] = capo_auditmanager.types.source_keyword.deserialize_json(
            data["sourceKeyword"]
        )
    if data.get("sourceFrequency") is not None:
        import capo_auditmanager.types.source_frequency

        out["source_frequency"] = (
            capo_auditmanager.types.source_frequency.deserialize_json(
                data["sourceFrequency"]
            )
        )
    if data.get("troubleshootingText") is not None:
        out["troubleshooting_text"] = data["troubleshootingText"]
    return out


def redact_sensitive(value: CreateControlMappingSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "troubleshooting_text" in value:
        out["troubleshooting_text"] = "*** Sensitive Data Redacted ***"
    return out
