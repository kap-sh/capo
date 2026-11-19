"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ConnectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.connector_name
    import capo_observabilityadmin.types.connector_provider
    import capo_observabilityadmin.types.resource_arn


class ConnectorSummary(TypedDict, closed=True):
    arn: "capo_observabilityadmin.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    provider: "capo_observabilityadmin.types.connector_provider.ConnectorProvider"
    """<p>The cloud provider that the connector connects to.</p>"""
    name: NotRequired["capo_observabilityadmin.types.connector_name.ConnectorName"]
    """<p>The name of the connector.</p>"""
    created_time_stamp: NotRequired["int"]
    """<p>The time when the connector was created, in milliseconds since the Unix epoch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_observabilityadmin.types.connector_provider

    out["Provider"] = capo_observabilityadmin.types.connector_provider.serialize_json(
        value["provider"]
    )
    if "name" in value:
        out["Name"] = value["name"]
    if "created_time_stamp" in value:
        out["CreatedTimeStamp"] = value["created_time_stamp"]
    return out


def deserialize_json(data: dict) -> ConnectorSummary:
    out: ConnectorSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Provider") is not None:
        import capo_observabilityadmin.types.connector_provider

        out["provider"] = (
            capo_observabilityadmin.types.connector_provider.deserialize_json(
                data["Provider"]
            )
        )
    else:
        import typing

        out["provider"] = typing.cast(
            "capo_observabilityadmin.types.connector_provider.ConnectorProvider", ""
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CreatedTimeStamp") is not None:
        out["created_time_stamp"] = data["CreatedTimeStamp"]
    return out
