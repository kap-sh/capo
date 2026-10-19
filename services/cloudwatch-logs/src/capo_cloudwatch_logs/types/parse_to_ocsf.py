"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ParseToOCSF``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.event_source
    import capo_cloudwatch_logs.types.mapping_version
    import capo_cloudwatch_logs.types.ocsf_version
    import capo_cloudwatch_logs.types.source


class ParseToOCSF(TypedDict, closed=True):
    source: NotRequired["capo_cloudwatch_logs.types.source.Source"]
    """<p>The path to the field in the log event that you want to parse. If you omit this value, the whole log message is parsed.</p>"""
    event_source: "capo_cloudwatch_logs.types.event_source.EventSource"
    """<p>Specify the service or process that produces the log events that will be converted with this processor.</p>"""
    ocsf_version: "capo_cloudwatch_logs.types.ocsf_version.OCSFVersion"
    """<p>Specify which version of the OCSF schema to use for the transformed log events.</p>"""
    mapping_version: NotRequired[
        "capo_cloudwatch_logs.types.mapping_version.MappingVersion"
    ]
    """<p>The version of the OCSF mapping to use for parsing log data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParseToOCSF) -> dict:
    out: dict = {}
    if "source" in value:
        out["source"] = value["source"]
    import capo_cloudwatch_logs.types.event_source

    out["eventSource"] = capo_cloudwatch_logs.types.event_source.serialize_aws_json_1_1(
        value["event_source"]
    )
    import capo_cloudwatch_logs.types.ocsf_version

    out["ocsfVersion"] = capo_cloudwatch_logs.types.ocsf_version.serialize_aws_json_1_1(
        value["ocsf_version"]
    )
    if "mapping_version" in value:
        out["mappingVersion"] = value["mapping_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParseToOCSF:
    out: ParseToOCSF = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    if data.get("eventSource") is not None:
        import capo_cloudwatch_logs.types.event_source

        out["event_source"] = (
            capo_cloudwatch_logs.types.event_source.deserialize_aws_json_1_1(
                data["eventSource"]
            )
        )
    else:
        import typing

        out["event_source"] = typing.cast(
            "capo_cloudwatch_logs.types.event_source.EventSource", ""
        )
    if data.get("ocsfVersion") is not None:
        import capo_cloudwatch_logs.types.ocsf_version

        out["ocsf_version"] = (
            capo_cloudwatch_logs.types.ocsf_version.deserialize_aws_json_1_1(
                data["ocsfVersion"]
            )
        )
    else:
        import typing

        out["ocsf_version"] = typing.cast(
            "capo_cloudwatch_logs.types.ocsf_version.OCSFVersion", ""
        )
    if data.get("mappingVersion") is not None:
        out["mapping_version"] = data["mappingVersion"]
    return out
