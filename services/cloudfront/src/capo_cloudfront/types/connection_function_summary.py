"""Generated from Smithy shape ``com.amazonaws.cloudfront#ConnectionFunctionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.function_config
    import capo_cloudfront.types.function_name
    import capo_cloudfront.types.function_stage
    import capo_cloudfront.types.resource_id
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class ConnectionFunctionSummary(TypedDict, closed=True):
    name: "capo_cloudfront.types.function_name.FunctionName"
    """<p>The connection function name.</p>"""
    id: "capo_cloudfront.types.resource_id.ResourceId"
    """<p>The connection function ID.</p>"""
    connection_function_config: "capo_cloudfront.types.function_config.FunctionConfig"
    connection_function_arn: "capo_cloudfront.types.string.string"
    """<p>The connection function Amazon Resource Name (ARN).</p>"""
    status: "capo_cloudfront.types.string.string"
    """<p>The connection function status.</p>"""
    stage: "capo_cloudfront.types.function_stage.FunctionStage"
    """<p>The connection function stage.</p>"""
    created_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The connection function created time.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The connection function last modified time.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ConnectionFunctionSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Id").text = str(value["id"])
    import capo_cloudfront.types.function_config

    capo_cloudfront.types.function_config.serialize_xml(
        value["connection_function_config"], el, "ConnectionFunctionConfig"
    )
    SubElement(el, "ConnectionFunctionArn").text = str(value["connection_function_arn"])
    SubElement(el, "Status").text = str(value["status"])
    import capo_cloudfront.types.function_stage

    capo_cloudfront.types.function_stage.serialize_xml(value["stage"], el, "Stage")
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["created_time"], el, "CreatedTime"
    )
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )


def deserialize_xml(el: Element) -> ConnectionFunctionSummary:
    out: ConnectionFunctionSummary = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_connection_function_config = el.find("ConnectionFunctionConfig")
    if child_connection_function_config is not None:
        import capo_cloudfront.types.function_config

        out["connection_function_config"] = (
            capo_cloudfront.types.function_config.deserialize_xml(
                child_connection_function_config
            )
        )
    else:
        raise DeserializationError(
            "ConnectionFunctionSummary.connection_function_config required"
        )
    child_connection_function_arn = el.find("ConnectionFunctionArn")
    if child_connection_function_arn is not None:
        out["connection_function_arn"] = str(child_connection_function_arn.text or "")
    else:
        out["connection_function_arn"] = ""
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        out["status"] = ""
    child_stage = el.find("Stage")
    if child_stage is not None:
        import capo_cloudfront.types.function_stage

        out["stage"] = capo_cloudfront.types.function_stage.deserialize_xml(child_stage)
    else:
        import typing

        out["stage"] = typing.cast(
            "capo_cloudfront.types.function_stage.FunctionStage", ""
        )
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import capo_cloudfront.types.timestamp

        out["created_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_created_time
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
