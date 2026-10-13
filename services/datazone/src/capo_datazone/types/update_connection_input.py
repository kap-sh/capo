"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateConnectionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.aws_location
    import capo_datazone.types.configurations
    import capo_datazone.types.connection_id
    import capo_datazone.types.connection_properties_patch
    import capo_datazone.types.description
    import capo_datazone.types.domain_id


class UpdateConnectionInput(TypedDict, closed=True):
    configurations: NotRequired["capo_datazone.types.configurations.Configurations"]
    """<p>The configurations of the connection.</p>"""
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where a connection is to be updated.</p>"""
    identifier: "capo_datazone.types.connection_id.ConnectionId"
    """<p>The ID of the connection to be updated.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of a connection.</p>"""
    aws_location: NotRequired["capo_datazone.types.aws_location.AwsLocation"]
    """<p>The location where a connection is to be updated.</p>"""
    props: NotRequired[
        "capo_datazone.types.connection_properties_patch.ConnectionPropertiesPatch"
    ]
    """<p>The connection props.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectionInput) -> dict:
    out: dict = {}
    if "configurations" in value:
        import capo_datazone.types.configurations

        out["configurations"] = capo_datazone.types.configurations.serialize_json(
            value["configurations"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "aws_location" in value:
        import capo_datazone.types.aws_location

        out["awsLocation"] = capo_datazone.types.aws_location.serialize_json(
            value["aws_location"]
        )
    if "props" in value:
        import capo_datazone.types.connection_properties_patch

        out["props"] = capo_datazone.types.connection_properties_patch.serialize_json(
            value["props"]
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectionInput:
    out: UpdateConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("configurations") is not None:
        import capo_datazone.types.configurations

        out["configurations"] = capo_datazone.types.configurations.deserialize_json(
            data["configurations"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("awsLocation") is not None:
        import capo_datazone.types.aws_location

        out["aws_location"] = capo_datazone.types.aws_location.deserialize_json(
            data["awsLocation"]
        )
    if data.get("props") is not None:
        import capo_datazone.types.connection_properties_patch

        out["props"] = capo_datazone.types.connection_properties_patch.deserialize_json(
            data["props"]
        )
    return out


def redact_sensitive(value: UpdateConnectionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "props" in value:
        import capo_datazone.types.connection_properties_patch

        out["props"] = capo_datazone.types.connection_properties_patch.redact_sensitive(
            value["props"]
        )
    return out
